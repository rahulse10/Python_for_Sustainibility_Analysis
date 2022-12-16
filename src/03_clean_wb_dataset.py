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
wdi_path = Path(
    directory_path
    / "data"
    / "raw"
    / "world bank"
    / "World Development Indicators"
)

# %%
# * 3. Import world bank wdi dataset csv file
wdi_df = pd.read_csv(
    wdi_path / "WDICountry.csv",
    sep=',',
)
# Rename columns to make coherent datasets
wdi_df = wdi_df.rename(columns={"Country Code": "Country code"})
wdi_df.head()

# %%
# * 4. Clean wdi dataframe to extract data only for income groups
# Setting index to country code
# Sorting index in ascending order to match other datasets
wdi_cleaned = wdi_df[[
    "Country code",
    "Income Group"]].set_index("Country code").sort_index(ascending=True)
wdi_cleaned.head()

# %%
# * 5. Export to csv
wdi_cleaned.to_csv(
    directory_path
    / "data"
    / "interim"
    / "world bank"
    / "World Development Indicators"
    / "WDI_cleaned.csv"
)

# Finished cleaning the dataset
# %%
