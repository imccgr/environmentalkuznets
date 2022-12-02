import requests
import pandas as pd
import numpy as np
rjson = requests.get("https://ghoapi.azureedge.net/api/SDGPM25").json()

# Using list comprehension tool and vectorised operations, a lot simpler to change to other town,urban etc, just change the + 1 index in the rjson value if we wanted in the future

def listing_countries():
    country_list = [(rjson["value"][(i * 51) - i]["SpatialDim"]) for i in range(189)]
    return(country_list)
country_list = listing_countries()

def total_for_each_country():
    total_list_of_avg_2010_to_2019 = [np.round(np.mean([rjson["value"][((i * 51) - i + 1) + (current_year * 5)]["NumericValue"] for current_year in range(10)]), decimals = 5) for i in range(189)]
    return(total_list_of_avg_2010_to_2019)
total_list_of_avg_2010_to_2019 = total_for_each_country()

def city_for_each_country():
    city_list_of_avg_2010_to_2019 = [np.round(np.mean([rjson["value"][((i * 51) - i) + (current_year * 5)]["NumericValue"] for current_year in range(10)]), decimals = 5) for i in range(189)]
    return(city_list_of_avg_2010_to_2019)
city_list_of_avg_2010_to_2019 = city_for_each_country()

dict = {"Country:": country_list, "City Average PM2.5:": total_list_of_avg_2010_to_2019, "Total Average PM2.5:": city_list_of_avg_2010_to_2019}
df = pd.DataFrame(dict)
df.to_csv('PM25_data_v2.csv')
print(df)