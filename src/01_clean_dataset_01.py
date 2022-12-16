# -*- Coding: utf-8 -*-
# Authors: angelasu@stud.ntnu.no, rahulse@stud.ntnu.no
# Date: 2022.10.30

# %%
# * Import packages
import numpy as np
import pandas as pd
from pathlib import Path
import os
import matplotlib.pyplot as plt

# %%
# * 1. Import dataset_01
directory_path = Path("../") #Defines directory path
dataset_01_path = Path( 
    directory_path 
    / "data" 
    / "raw" 
    / "ember_electricity_data"
) #Defines dataset path
ember_df = pd.read_csv( 
    dataset_01_path / "ember_yearly_data.csv",
    sep=',',
) #Imports csv file from the folder
display(ember_df) #Display the file

#%%
# * 2. Clean ember_df to extract data only for year 2019 and only for countries
ember_2019 = ember_df.loc[(ember_df["Year"] == 2019) & (ember_df["Area type"] == "Country")]
display(ember_2019)

#%%
# * 3. Clean ember_2019 to subset data for clean energy percentage
ember_2019_clean = ember_2019.loc[
    (ember_2019["Category"] == "Electricity generation") 
    & (ember_2019["Subcategory"] == "Aggregate fuel") 
    & (ember_2019["Variable"] == "Clean") 
    & (ember_2019["Unit"] == "%")]
display(ember_2019_clean)

#%%
# * 4. Clean ember_2019 to subset data for emissions from power sector
ember_2019_emissions = ember_2019.loc[
    (ember_2019["Category"] == "Power sector emissions") 
    & (ember_2019["Subcategory"] == "Total")
    & (ember_2019["Variable"] == "Total emissions")
    & (ember_2019["Unit"] == "mtCO2")]
display(ember_2019_emissions)

# %%
# * 5. Prepare to export cleaned file with required columns only for further processing
# - (WIP) and set index to country name and rename "Area" column to "Country"
ember_clean = ember_2019_clean[["Area", "Country code", "Category", "Subcategory", "Variable", "Unit", "Value"]]
display(ember_clean)

#%%
#ember_clean_export = ember_clean.set_index("Area")
#display(ember_clean_export)

#%%
ember_emissions = ember_2019_emissions[["Area", "Country code", "Category", "Subcategory", "Variable", "Unit", "Value"]]
display(ember_emissions)

#%%
# * 6. Export both files separately to csv format 
# + Why separate files? 
# = 1. Clean energy file will be processed directly 
# = 2. Emissions file will be merged with population file to calculate emissions per capita
ember_clean.to_csv(directory_path / "data"/ "processed"/ "Ember_clean.csv") #To save the file as csv
ember_emissions.to_csv(directory_path / "data"/ "processed"/ "Ember_emissions.csv") #To save the file as csv

# * 7. Finished cleaning first dataset and created two new clean datasets