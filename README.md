# Project: Identifying countries that need to focus on reducing their CO2 emissions
## TEP4221 - Python for Sustainability Analysis
Date: August 2022 - December 2022

Contributors:
Angela Subedi, angelasu@stud.ntnu.no
Rahul Sehgal, rahulse@stud.ntnu.no

Keywords: renewable energy; CO2 emissions; population demographics; environment
Relevant SDGs:
SDG 7: Affordable and clean energy
SDG 9: Industry, innovation and infrastructure
SDG 13: Climate action 

## Project overview
```
PROJECT
│   env.yml
│   README.md
│
├───data
│   ├───interim
│   │   ├───ember
│   │   │   └───Yearly electricity data
│   │   │           Ember_cleaned_2019.csv
│   │   │
│   │   ├───natural earth
│   │   │   └───large scale
│   │   │           naturalearth_cleaned.geojson
│   │   │
│   │   ├───un
│   │   │   └───WPP2022_Demographic_Indicators_Medium
│   │   │           Population_cleaned_2019.csv
│   │   │
│   │   └───world bank
│   │       └───World Development Indicators
│   │               WDI_cleaned.csv
│   │
│   ├───processed
│   │       processed_gdf.geojson
│   │
│   └───raw
│       ├───ember
│       │   └───Yearly electricity data
│       │           yearly_full_release_long_format.csv
│       │
│       ├───natural earth
│       │   └───large scale
│       │           world_data.geo.json
│       │
│       ├───un
│       │   └───WPP2022_Demographic_Indicators_Medium
│       │           WPP2022_Demographic_Indicators_Medium.csv
│       │
│       └───world bank
│           └───World Development Indicators
│                   WDICountry.csv
│
├───docs
│       2022.11.15. Python presentation.pdf
│       Ember-Electricity-Data-Methodology.pdf
│       readme for info.txt
│       WPP2022_Data_Sources.pdf
│
├───src
│       01_clean_ember_dataset.py
│       02_clean_un_dataset.py
│       03_clean_wb_dataset.py
│       04_clean_naturalearth_dataset.py
│       05_combine_interim_data.py
│       06_plot_processed_data.py
│
└───visualisations
        1.Clean energy vs emissions per capita.png
        2.Countries compared by share of global CO2 emissions.png
        3.Which countries over- and under-emit.png
```

## Introduction
---
This project is to analyze the relationship between percentage of clean energy generated and CO2 emmissions per capita from power sector of different countries. The aim of the project is to visualize differences in CO2 emissions depending on income groups of the countries. This analysis helps to figure out which countries are contributing to higher CO2 emissions per capita and which countries are currently producing more clean energy than others. The data visualization helps to investigate if high income countries have direct link to higher CO2 emissions. The project relates to sustainability since burning of fossil fuel is one of the main contributors to climate change. The developed countries are emitting more CO2 and contributing to climate change while the repurcussions are faced by the poorer countries. Thus, it helps us identify which nations need to work on reducing their CO2 emissions.

## Research questions
---
1. Which countries need to invest more in renewable energy and control the use of non-renewable sources and CO2 emissions?
2. How does difference in income of countries relate to CO2 emissions?
3. Which countries over- and under-emit relative to their gloabl population share.
 
## Datasets
---
1. Ember Yearly electricity data 
(Source: https://ember-climate.org/data-catalogue/yearly-electricity-data/)
(Version: Last updated on 2 November 2022)
(Used for: Clean energy percentage and total emissions in mtCO2 (for the year 2019) of all countries)

2. UN WPP data 
(Source: https://population.un.org/wpp/Download/Standard/CSV/) 
(Version: Subgroup - Demographic Indicators)
(Used for: Population of the world)

3. Natural earth data 
(Source: https://www.naturalearthdata.com/downloads/)
(Version: Large scale data)
(Used for: Geospatial data)

4. World bank data - World Development Indicators
(Source: https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators)
(Version: Last updated on Sep 16, 2022)
(Used for: Income groups of countries)

## Challenges
---
1. The data for CO2 emissions (in ember dataset) was not consistent for the recent years (i.e. 2020, 2021) due to the pandemic. So the data was analyzed for 2019.
2. It was not straightforward to merge different datasets by country names as they were not consistent in 4 different datasets. 
3. It was challenging to annotate the most dominant countries within the plots.
4. Deciding how to visualize in a way that few plots convey clear and comprehensive information was a bit challenging in the beginning.

## Visualisations
---
1. Countries compared by % of clean energy produced vs CO2 emissions per capita by the power sector
![Alt text](https://github.com/rahulse10/Python_for_Sustainibility_Analysis/blob/main/visualisations/1.Clean%20energy%20vs%20emissions%20per%20capita.png)

2. Countries compared by % of total emissions vs % of total population (Grouped by Income level)
![Alt text](https://github.com/rahulse10/Python_for_Sustainibility_Analysis/blob/main/visualisations/2.Countries%20compared%20by%20share%20of%20global%20CO2%20emissions.png)

3. Which countries over- and under-emit relative to their population share
![Alt text](https://github.com/rahulse10/Python_for_Sustainibility_Analysis/blob/main/visualisations/3.Which%20countries%20over-%20and%20under-emit.png)

## Conclusion
---
1. RQ1 - The middle eastern countries (Qatar, Bahrain, Kuwait) have the highest CO2 emmisions per capita from the power sector and lowest percentage production of renewable energy. Within countries having high population, USA, China, Japan and Russia emit the most CO2.
2. RQ2 - From the analysis, it was found that CO2 emmisions per capita and income group of countries have a direct link, with emissions increasing as the income increases in most countries. 
3. RQ3 - Within the group of high income countries, its just the Western European countries that are emitting less than their population share, while rest of the global north has higher emissions than their share of world population.
