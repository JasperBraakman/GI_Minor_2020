###############################################################################################
# This is Excercise 1 for the practical assignment to learn python for API´s                  #
# prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Simeon Nedkov, Chris Lucas, Maurice de Kleijn, Devi Brands                                  #
###############################################################################################

# Since we want to be able to get data out of the luchtmeetnet we first we import the request module (which we already did for you) 
# documentation on the request module : https://3.python-requests.org/

import requests


# In order to understand how the luchtmeetnet API works, we want you to go through the following steps. 
# Step 1: First we need to find the URL with which we can access the API and get to the different stations. Go to https://api-docs.luchtmeetnet.nl/#intro and search for the right URL.
# Hint: the base url reverded to in the documentations is 'https://api.luchtmeetnet.nl'
# Add this URL to a get request that you store as a response object. Put this request in the line below:


# Step 2: In order to access the various data nodes we now want you to create a python dictionary from the response object by reading the API output. You probably noticed the API generates json output so make sure to read json. 
# Hint: see read.me file
# Write your line(s) of code below:

# Now that the response from the API is added to a dictionary you can explore the response using the variable explorer of Spyder or by printing it out to console.
# Step 3: In this step we want you to save the first location to a variable and print it out to the console.


# Step 4: Now go through the dictionary and select a station that is within Amsterdam (or any other city you prefer).
# Save location name and station number to variables and print them out to console.
# Write your line(s) of code below:


# Now that we isolated one station we want you to get specific air quality measurements from that station. 
# Step 5: In order to do so we want you to request the data of your chosen station and create a python dictionary.
# Hint: you need to specify the station number in the URL. In order to see how that is done please check the API documentation (https://api-docs.luchtmeetnet.nl/#intro) for an example.
# Now use the variable for the station number created in step 4.
# Write your line(s) of code below:


# Step 6: Since we, as Geo Information students, are interested in locations we want you to save:
# 1. the description
# 2. the chemical compounds which are measured at this station
# 3. the location (coordinates) to variables 
# print the results.
# Write your line(s) of code below:



