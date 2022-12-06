import requests
import pandas as pd
import numpy as np

#Using list comprehension tool and vectorised operations, a lot simpler to change to other town,urban etc, just change the + 1 index in the rjson value if we wanted in the future
#Used the filtered API now

rjson_2 = requests.get("https://ghoapi.azureedge.net/api/SDGPM25?$filter=Dim1%20eq%20%27TOTL%27").json()

def avg_for_each_country():
    total_list_of_avg_2010_to_2019 = [np.round(np.mean([rjson_2["value"][(i * 10) + current_year]["NumericValue"] for current_year in range(10)]), decimals = 5) for i in range(189)]
    print(total_list_of_avg_2010_to_2019)
    return(total_list_of_avg_2010_to_2019)
total_list_of_avg_2010_to_2019 = avg_for_each_country()

#9,450 data points for 189 countries. 9450/189=50. 50 data points per country / 5 locations per country = 10 years per country. Therefore no missing data.
#nvm, there are 195 countries

def total_each_year():
    total_list_of_each_year = [[rjson_2["value"][(i * 10) + current_year]["NumericValue"] for i in range(195)] for current_year in range(10)]
    return(total_list_of_each_year)
total_list_of_each_year = total_each_year()

def listing_countries():
    country_list = [(rjson_2["value"][i * 10]["SpatialDim"]) for i in range(195)]
    return(country_list)
country_list = listing_countries()

dict = {"Country:": country_list, "2010 Total:": total_list_of_each_year[0], "2011 Total:": total_list_of_each_year[1], "2012 Total:": total_list_of_each_year[2], "2013 Total:": total_list_of_each_year[3], "2014 Total:": total_list_of_each_year[4], "2015 Total:": total_list_of_each_year[5],"2016 Total:": total_list_of_each_year[6], "2017 Total:": total_list_of_each_year[7], "2018 Total:": total_list_of_each_year[8], "2019 Total:": total_list_of_each_year[9]}
df = pd.DataFrame(dict)
df.to_csv('PM25_data.csv')
print(df)