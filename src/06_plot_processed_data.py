# -*- Coding: utf-8 -*-
# Authors: angelasu@stud.ntnu.no, rahulse@stud.ntnu.no
# Date: 2022.12.02

# %%
# * 1. Import packages
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import geopandas as gpd

# %%
# * 2. Define paths
directory_path = Path("../")
processed_dataset_path = Path(
    directory_path
    / "data"
    / "processed"
)
visualisations_path = Path(
    directory_path
    / "visualisations"
)

# %%
# * 3. Import processed dataset
processed_df = gpd.read_file(
    processed_dataset_path
    / "processed_gdf.geojson",
    sep=',',
)
processed_df.head()

# %%
# * 4. Plot % of clean energy and emissions per capita
# To annotate countries emitting more than 7.8 tCO2 per capita
countries = processed_df[processed_df['Emissions per capita in tCO2'] > 7.8]
# To annotate countries with more than 100 million populaion
countries_2 = processed_df[processed_df['Population in 1000s'] > 100000]
# Plot the figure
fig, ax = plt.subplots(figsize=(10, 6))
plt.grid()
ax.set_axisbelow(True)
plot1 = sns.scatterplot(
    data=processed_df,
    x='Percentage of clean energy generated',
    y='Emissions per capita in tCO2',
    hue='Continent',
    size='Population in 1000s',
    alpha=0.7
).set_title(
    "Percentage of clean energy produced by a country \
compared to CO2 emissions per capita"
)
for idx, row in countries.iterrows():
    ax.annotate(
        row["Country"],
        (row["Percentage of clean energy generated"] + 0.5,
         row["Emissions per capita in tCO2"] + 0.05),
        fontsize=5
    )
for idx, row in countries_2.iterrows():
    ax.annotate(
        row["Country"],
        (row["Percentage of clean energy generated"]+0.5,
         row["Emissions per capita in tCO2"]+0.05),
        fontsize=5
    )
ax.legend(fontsize=7)

# Save the plot
fig.savefig(
    visualisations_path
    / "1.Clean energy vs emissions per capita.png",
    dpi=1200
)

# %%
# * 5. Plot percent of total population and emissions
fig, ax = plt.subplots(figsize=(10, 6))
plt.grid()
ax.set(xscale='log', yscale='log')
sns.scatterplot(
    data=processed_df,
    ax=ax,
    x='Percent of total population',
    y='Percent of total emissions',
    hue='Income Group',
    alpha=0.7
).set_title("Countries compared by share of global CO2 emissions")
# Save the plot
fig.savefig(
    visualisations_path
    / "2.Countries compared by share of global CO2 emissions.png",
    dpi=1200
)

# %%
# * 6. Plot over-emitting and under-emitting countries
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_axis_off()
('black')
ax.patch.set_linewidth('1')
processed_df.plot(
    column="Equity",
    ax=ax,
    legend=True,
    legend_kwds={'loc': 'lower left'}
).set_title(
    "Which countries over- and under-emit relative to their population share"
)
# Save the plot
fig.savefig(
    visualisations_path
    / "3.Which countries over- and under-emit.png",
    dpi=1200
)

# %%
