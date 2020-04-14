from rest_framework import serializers
from rest_framework_tracking.models import  APIRequestLog

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIRequestLog
        fields = ["method","path","status_code","response_ms"]
        
        
class RegionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    avgAge = serializers.FloatField()
    avgDailyIncomeInUSD = serializers.FloatField()
    avgDailyIncomePopulation = serializers.FloatField()
    
class CovidDataEntrySerializer(serializers.Serializer):
    region = RegionSerializer()
    periodType = serializers.CharField(max_length=10)
    timeToElapse = serializers.IntegerField()
    reportedCases = serializers.IntegerField()
    population = serializers.IntegerField()
    totalHospitalBeds = serializers.IntegerField()