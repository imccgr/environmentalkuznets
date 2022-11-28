import requests
import pandas as pd

#NOTE there are 189 total countries in the API

response = requests.get("https://ghoapi.azureedge.net/api/SDGPM25")
rjson = response.json()

def listing_countries():
    country_list = []
    for i, t in zip(range(189), range(189)):
        country_list.append(rjson["value"][(i*51)-t]["SpatialDim"])
    print(country_list)
    print(len(country_list))
    return(country_list)
country_list = listing_countries()

def total_for_each_country():
    total_list_of_avg_2010_to_2019 = []
    for i, t in zip(range(189), range(189)):
        value_2010 = rjson["value"][(i * 51) - t + 1]["NumericValue"]
        value_2011 = rjson["value"][((i * 51) - t + 1) + 5]["NumericValue"]
        value_2012 = rjson["value"][((i * 51) - t + 1) + 10]["NumericValue"]
        value_2013 = rjson["value"][((i * 51) - t + 1) + 15]["NumericValue"]
        value_2014 = rjson["value"][((i * 51) - t + 1) + 25]["NumericValue"]
        value_2015 = rjson["value"][((i * 51) - t + 1) + 30]["NumericValue"]
        value_2016 = rjson["value"][((i * 51) - t + 1) + 35]["NumericValue"]
        value_2017 = rjson["value"][((i * 51) - t + 1) + 40]["NumericValue"]
        value_2018 = rjson["value"][((i * 51) - t + 1) + 45]["NumericValue"]
        value_2019 = rjson["value"][((i * 51) - t + 1) + 50]["NumericValue"]
        average_per_country = round(((value_2010 + value_2011 + value_2012 + value_2013 + value_2014 + value_2015 + value_2016 + value_2017 + value_2018 + value_2019) / 10), 5)
        total_list_of_avg_2010_to_2019.append(average_per_country)
    print(total_list_of_avg_2010_to_2019)
    print(len(total_list_of_avg_2010_to_2019))
    return(total_list_of_avg_2010_to_2019)
total_list_of_avg_2010_to_2019 = total_for_each_country()

def city_for_each_country():
    city_list_of_avg_2010_to_2019 = []
    for i, t in zip(range(189), range(189)):
        value_2010 = rjson["value"][(i * 51) - t]["NumericValue"]
        value_2011 = rjson["value"][((i * 51) - t) + 5]["NumericValue"]
        value_2012 = rjson["value"][((i * 51) - t) + 10]["NumericValue"]
        value_2013 = rjson["value"][((i * 51) - t) + 15]["NumericValue"]
        value_2014 = rjson["value"][((i * 51) - t) + 25]["NumericValue"]
        value_2015 = rjson["value"][((i * 51) - t) + 30]["NumericValue"]
        value_2016 = rjson["value"][((i * 51) - t) + 35]["NumericValue"]
        value_2017 = rjson["value"][((i * 51) - t) + 40]["NumericValue"]
        value_2018 = rjson["value"][((i * 51) - t) + 45]["NumericValue"]
        value_2019 = rjson["value"][((i * 51) - t) + 50]["NumericValue"]
        average_per_country = round(((value_2010 + value_2011 + value_2012 + value_2013 + value_2014 + value_2015 + value_2016 + value_2017 + value_2018 + value_2019) / 10), 5)
        city_list_of_avg_2010_to_2019.append(average_per_country)
    print(city_list_of_avg_2010_to_2019)
    print(len(city_list_of_avg_2010_to_2019))
    return(city_list_of_avg_2010_to_2019)
city_list_of_avg_2010_to_2019 = city_for_each_country()

listing_countries()
total_for_each_country()
city_for_each_country()

dict = {"Country:": country_list, "City Average:": total_list_of_avg_2010_to_2019, "Total Average:": city_list_of_avg_2010_to_2019}
df = pd.DataFrame(dict)
df.to_csv('PM25_data.csv')
print(df)