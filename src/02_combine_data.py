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
# * 1. Import emissions data
directory_path = Path("../") #Defines directory path
emissions_path = Path( 
    directory_path 
    / "data" 
    / "processed" 
) #Defines dataset path
emissions_df = pd.read_csv( 
    emissions_path / "Ember_emissions.csv",
    sep=',',
) #Imports csv file from the folder
display(emissions_df) #Display the file

# %%
# * 2. Import population data
population_path = Path( 
    directory_path 
    / "data" 
    / "processed" 
) #Defines dataset path
population_df = pd.read_csv( 
    population_path / "Population_export.csv",
    sep=',',
) #Imports csv file from the folder
display(population_df) #Display the file

# %%
# * 3. Merge emissions and population
merged_emmissions_population = pd.merge(emissions_df, population_df, 
                   on = "Country code", 
                   how = "inner")
display(merged_emmissions_population)

# %%
# * 4. Add column for emissions per capita
merged_emmissions_population["Emissions per capita in tCO2"] = (merged_emmissions_population["Value"] * 10**6) / (merged_emmissions_population["TPopulation1Jan"] * 10**3)
display(merged_emmissions_population)

# %%
# * 5. Load clean energy file
clean_energy_path = Path( 
    directory_path 
    / "data" 
    / "processed" 
) 

clean_energy_df = pd.read_csv( 
    clean_energy_path / "Ember_clean.csv",
    sep=',',
) 

display(clean_energy_df)

#%%
# * 6. Merge clean energy file with above merged file
all_merged = pd.merge(merged_emmissions_population, clean_energy_df,
                    on = "Country code",
                    how = "inner")
display(all_merged)

#%%
# * 7. Plot all merged data
fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
z = np.array(all_merged['TPopulation1Jan']/1000)
ax.scatter(all_merged['Value_y'], all_merged["Emissions per capita in tCO2"], s=z, marker = "o", alpha = 0.7)
ax.set_xlabel("Clean Energy in %")
ax.set_ylabel("Emmission in tCO2 per capita")
ax.set_title("Clean energy vs emissions per capita")
plt.show()

#%%
# * 8. Annotate the countries with higher population
#WIP
#...


# %%
# * 9. Save file into png format
fig.savefig("Clean energy vs emissions per capita.png" , dpi = 300)