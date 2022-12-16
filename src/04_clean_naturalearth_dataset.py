# -*- Coding: utf-8 -*-
# Authors: angelasu@stud.ntnu.no, rahulse@stud.ntnu.no
# Date: 2022.12.02

# %%
# * 1. Import packages
from pathlib import Path
import geopandas as gpd

# %%
# * 2. Define paths
directory_path = Path("../")
naturalearth_path = Path(
    directory_path
    / "data"
    / "raw"
    / "natural earth"
    / "large scale"
)

# %%
# * 3. Import natural earth dataset json file
naturalearth_df = gpd.read_file(
    naturalearth_path
    / "world_data.geo.json"
)
# Rename columns to make coherent datasets
naturalearth_df = naturalearth_df.rename(
    columns={"iso_a3_eh": "Country code"}
)
naturalearth_df.head()

# %%
# * 4. Clean natural earth dataframe to extract data only for geometry
# * Setting index to country code
# * Sorting index in ascending order to match other datasets
naturalearth_cleaned = naturalearth_df[
    ["Country code", "geometry"]
    ].set_index("Country code").sort_index(ascending=True)
naturalearth_cleaned.head()

# %%
# * 5. Check if all countries are visible in the plot
naturalearth_cleaned.plot()
type(naturalearth_cleaned)

# %%
# * 6. Export geodataframe
naturalearth_cleaned.to_file(
    directory_path
    / "data"
    / "interim"
    / "natural earth"
    / "large scale"
    / "naturalearth_cleaned.geojson",
    driver='GeoJSON'
)

# Finished cleaning dataset
# %%
