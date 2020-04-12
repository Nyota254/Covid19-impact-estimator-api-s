from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('responseTime')
        
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