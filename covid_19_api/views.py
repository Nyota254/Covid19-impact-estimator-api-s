from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Log
from .serializers import LogSerializer,RegionSerializer,CovidDataEntrySerializer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from timeit import default_timer as timer
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog


def estimator(data):
  '''
  Method for impact estimation on the covid_19 pandemic based on calculations
  and studys by Havard Medical School and Massachusetts General Hospital

  Args:
      Dictionary data such as the example below.
      {
        'region': {
        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 4,
        'avgDailyIncomePopulation': 0.73
        },
        'periodType': "days",
        'timeToElapse': 38,
        'reportedCases': 2747,
        'population': 92931687,
        'totalHospitalBeds': 678874
      }
  '''
  #original data storage
  originalData = data

  #Calculations for Currently infected

  currentlyInfectedImpact = int(data['reportedCases'] * 10)
  currentlyInfectedSeverImpact = int(data['reportedCases'] * 50)


  # Start of calculations for infections by requested time. factoring in one will use
  # days,weeks and months

  if data['periodType'] == "weeks":
    data['timeToElapse'] = data['timeToElapse'] * 7

  elif data['periodType'] == "months":
    data['timeToElapse'] = data['timeToElapse'] * 30

  else:
    pass

  powerNumber = int(data['timeToElapse']/3)
  infectionsByRequestedTimeImpact = int(currentlyInfectedImpact * (2**powerNumber))
  infectionsByRequestedTimeSeverImpact = int(currentlyInfectedSeverImpact * (2**powerNumber))

  #Start of calculations for severcases of infection that will require hospitalization

  severeCasesByRequestedTimeImpact = int(0.15 * infectionsByRequestedTimeImpact)
  severeCasesByRequestedTimeSevereImpact = int(0.15 * infectionsByRequestedTimeSeverImpact)

  #Start of calculation for number of hospital beds available for covid_19 Patients at requested time

  availableBeds = 0.35 * data['totalHospitalBeds']
  hospitalBedsByRequestedTimeImpact = int(availableBeds - severeCasesByRequestedTimeImpact)
  hospitalBedsByRequestedTimeSeverImpact = int(availableBeds - severeCasesByRequestedTimeSevereImpact)

  #Start of calculation for ICU cases

  casesForICUByRequestedTimeImpact = int(0.05 * infectionsByRequestedTimeImpact)
  casesForICUByRequestedTimeSeverImpact = int(0.05 * infectionsByRequestedTimeSeverImpact)

  #Ventilator Requirements
  casesForVentilatorsByRequestedTimeImpact = int(0.02 * infectionsByRequestedTimeImpact)
  casesForVentilatorsByRequestedTimeSeverImpact = int(0.02 * infectionsByRequestedTimeSeverImpact)

  #Economy loss calculation

  dollarsInFlightImpact = int((infectionsByRequestedTimeImpact * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])
  dollarsInFlightSeverImpact = int((infectionsByRequestedTimeSeverImpact * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])

  # data to be returned inform of a dictionary
  data = {'data':{'region': {
                              'name': originalData['region']['name'],
                              'avgAge': originalData['region']['avgAge'],
                              'avgDailyIncomeInUSD': originalData['region']['avgDailyIncomeInUSD'],
                              'avgDailyIncomePopulation': originalData['region']['avgDailyIncomePopulation']
                            },
                  'periodType': originalData['periodType'],
                  'timeToElapse': originalData['timeToElapse'],
                  'reportedCases': originalData['reportedCases'],
                  'population': originalData['population'],
                  'totalHospitalBeds': originalData['totalHospitalBeds']
          },

                        'impact':{'currentlyInfected': currentlyInfectedImpact,
                                'infectionsByRequestedTime': infectionsByRequestedTimeImpact,
                                'severeCasesByRequestedTime': severeCasesByRequestedTimeImpact,
                                'hospitalBedsByRequestedTime': hospitalBedsByRequestedTimeImpact,
                                'casesForICUByRequestedTime': casesForICUByRequestedTimeImpact,
                                'casesForVentilatorsByRequestedTime':casesForVentilatorsByRequestedTimeImpact,
                                'dollarsInFlight': dollarsInFlightImpact
                        },

                        'severeImpact':{'currentlyInfected':currentlyInfectedSeverImpact,
                                      'infectionsByRequestedTime': infectionsByRequestedTimeSeverImpact,
                                      'severeCasesByRequestedTime':severeCasesByRequestedTimeSevereImpact,
                                      'hospitalBedsByRequestedTime': hospitalBedsByRequestedTimeSeverImpact,
                                      'casesForICUByRequestedTime': casesForICUByRequestedTimeSeverImpact,
                                      'casesForVentilatorsByRequestedTime':casesForVentilatorsByRequestedTimeSeverImpact,
                                      'dollarsInFlight': dollarsInFlightSeverImpact
                        }
  }

  return data


def home(request):
    '''
    Home page
    '''
    title="covid estimator api"
    context = {
        "title":title
    }
    
    return render(request,"home.html",context)

class CovidData(LoggingMixin,APIView):
    def post(self, request, format=None):
        serializers = CovidDataEntrySerializer(data=request.data)
        if serializers.is_valid():
            return Response(estimator(serializers.data), status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CovidDataJson(LoggingMixin,APIView):
    def post(self, request, format=None):
        serializers = CovidDataEntrySerializer(data=request.data)
        if serializers.is_valid():
            return Response(estimator(serializers.data), status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get(self,request,formart=None):
    #     serializers = CovidDataEntrySerializer(data=request.data)
    #     if serializers.is_valid():
    #         return Response(estimator(serializers.data))
    
class CovidDataXML(LoggingMixin,APIView):
    renderer_classes = [XMLRenderer]
    def post(self, request, formart=None):
        serializers = CovidDataEntrySerializer(data=request.data)
        if serializers.is_valid():
            return Response(estimator(serializers.data), status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get(self,request,formart=None):
    #     serializers = CovidDataEntrySerializer(data=request.data)
    #     if serializers.is_valid():
    #         return Response(estimator(serializers.data))
    

class LogList(LoggingMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'log_list.html'
    
    def get(self, request):
        queryset = APIRequestLog.objects.all()
        return Response({'logs': queryset},content_type='text/plain')
