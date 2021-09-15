###############################################################################################
# This is the second Exercise for the practical assignment to learn python for API´s.        #
# Prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Simeon Nedkov, Chris Lucas, Maurice de Kleijn, Devi Brands                                  #
###############################################################################################

# For this excercise we are going look into the air measurements for a specific station for a specific chemical compound.
# For this we will be using the following modules. The first one you are already familiar with from the first exercise. 
# The other´s will be explained once you are going to use them for your code
import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: As first step we want you to to choose a station number (e.g. the number of the station of the previous exercise) and save to a variable.
# Write this line of code below:


# Step 2: Choose a chemical compound and request the data (no need to specify a page yet, you will by default recieve the most recent page)
# Create a dictionary of the response in the same way you did in the previous exercise.
# hint: you need to specify the station number in the URL
# hint: you need to specify the chemical compound in the parameters of the request (https://requests.readthedocs.io/en/master/user/quickstart/?highlight=parameters#passing-parameters-in-urls)
# hint: look in the API documentation what the parameter to define a chemical compound is called (https://api-docs.luchtmeetnet.nl/#intro)
# Write your lines of code below:


# Step 3: Now that we have the specific component we are going to 
# Create a list of values of the measured quantity of the chosen chemical compound and
# Create a list of corresponding timestamps
# hint: look in the data where the measured quantities and timestamps are stored
# hint: you will need to loop over the retrieved data
# hint: create empty lists and append the data to the lists in the loop (check your training material if you forgot how)
# Write your lines of code below:


# Step 4: For this step we are going to prepare the timestamp data in order to plot it as a graph. 
# You probably noted that the timestamps are strings that are build in a certain way (a format)
# Before we can plot the data we therefore need to tell the computer how to interpret this string
# and create a datetime object with it that python can interpret
# (As promised above we would inform you when one of the modules above is used. At this point we are going to use datetime.)
# For simplicity we give you the correct time format: 
# REMOVE THE HASHTAG IN THE NEXT LINE 
#time_format = '%Y-%m-%dT%H:%M:%S+00:00'

# Now change the loop so that the timestamp information is parsed using the format (https://pymotw.com/2/datetime/#formatting-and-parsing)
# Write your lines of code below:


# Step 5: Now we want you to plot the data in a graph. For this we want you to use the matplotlib module (which we imported above). 
# We want you to plot timestamps on the X-axis and values for the chemical components on the Y-axis. 
# Please look at https://pythonspot.com/plot-time-with-matplotlib/ on how to do so.
# Write your lines of code below:


# Step 6: In the plot you probably notices we can see it only spans a pretty limited timespan. 
# For this next step we want you to increase this. To do so we need to retrieve more pages of data (e.g. 10 pages)
# hint: use the 'page' parameter to define which page you want to request (http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
# hint: we now need to pass two parameters with the request (chemical compund and page number)
# hint: use a loop to request multiple pages
# hint: first create the empty lists again and then append the data in the loop
# hint: you can create a loop within a loop
# write your lines of code below:


# Step 7: Now plot it (https://pythonspot.com/plot-time-with-matplotlib/)


# Step 8: it might be that the graph looks wrong in some places now
# this is due the data not being sorted by date
# to sort the data by date we are going to create a DataFrame using the pandas module (which we imported as pd above)
# a DataFrame is a datatype that stores tabular data, kinda like an excel sheet
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
# To get you started we have prepared a couple of lines to initaite a DataFrame:
# REMOVE THE HASHTAG IN THE NEXT LINE
# df = pd.DataFrame()
# df['timestamps'] = timestamps
# df['NO2'] = values

# now that the data is in a DataFrame we can use the sort_values function of the DataFrame to sort the values by the timestamps 
# Look here how that is done https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
# write the sort function for timestaps in the line below:


# Step 9: pandas DataFrames also come with easy function to make a plot, use it to create a plot of the sorted data
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html


# Step 10: In order to use the data in different software package (like GIS software, SPSS, excel or MS Access) it might in some cases be useful to save your dataframe to a csv.
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
# To do so we have prepared the following line. 
# REMOVE THE HASHTAG IN THE NEXT LINE
#df.to_csv('timeseries.csv')
