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

#%%
# * 1. Import dataset_02
directory_path = Path("../") #Defines path
dataset_02_path = Path(
    directory_path 
    / "data" 
    / "raw" 
    / "un_population_data"
)
population_df = pd.read_csv( 
    dataset_02_path / "population_data.csv",
    sep=',',
) #Imports csv file from the folder
display(population_df)
population_df.rename(columns = {'ISO3_code':'Country code', 'Location':'Area'}, inplace = True)
display(population_df)

#%%
# * 2. Clean dataset_02 to extract data only for year 2019 and only for countries
population_2019 = population_df.loc[(population_df["Time"] == 2019) & (population_df["LocTypeName"] == "Country/Area")]
display(population_2019)

# %% 
# * 3. Prepare to export cleaned file with required columns only for further processing
population_cleaned = population_2019[["Country code", "Area", "TPopulation1Jan"]]
display(population_cleaned)

#%%
# * 4. Setting index to Country in ascending order to match with other datasets
population_export = population_cleaned.set_index("Area").sort_index(ascending = True)
display(population_export)

#%%
# * 4. Export to csv
population_export.to_csv(directory_path / "data"/ "processed"/ "Population_export.csv")

# * 5. Finished cleaning second dataset
# %%
