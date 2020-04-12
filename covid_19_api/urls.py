from django.urls import path
from .views import (home,
                    LogList,
                    CovidData,
                    CovidDataJson,
                    CovidDataXML)

urlpatterns = [
    path('',home,name="home"),
    path('api/v1/on-covid-19/logs/',LogList.as_view()),
    path('api/v1/on-covid-19/',CovidData.as_view()),
    path('api/v1/on-covid-19/json',CovidDataJson.as_view()),
    path('api/v1/on-covid-19/xml',CovidDataXML.as_view()),
]