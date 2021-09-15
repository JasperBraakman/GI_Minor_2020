###############################################################################################
# This is the auxiliary file for the practical assignment to learn python for API´s.          #
# Prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Maurice de Kleijn, Devi Brands                                                              #
###############################################################################################

# For this assignment we do provide most off the code, you will only need to download the data and fill in the correct collums.
# It is your task to create a script that generates a CSV file with information about traffic
# from the excelsheet you downloaded for april 2019 (15/04 - 19/04) and april 2020 (13/04 - 17/04) from https://dexter.ndwcloud.nu/opendata
# the  CSV file should contain the following fields:
# ID 	X_coord 	Y_coord 	vehicles_2019 	vehicles_2020

# to create this file you will need the following modules 
import pandas as pd

# Step 1: Fill in the correct names of the collums where the code says '...'.
# Hint: if no name is written on line one of the excelsheet use the Name 'Unnamed: x',
# where x represents the number of the colom (remember that python starts countring from 0 and not 1)
# Hint: make sure that the excel files are in the same folder as your .py file

#load 2019 and 2020 data
stations=pd.read_excel("2019.xlsx")
traffic_19=pd.read_excel("2019.xlsx",sheet_name='Intensiteit')
traffic_20=pd.read_excel("2020.xlsx",sheet_name='Intensiteit')

#create dataframe that will be used to generate the required shapefile, using iloc
df_traffic=pd.DataFrame()
df_traffic['ID']=stations.iloc[5:]['...']
df_traffic['X_coord']=stations.iloc[5:]['...']
df_traffic['Y_coord']=stations.iloc[5:]['...']

#only select usefull rows ('totaal' or with loopidentifiers)
traffic_19=traffic_19[(traffic_19['...']=='Totaal')|(traffic_19['...'].str.contains('Gemiddelde voertuigverdeling per uur'))]
traffic_20=traffic_20[(traffic_20['...']=='Totaal')|(traffic_20['...'].str.contains('Gemiddelde voertuigverdeling per uur'))]

df_values=pd.DataFrame()
df_values['ID']=traffic_19[traffic_19['...'].str.contains('Gemiddelde voertuigverdeling per uur')]['...'].str.split('(',n=1,expand=True)[1].str.split(')',n=1,expand=True)[0]

#add total vehicles
df_values['vehicles_2019']=traffic_19['...'].loc[df_values.index+26].values
df_values['vehicles_2020']=traffic_20['...'].loc[df_values.index+26].values

#merge dataframes
df_traffic=df_traffic.merge(df_values)


# Step 2: Now export the df into a CSV file.
