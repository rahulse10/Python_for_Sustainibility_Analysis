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
ember_dataset_path = Path(
    directory_path
    / "data"
    / "raw"
    / "ember"
    / "Yearly electricity data"
)

# %%
# * 3. Import ember_dataset csv file from the folder
ember_df = pd.read_csv(
    ember_dataset_path /
    "yearly_full_release_long_format.csv",
    sep=',',
)
ember_df.head()

# %%
# * 4. Clean ember_df to extract data only for year 2019
# * and only for 'Area type = Country'
# ! The data is not consistent for the recent years due to the pandemic.
# ! So the data was analyzed for 2019.
ember_2019 = ember_df.loc[(ember_df["Year"] == 2019)
                          & (ember_df["Area type"] == "Country")]
ember_2019.head()

# %%
# * 5. Clean ember_2019 to subset data for clean energy percentage
ember_2019_clean = ember_2019.loc[
    (ember_2019["Category"] == "Electricity generation")
    & (ember_2019["Subcategory"] == "Aggregate fuel")
    & (ember_2019["Variable"] == "Clean")
    & (ember_2019["Unit"] == "%")]
ember_2019_clean.head()

# %%
# * 6. Cleaned dataframe with required columns only
# * for further processing
# Area column for country names
# Country code column as common index in all datasets
# Continent names to categorize countries in plots
ember_clean = ember_2019_clean[["Area", "Country code", "Continent", "Value"]]
# Renaming columns for consistency and making sense of 'Value' column
# Same column names will be used in other datasets too
# Setting index to country code
ember_clean = ember_clean.rename(
    columns={"Area": "Country",
             "Value": "Percentage of clean energy generated"}
             ).set_index("Country code")
ember_clean.head()

# %%
# * 7. Clean ember_2019 to subset data for emissions from power sector
ember_2019_emissions = ember_2019.loc[
    (ember_2019["Category"] == "Power sector emissions")
    & (ember_2019["Subcategory"] == "Total")
    & (ember_2019["Variable"] == "Total emissions")
    & (ember_2019["Unit"] == "mtCO2")]
ember_2019_emissions.head()

# %%
# * 8. Cleaned dataframe with required columns only
# * for further processing
ember_emissions = ember_2019_emissions[["Area", "Country code", "Value"]]
# Renaming columns for consistency and making sense of 'Value' column
# Setting index to country code
ember_emissions = ember_emissions.rename(
    columns={"Area": "Country",
             "Value": "Total emissions from power sector (mtCO2)"}
             ).set_index("Country code")
ember_emissions.head()

# %%
# * 9. Merge two dataframes
ember_merged_2019 = pd.merge(
    ember_clean, ember_emissions,
    on=["Country code", "Country"])
ember_merged_2019.head()

# %%
# * 10. Export cleaned file to csv format
ember_merged_2019.to_csv(
    directory_path
    / "data"
    / "interim"
    / "ember"
    / "Yearly electricity data"
    / "Ember_cleaned_2019.csv"
)

# Finished cleaning ember dataset and created a clean dataset

# %%
