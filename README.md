# Sharing Project Code:  Environmental Kuznets Curve
## Key idea: IS THE ENVIRONMENTAL KUZNETS CURVE STILL ACCURATE? Using evidence from PM2.5 Concentration Data and indicators of development. 

# Instructions for our group
- When you commit changes : message the group chat 
- once a new coding file is uploaded : add the name of the file in the table of contents under the current subheading

# Table of contents
1. [Introduction](#introduction)
2. [Data used](#paragraph1)
    1. [World Health Organisation API](#subparagraph1)
    2. [World Bank CSV dataset](#subparagraph2) 
3. [Data visualisation](#paragraph2)
4. [Collobarators](#paragraph3)

## Introduction - our project and our motivation <a name="introduction"></a>
During the last few years, there’s been a growing concern on the industrialisation of less developed countries and its impact on climate change as growing industrialisations remains synonymous with growing emissions in a world where we can not afford that. By looking at the accuracy of the environmental kuznet’s curve, we will be able to prove whether policies, aimed at flattening this curve, are useful and accurate. And this is what made us interested in this data. 

Our goal is to use the World Bank’s API to retrieve PM2.5 data (particulate matter) and clean IMF data for development indicators to test the validity of the Kuznets curve. Our Hypothesis is that PM2.5 concentration levels peak during the industrialization stage of development - characterized as fast-growing economies, increasing female participation rate, expanding urban population
In turn, this has implications on policy: maybe focusing on “flattening” the Kuznets curve could be a viable emission-reduction target for the medium-term?

## Data used <a name="paragraph1"></a>
Two datasets: World Health Organisation API from the global health observatory and a CSV datasets for development indicators from the World Bank particularly on Health, Nutrition and Population Statistics

### World Health Organisation API <a name="subparagraph1"></a>
Pollution indicator: SDGPM25  (Particulate matter (PM) is everything in the air that is not a gas and therefore consists of a huge variety of chemical compounds and materials, some of which can be toxic, The Air Quality Standards Regulations 2010 require that concentrations of PM in the UK must not exceed: An annual average of 20 µg/m3 for PM2.5)
Every country w/ 10 years of data (2010-2019)
Air Pollution levels in 5 categories (DIM1) (Total, City, Rural, Town, Urban)

[Code for PM2.5](https://github.com/neocommits/environmentalkuznets/blob/8d320777d10cfe5cc6c4a601a26e706a416b5718/API%20code%20and%20csv%20file/PM25.py)

[CSV file for PM2.5](https://github.com/neocommits/environmentalkuznets/blob/11c950810089379519de1a039b15b76a8f58afd3/API%20code%20and%20csv%20file/PM25_data.csv)

### World Bank CSV dataset <a name="subparagraph2"></a>

Measuring development through 9 indicators:
- % urban population (development stage)
- School enrollment 
- Rural population  (development stage)
- Public spending on education +
- Population total  (dev stage)
- Population growth (dev stage)
- Life expectancy +
- Female labour force +
- GNI per capita +
- % Manufacturing sector in GDP
- GDP growth (%)

[Original excel file (unclean)](..Indicators csv cleaning and final dataframe/indicators_unclean.xlsx)

[Clean Data](Indicators csv cleaning and final dataframe/indicators_unclean.xlsx)

[Code to clean data](https://github.com/neocommits/environmentalkuznets/blob/e51ec8c181716de6e131260745501ded40ae3c37/Indicators%20csv%20cleaning%20and%20final%20dataframe/Indicators_data_cleaning.ipynb)

### Merging Data

[merging data code](https://github.com/neocommits/environmentalkuznets/blob/e51ec8c181716de6e131260745501ded40ae3c37/Indicators%20csv%20cleaning%20and%20final%20dataframe/Final_data_merging.ipynb)

[final merged dataframe](https://github.com/neocommits/environmentalkuznets/blob/e51ec8c181716de6e131260745501ded40ae3c37/Indicators%20csv%20cleaning%20and%20final%20dataframe/final_dataframe.csv)


## Data visualisation <a name="paragraph2"></a>

## Collobarators  <a name="paragraph3"></a>
Ines McCairley

Adrien Joly

Hassam Zahid

Sara Tiron

