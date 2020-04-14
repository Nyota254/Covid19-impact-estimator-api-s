# Covid_Impact_Estimator_Api's

This are api end points for corona virus impact estimation.its aimed at helping society and leaders prepare for the real big problem of COVID-19, which has an impact on lives, health systems, supply chains, and the economy.

* Too many patients, not enough hospitals and beds. A serious shortage of ventilators, masks and other PPE - if we don’t practice social distancing.
* Job losses or freezes, low cash flow and low production (even for essentials like food). These and more from too many people being sick, a sizable number dying (including some of the best people in many fields), and many others affected by the impact of losing loved ones or a world operating in slow motion

# Endpoints
1. POST API'S.

**JSON RESPONSE PREFERENCE ENDPOINTS**
 
* https://covid-impact-estimator.herokuapp.com/api/v1/on-covid-19
* https://covid-impact-estimator.herokuapp.com/api/v1/on-covid-19/json
 
 This api enpoint allows one to input data in the following json formart. 

 ```
 {
       "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 4,
        "avgDailyIncomePopulation": 0.73
        },
        "periodType": "days",
        "timeToElapse": 38,
        "reportedCases": 2747,
        "population": 92931687,
        "totalHospitalBeds": 678874
}  
 ```
 The api then processess the information and returns data in the following formart

 ```
 {
  "data": {
    "region": {
      "name": "Africa",
      "avgAge": 19.7,
      "avgDailyIncomeInUSD": 4.0,
      "avgDailyIncomePopulation": 0.73
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874
  },
  "impact": {
    "currentlyInfected": 27470,
    "infectionsByRequestedTime": 112517120,
    "severeCasesByRequestedTime": 16877568,
    "hospitalBedsByRequestedTime": -16639962,
    "casesForICUByRequestedTime": 5625856,
    "casesForVentilatorsByRequestedTime": 2250342,
    "dollarsInFlight": 8646052
  },
  "severeImpact": {
    "currentlyInfected": 137350,
    "infectionsByRequestedTime": 562585600,
    "severeCasesByRequestedTime": 84387840,
    "hospitalBedsByRequestedTime": -84150234,
    "casesForICUByRequestedTime": 28129280,
    "casesForVentilatorsByRequestedTime": 11251712,
    "dollarsInFlight": 43230261
  }
}
 ```

**XML PREFERENCE ENDPOINT**

* https://covid-impact-estimator.herokuapp.com/api/v1/on-covid-19/xml

api recieves the same data in json formart and returns data in xml formart.

```
<?xml version="1.0" encoding="utf-8"?>
<root>
  <data>
    <region>
      <name>Africa</name>
      <avgAge>19.7</avgAge>
      <avgDailyIncomeInUSD>4.0</avgDailyIncomeInUSD>
      <avgDailyIncomePopulation>0.73</avgDailyIncomePopulation>
    </region>
    <periodType>days</periodType>
    <timeToElapse>38</timeToElapse>
    <reportedCases>2747</reportedCases>
    <population>92931687</population>
    <totalHospitalBeds>678874</totalHospitalBeds>
  </data>
  <impact>
    <currentlyInfected>27470</currentlyInfected>
    <infectionsByRequestedTime>112517120</infectionsByRequestedTime>
    <severeCasesByRequestedTime>16877568</severeCasesByRequestedTime>
    <hospitalBedsByRequestedTime>-16639962</hospitalBedsByRequestedTime>
    <casesForICUByRequestedTime>5625856</casesForICUByRequestedTime>
    <casesForVentilatorsByRequestedTime>2250342</casesForVentilatorsByRequestedTime>
    <dollarsInFlight>8646052</dollarsInFlight>
  </impact>
  <severeImpact>
    <currentlyInfected>137350</currentlyInfected>
    <infectionsByRequestedTime>562585600</infectionsByRequestedTime>
    <severeCasesByRequestedTime>84387840</severeCasesByRequestedTime>
    <hospitalBedsByRequestedTime>-84150234</hospitalBedsByRequestedTime>
    <casesForICUByRequestedTime>28129280</casesForICUByRequestedTime>
    <casesForVentilatorsByRequestedTime>11251712</casesForVentilatorsByRequestedTime>
    <dollarsInFlight>43230261</dollarsInFlight>
  </severeImpact>
</root>

```
2. Get Apis

**LOGS FROM THE API REQUESTS**
* https://covid-impact-estimator.herokuapp.com/api/v1/on-covid-19/logs


example response
```
POST   /api/v1/on-covid-19/    201    02ms
POST   /api/v1/on-covid-19/    201    02ms
POST   /api/v1/on-covid-19/json    201    02ms
```

## LOCAL MACHINE SETUP

## Getting Started

Fork this repository or clone it to your local machine on ubuntu use the following commands
```
git clone 
```

### Prerequisites

1. You will need to install the following for you you to be able to run the following application in your local machine.
* Python version 3.6
* postgres database

### Installing

A step by step series of examples that tell you how to get a development env running

2. set up a virtual environment using the following command

```
python3.6 -m venv --without-pip virtual
```

And activate it

```
source virtual/bin/activate
```
3. install the latest version of pip

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

4. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
5. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
6. create postgres database
```
CREATE DATABASE <your-database-name>
```
7. create a migration using the following command
```
python3.6 manage.py makemigrations
```

and migrate
```
python3.6 manage.py migrate
```
8. create a admin account
```
python 3.6 manage.py createsuperuser
```
and add your credentials

9. run the application using 
```
python3.6 manage.py runserver
```
10. navigate to the admin panel by typing 
```
localhost:8000/admin
```


