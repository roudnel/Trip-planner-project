from Interface import Interface_Saisie
from BestMonth import insert_city, extract
from BestCities import insert_month
from Interface_nocity import city_choice
from Interface_nomonth import month_choice
from Place2visit import best_places
from Restaurants import search_restaurant
from Temp import extract_temp
import pandas as pd


result = Interface_Saisie()
city = str(result[0])
month = str(result[1])


if city == '' and month!='':
    cities = insert_month(month)
    city = city_choice(cities)[0]
    best_place = best_places(city)
    resto=search_restaurant(city)
    temp = extract_temp(city)[month]
 
elif month == '' and city!='':
    bs = insert_city(city)
    dict_meteo = extract(bs)
    month = month_choice(dict_meteo)
    best_place = best_places(city)
    resto=search_restaurant(city)
    temp = extract_temp(city)[month[0]]
    
else :
    best_place = best_places(city)
    resto=search_restaurant(city)
    temp = extract_temp(city)[month]
     
data_dict={ 
           'Lieux à visiter': best_place,
           'Restaurant':resto
            }
    # Create a Pandas dataframe from the data.
df = pd.DataFrame.from_dict(data_dict)


df.to_csv('/Users/hugol/Advanced Programming/T2/trip_ planner.csv',index=False)
df2 = pd.read_csv('/Users/hugol/Advanced Programming/T2/trip_ planner.csv')

recap = "A "+ city +" en "+ month +" il fait environ "+ temp
with open(r'liste.txt', 'w') as fp:
    fp.write(recap)