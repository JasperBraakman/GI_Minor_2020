# Practical Assignment 1 - py1 Air Quality - API 

## Introduction
A recent study of SPINlab researcher [Dr. Bo Andrée](https://research.vu.nl/en/persons/bo-pieter-johannes-andree) showed a relationship between air pollution and confirmed COVID-19 cases. He concluded that a high level of Particulate Matter with a diameter of 2.5 μm or less per m3 is a highly significant predictor for the number of confirmed COVID-19 cases and related hospital admissions. Why this is the case...? that is still unclear. The two most accepted theories are however that either people living in areas with high levels of air pollution already have lung damage due to the pollution, or that the virus latches on aerosols in the air which speeds up the spread of the virus. Either way, the results of this study are important in understanding how to deal. It shows that more and or different measures might have to be taken to protect people that live in areas with high levels of air pollution.

The results of this study even made it to the national [news](https://spinlab.vu.nl/relation-between-air-pollution-and-confirmed-covid-19-cases-researched/).

To access the full article follow this link and download the pdf: https://openknowledge.worldbank.org/handle/10986/33664
For this study Andrée used spatial data about the average level of particulate matter per m3 in 2017 which he obtained from the "Atlas van de leefomgeving" - the atlas of the living environment [link](https://www.atlasleefomgeving.nl/kaarten). The data layers he used are: 
- [Particulate Matter 2.5 μm or less per m3](https://nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/metadata/1689e358-6555-4b5d-902f-7bc36cf2c266) 
- [Particulate Matter 10 μm or less per m3](https://nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/metadata/10b1f613-e492-44f6-9745-b444880c136b?tab=general)

Both layers are the result of interpolated data points from measuring stations. A full description about how these data layers are modelled can be found [here](https://www.nsl-monitoring.nl/informatie/data-nsl/) (in Dutch). 

In this practical assignment it is your task to collect data from air measuring stations and to see how these match with the modelled dataset used by Andrée. For this you are going to use the luchtmeetnet (Air measurement network). Luchtmeetnet is hosted by the Netherlands National Institute for Public Health and the Environment (or Rijksinstituut voor Volksgezondheid en Milieu (RIVM)) and contains information about air quality.

## About APIs 
Before we start, it is important to know a bit more about the data. Data gets made available in different ways. Sometimes you can simply go to a website and click a download link, sometimes you need to [scrape it off a website](https://realpython.com/python-web-scraping-practical-introduction/), and sometimes you can use an [API (application programming interface)](https://en.wikipedia.org/wiki/Application_programming_interface). An API is a set of definitions and methods for different computer software to communicate with each other. It is a general term, but in the context of data acquisition an API makes it easier to retrieve data in an automatic way. To make use of this automation we need a way to tell the computer how to use the API. This can be done using various tools and/or programming languages. We will use python to this end, since it is a very accessible and flexible programming language, with a lot of modules available able to provide a broad range of extra functionality. Python is also the programming language used by GIS packages such as ArcGIS (arcpy) and QGIS.

As a data source for this practical assignment we are going to use the the Luchtmeetnet (air measurements network) API published by the RIVM. The luchtmeetnet contains measurements of different chemical compounds in the air and can be accessed here: 

https://api.luchtmeetnet.nl/open_api

The RIVM also made an interactive mapviewer out of it. This can be accessed here: https://www.luchtmeetnet.nl/

The documentation of this API can be found at https://api-docs.luchtmeetnet.nl/#intro. 

The techniques used in this exercise can also be used to download data from many more API's from other sources, since most API's follow a similar structure, which is called [REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

## Requests

To retrieve data from the API we will use the `requests` module. Requests is a fairly straight forward, easy to use, and powerful library for sending requests over the internet (HTTP). Requests retrieves data from an url, which can be a website, an image, or any other file. It stores the response from the server in an python object. From this object you can get all the needed information. A basic request using requests looks like this:

First we import the module:
```python
import requests
```
Then we request data using a url (in this case a website):
```python
response = requests.get('https://github.com/SPINLab/GI_Minor_2020/')
```
The website (html file) is now stored in the response object `response`. You can see the content as follows:
```python
print(response.content)
```
A REST API will always respond with [JSON](https://en.wikipedia.org/wiki/JSON) data. JSON is a file format that is very commonly used for sending data over the internet. It is composed of key-value pairs (using curly brackets {}) and lists (using square brackets []). An example (taken from Wikipedia):
```json
{
    "firstName": "John",
    "lastName": "Smith",
    "isAlive": true,
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        },
        {
            "type": "mobile",
            "number": "123 456-7890"
        }
    ],
    "children": [],
    "spouse": null
}
```
You might have noticed that this is exactly the format of Python dictionaries and lists. A response from Requests will have a [method specifically made to deal with JSON data](https://3.python-requests.org/user/quickstart/#json-response-content) and will return a Python dictionary. Perfect for when we want to use the data in Python. It is used as follows:
```python
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
response_dictionary = response.json()
print(response_dictionary)
print(response_dictionary['userId'])
```
## Getting Started
For this practical assignment we have prepared two exercises which will help you to understand which steps you will need to take to extract data from luchtmeetnet in order to reproduce the map for the average level of particulate matter per m3 in 2017. However, before you open them we first want you to go to the [Luchtmeetnet API documentation](https://api-docs.luchtmeetnet.nl/#intro) and explore the API (what directories are there? What data do they return? Which options do they have?) Think of which url we can use to retrieve a list of measurement locations (stations) and how to retrieve information about a station.

## Excercise 1: Basic Info
Once you explored the API open [1_basic_info.py](https://github.com/JasperBraakman/GI_Minor_2020/blob/master/py1_LuchtmeetnetAPI/1_basic_info.py) in spyder and go trough the different steps. This script will allow you to retrieve basic information from the API. The file contains pointers and hints to help you. But remember, coding can be very frustrating. Most of the time you are trying different approaches to find out that you were on the wrong path. In the end it will be very rewarding to finally get what you we looking for. 

## Excercise 2: Timeseries data
Now that you understand how to get basic information from the Luchtmeetnet API we are going to obtain data from a specific time period. Have another look at the [Luchtmeetnet API documentation](https://api-docs.luchtmeetnet.nl/#intro) and try to determine which url we could use to request measurement data of a single station? Which parameters would we have to set? Now choose a location (for example the one in Amsterdam of the previous exercise) and retrieve the location number. Next, open [2_timeseries.py](https://github.com/JasperBraakman/GI_Minor_2020/blob/master/py1_LuchtmeetnetAPI/2_timeseries.py) and create a python script which retrieves and plots measurement data of a station.

## Practical Assignment 
With the two exercises completed you are now ready for the practical assignment. to extract the data from the luchtmeetnet API which can be used as input to reproduce the map for the average level of particulate matter of 2.5 μm and 10 μm or less per m3 of a week in 2017. Note, that we do not ask you to interpolate the data. We just want you to extract the different point datasets. 

Again have a look at the [Luchtmeetnet API documentation](https://api-docs.luchtmeetnet.nl/#intro) and determine which data we need to request to make a map of all stations colored by the measurement of a particulate matter of 2.5 μm and 10 μm or less per m3. Now open Practical_assignment_1.py and create a python script which retrieves the average measurement data of PM 2.5 and PM 10 for 2017 for all of the Netherlands.

The script you have to produce must result in a shapefile `measurements.shp`containing the average PM 2.5 and PM10 measurements for a week in 2017.

Once you finished the script go to https://www.atlasleefomgeving.nl/kaarten and download the PM 10 and PM 2.5 map data used by Andrée. Add the shape files you created and the downloaded data in a GIS (ArcGIS pro or QGIS) and systematically compare the data you retrieved from the luchtmeetnet API. Answer the following: 
   1. Which functionalities in GIS have you used to compare the data point with the modelled raster layer?
   2. Do the measurements from the Luchtmeetnet correspond with the datalayer PM 10 and PM 2.5 from the atlas van de leefomgeving?
   3. Do you think that the measurements from the Luchtmeetnet are sufficient as input for to generate the maps layers? 
   4. Image that Andrée would have used the data from the Luchtmeetnet directly in the way you did. How do you think that would have changed his analysis?
   5. Now look back at the fit for purpose framework you developed for the first practical assignment. How fit would your generated point data be for the purpose of Andrée´s study? 

Save your answers to a file named `py1_air_quality_answers.txt`.

## Submit the following

Create a .zip file containing the following files 
- `Practical_assignment_1.py` 
- `measurements.shp` (with all auxiliary files; remember the Kenya practical assignment)
- `py1_air_quality_answers.txt`

Submit it to Canvas **before the 25th of September 23:59**. 
