import requests
import pandas as pd

rjson_2 = requests.get("https://ghoapi.azureedge.net/api/SDGPM25?$filter=Dim1%20eq%20%27TOTL%27").json()

def total_each_year():
    total_list_of_each_year = [[rjson_2["value"][(i * 10) + current_year]["NumericValue"]
                                for i in range(195)] for current_year in range(10)]
    return(total_list_of_each_year)
total_list_of_each_year = total_each_year()

def listing_countries():
    country_list = [(rjson_2["value"][i * 10]["SpatialDim"]) for i in range(195)]
    return(country_list)
country_list = listing_countries()

dict = {"Country:": country_list, "2010 Total:": total_list_of_each_year[0], "2011 Total:": total_list_of_each_year[1],
        "2012 Total:": total_list_of_each_year[2], "2013 Total:": total_list_of_each_year[3],
        "2014 Total:": total_list_of_each_year[4], "2015 Total:": total_list_of_each_year[5],
        "2016 Total:": total_list_of_each_year[6], "2017 Total:": total_list_of_each_year[7],
        "2018 Total:": total_list_of_each_year[8], "2019 Total:": total_list_of_each_year[9]}
df = pd.DataFrame(dict)
df.to_csv('PM25_data.csv')
print(df)
