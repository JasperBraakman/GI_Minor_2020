# Practical Assignment 2 - py2 Traffic data

## Introduction

In the [previous practical assignment](https://github.com/SPINLab/GI_Minor_2020/tree/master/py1_LuchtmeetnetAPI) you have learned how to get data from air measurement stations. For this practical assignment we are going to combine data about air quality with traffic data. We want you to look at a two measurement stations and see whether you can find a relationship between the number of cars and the air quality, in partical nitrogen compounds (NO and NO2). But let us first have a look at the traffic data.  

## Traffic data

Information about traffic can be obtained from different sources. Much of this data is not available as open data. You will often need to sign an agreement or buy a licence. Whenever you have such an agreement you will often get an api_key which you need to include in your script and which provides access to the API in the same way as with Luchtmeetnet. For many of these data sources you can create a free account which offers limited but still very useful functionalities. Good platforms that you could use to get traffic information from are:

 - [HERE](https://www.developer.here.com/documentation/traffic/dev_guide/topics/what-is.html) 
 - [TOMTOM](https://developer.tomtom.com/)
 - [Flitsmeister](https://www.flitsmeister.nl/fcd.html) 

And remember, these APIs have a lot of data. They have live data and historical data that go back a couple of years. Working with these very large datasets is genrally considered as Big Data analytics. Another thing that is interesting to notice is that the data these sources offer is obtained from the users that use their devices and apps. In some cases  such commerical parties thus know more about our traffic behaviour than the government. Interesting times, right?   

Information about traffic on the Dutch highways is available at the [National Data Warehouse for Traffic Information (NDW)](https://www.ndw.nu/en/). This data is not collected through users that use a certain app or that installed a certain sensor on their vehicle, but works the other way around. NDW data is foremost obtained through external sensors like cameras, rubber tubes or loop detectors. Like the data sources above also NDW is not fully open data. 

They do offer a very useful open data tool with which you can generate an excel sheet with the number of vehicles for a certain period. 

https://dexter.ndwcloud.nu/opendata

This tool is limited to 10 stations per download, so whenever you are interested in a small area this can be very useful. The excelsheet is however not structured in the way that you can easily use it in a GIS. For this practical assignment it is your task to convert the data into usable GIS data. Some steps could have easily been done manually as well, but imagine you would want to include multiple time series in your analysis. Not only would it be very error sensitive to manually convert all data, it would also be very labor intensive.

## Python to read and write Excel files
One of the main purposes for which you will use python is to preprocess your data before performing an analysis. A huge advantage of scripting data processing steps is that it remains transparant what you exactly did, thus reproducable by other researcher. There are multiple modules that allow you to proces (read and write) data from excel sheets. The most popular is [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html), but older alternatives like [openpyxl](https://openpyxl.readthedocs.io/en/stable/) or [xlrd](https://xlrd.readthedocs.io/en/latest/) are still useful. For this practical assignment we want you to work with [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html).

# Practical Assignment

In order to see the effect of traffic on air quality, we are going to compare the traffic and air quality measurements from April 2019 and April 2020. We will do so for the air quality measuring station alongside the Ring A10 `Amsterdam-Einsteinweg` and the station alongside highway A2 near `Breukelen-A2`. The Netherlands was in lockdown due to the COVID-19 virus in April 2020, we therefore expect that there was less traffic which might have led to better air quality.  It is up to you to find out! 

## Traffic data
To get your data go to: https://dexter.ndwcloud.nu/opendata

For the first excelsheet we want you to fill in `15-04-2019` for `Begindatum` (startdate) and `19-04-2019` for `Einddatum` (Enddate). Select the traffic measuring stations by clicking on `Locatieselectie aanpassen` go to `Klembord` and paste the following in `Selectie uit klembord` (these are 4 stations near `Amsterdam-Einsteinweg` and 4 stations near `Breukelen-A2`):

```python
RWS01_MONIBAS_0021hrl0459ra
RWS01_MONIBAS_0021hrl0469ra
RWS01_MONIBAS_0021hrr0457ra
RWS01_MONIBAS_0021hrr0469ra
RWS01_MONIBAS_0101hrl0257ra
RWS01_MONIBAS_0101hrl0261ra
RWS01_MONIBAS_0101hrr0258ra
RWS01_MONIBAS_0101hrr0261ra
```

Now click on `+Toevoegen` and confirm by clicking on `Bevestigen`. For `Naam` `2019`, fill in your email adress, check the `Ik ben geen robot` (I am not a robot) box and click at `Aanvraag starten`. Wait a bit and the download will be ready. 

Once you downloaded the 2019 sheet go through the proces a second time (you might have to refresh by pressing `F5`) but now change the `Begindatum` to `13-04-2020` and the `Einddatum` to `17-04-2020` and fill in for `Name` `2020`. 

When you open the excel sheet you will notice that the data is structured, but not in a way in which it can easily be intgrated into your GIS. Restructuring the data can be done manually, but is error sensitive and not easily reproducable. Since you are trained as researchers we want you to not modify the downloaded data, but instead generate a new datafile without touching the orginal data. Whenever publishing an academic report you can accompany it with your data processing scripts (which most researchers currently publish on platforms like GIThub, the platform where this practical assignment is published on as well). 

For this practical assignment we want you to create a CSV `traffic_april_1920.csv`file with the following columns (please note that the values in the table are made up). 

| ID | X_coord | Y_coord | vehicles_2019 | vehicles_2020 |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| RWS01_MONIBAS_0100vwb0183ra | 52.3396955| 4.8836328 |  13956.1 | 5816.5 |
| RWS01_MONIBAS_0100vwb0199ra | 52.3389098| 4.8604215 |  20715.5 | 9487.2 |
| ... | ... | ... | ... | ... |

**ID** represents the unique ID of the sensor and can be found on either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `B7:B16` this column must be stored as string / text.

**X_Coord** represents the Longitude of the sensor and can be found either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `D7:D16`. This column must be stored as float or double in order for your GIS to be recognized as number.

**Y_Coord** represents the Latitude of the sensor and can be found either the `2019.xlsx`or `2020.xlsx` excel files on sheet `overzicht` cells `E7:E16`. This column must be stored as float or double in order for your GIS to be recognized as number.

**vehicles_2019** are the total number of cars that passed this sensor for the predefined period. These figures can be found in `2019.xlsx` on the `intensiteit` sheet in the different cells that provide `Totaal` under the column `intensiteit`. For sensor `RWS01_MONIBAS_0021hrl0459ra` this is cell B30 fo sensor `RWS01_MONIBAS_0021hrl0469ra` this is `B67` for `RWS01_MONIBAS_0100vwc0175ra` this is `B104` (do you see the pattern?).

**vehicles_2020** are the total number of cars that passed this sensor for the predefined period. These figures can be found in `2020.xlsx` on the `intensiteit` sheet in the different cells that provide `Totaal` under the column `intensiteit`. For sensor `RWS01_MONIBAS_0021hrl0459ra` this is cell B30 fo sensor `RWS01_MONIBAS_0021hrl0469ra` this is `B67` for `RWS01_MONIBAS_0100vwc0175ra` this is `B104` (do you see the pattern?).

It is now up to you to do this. Go through the documentation of [pandas] and in particular have a look at this [tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write).

To help you a bit, we have prepared 1_traffic.py in which we included some tips on how to create your script. 

## Air Quality data

In order to see which stations are near to the traffic sensors, we want you to add the traffic shapefile and the measurement stations from the previous practical assignment to your GIS (if you want, you can also get it done using buffer analysis using **arcpy** or **geopandas**, however let´s take it easy for the moment). We are going to focus at nitrogen compounds for which we will focus at NO and NO2. Now select the air quality measurement stations `Amsterdam-Einsteinweg` and `Breukelen-A2` and modify the script from the previous assignment to get the data for the periods in **April 2019** and **April 2020**. Make sure to include average measurements for NO and NO2. 

Name your script: `py2_air_april_1920.py`. 

Create a shapefile named `air_q_april_1920.shp` containing the following table structure.

| ID_AQ | X_coord | Y_coord | 19_NO | 19_NO2 | 20_NO | 20_NO2 
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| ... | ... | ... | ... | ... |... | ... |

**ID_AW** represents the unique ID of the Air Quality station. This column should be stored as string / text.

**X_Coord** represents the Longitude of the measuring station.

**Y_Coord** represents the Latitude of the measuring station.

**19_NO** should contain the average measurements for NO in April 2019 (15/4 - 19/4): stored as a number (float).

**19_NO2** should contain the average measurements for NO2 in April 2019 (15/4 - 19/4): stored as a number (float).

**20_NO** should contain the average measurements for NO in April 2020 (13/4 - 17/4): stored as a number (float).

**20_NO2** should contain the average measurements for NO2 in April 2020 (13/4 - 17/4): stored as a number (float).


## Comparing the Air Quality and Traffic
Now that you created two CSV files we want you to compare April 2019 with April 2020. Although various statistical methods exist and obviously interpolation and distance decay functionalities should be included to analyse this in a more robust academic manner, for this assignment we want you to just explore the data and compare the figures visually in GIS. Answer the following questions:

1. What do you see when you compare the air quality of April 2019 with April 2020.
2. How would you interpret these results in relation to the amount of traffic? What conclusions would you draw from your explorative analysis?
3. What other information would you need to analyse the relationship between air quality and traffic?

Save your answers in a file named `py2_answers.txt`

## Submit the following

Create a .zip file containing the following files 

- `py2_traffic.py` which contains the script with which you modify the traffic data into a useable shapefile.
- the generated shapefile `traffic_april_1920.csv`
- `py2_air_april_1920.py` Note that we have not provided an auxiliary file. 
Please reuse the file you submitted for the previous assignment and change it´s configuration.
- the generated shapefile `air_q_april_1920.csv`
- `py2_answers.txt`

Submit this zip to Canvas **before the 20th of September 23:59**. 
