# -*- Coding: utf-8 -*-
# Authors: angelasu@stud.ntnu.no, rahulse@stud.ntnu.no
# Date: 2022.12.02

# %%
# * 1. Import packages
import pandas as pd
from pathlib import Path

# %%
# * 2. Define paths
directory_path = Path("../")
wpp_path = Path(
    directory_path
    / "data"
    / "raw"
    / "un"
    / "WPP2022_Demographic_Indicators_Medium"
)

# %%
# * 3. Import un wpp dataset csv file
wpp_df = pd.read_csv(
    wpp_path / "WPP2022_Demographic_Indicators_Medium.csv",
    sep=',',
)
# Rename columns to make coherent datasets
wpp_df = wpp_df.rename(columns={
    "ISO3_code": "Country code",
    "TPopulation1Jan": "Population in 1000s"},
)
wpp_df.head()

# %%
# * 4. Clean wpp dataframe to extract data only for year 2019
# * and only for 'Area type = Country'
population_2019 = wpp_df.loc[
    (wpp_df["Time"] == 2019)
    & (wpp_df["LocTypeName"] == "Country/Area")
]
population_2019.head()

# %%
# * 5. Clean file with required columns only for further processing
# Setting index to country code
# Sorting index in ascending order to match other datasets
population_cleaned = population_2019[
    ["Country code", "Population in 1000s"]
    ].set_index("Country code").sort_index(ascending=True)
population_cleaned.head()

# %%
# * 6. Export to csv
population_cleaned.to_csv(
    directory_path
    / "data"
    / "interim"
    / "un"
    / "WPP2022_Demographic_Indicators_Medium"
    / "Population_cleaned_2019.csv"
)

# Finished cleaning un dataset and created a clean dataset

# %%
