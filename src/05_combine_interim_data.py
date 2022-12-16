# -*- Coding: utf-8 -*-
# Authors: angelasu@stud.ntnu.no, rahulse@stud.ntnu.no
# Date: 2022.12.02

# %%
# * 1. Import packages
import numpy as np
import pandas as pd
from pathlib import Path
import geopandas as gpd

# %%
# * 2. Define paths
directory_path = Path("../")

ember_dataset_path = Path(
    directory_path
    / "data"
    / "interim"
    / "ember"
    / "Yearly electricity data"
)

un_dataset_path = Path(
    directory_path
    / "data"
    / "interim"
    / "un"
    / "WPP2022_Demographic_Indicators_Medium"
)

wb_dataset_path = Path(
    directory_path
    / "data"
    / "interim"
    / "world bank"
    / "World Development Indicators"
)

naturalearth_dataset_path = Path(
    directory_path
    / "data"
    / "interim"
    / "natural earth"
    / "large scale"
)

# %%
# * 3. Import all interim datasets
ember_df = pd.read_csv(
    ember_dataset_path
    / "Ember_cleaned_2019.csv",
    sep=',',
)

population_df = pd.read_csv(
    un_dataset_path
    / "Population_cleaned_2019.csv",
    sep=',',
)

wdi_df = pd.read_csv(
    wb_dataset_path
    / "WDI_cleaned.csv",
    sep=',',
)

naturalearth_df = gpd.read_file(
    naturalearth_dataset_path
    / "naturalearth_cleaned.geojson",
    sep=',',
)

# %%
# * 4. Merge all dataframes
# 4.1. Merge ember and population
ember_pop_merged = pd.merge(
    ember_df, population_df,
    on="Country code",
    how="inner"
)
ember_pop_merged.head()

# %%
# 4.2. Merge above and wdi
ember_pop_wdi_merged = pd.merge(
    ember_pop_merged, wdi_df,
    on="Country code",
    how="inner"
)
ember_pop_wdi_merged.head()

# %%
# 4.3. Merge above and naturalearth and setting index to country code
all_merged = naturalearth_df.merge(
    ember_pop_wdi_merged,
    on="Country code",
    how="inner"
).set_index("Country code")
all_merged.head()

# %%
# * 5. Add column for emissions per capita
all_merged["Emissions per capita in tCO2"] = \
    all_merged["Total emissions from power sector (mtCO2)"] * 10**3 \
    / all_merged["Population in 1000s"]
all_merged.head()

# %%
# * 6. Add column for percent of total population
total_world_population = all_merged["Population in 1000s"].sum()
all_merged["Percent of total population"] = \
    all_merged["Population in 1000s"] * 100 \
    / total_world_population
all_merged.head()

# %%
# * 7. Add column for percent of total emissions
total_world_emission = \
    all_merged["Total emissions from power sector (mtCO2)"].sum()
all_merged["Percent of total emissions"] = \
    all_merged["Total emissions from power sector (mtCO2)"] * 100 \
    / total_world_emission
all_merged.head()

# %%
# * 8. Check which countries over-emit and under-emit
conditions = [
    (all_merged["Percent of total emissions"]
     > all_merged["Percent of total population"]),
    (all_merged["Percent of total emissions"]
     < all_merged["Percent of total population"])
]
value = ["over-emit", "under-emit"]
# Add new column with this data
all_merged["Equity"] = np.select(conditions, value)
all_merged.head()

# %%
# * 9. Export file for geospatial plot
processed_gdf = gpd.GeoDataFrame(all_merged)
type(processed_gdf)
processed_gdf = processed_gdf.set_geometry(col="geometry")
processed_gdf.to_file(
    directory_path
    / "data"
    / "processed"
    / "processed_gdf.geojson",
    driver='GeoJSON'
)
# %%
