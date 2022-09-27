from Interface import Interface_Saisie
from BestMonth import insert_city, extract
from BestCities import insert_month
from Interface_nocity import city_choice
from Interface_nomonth import month_choice
from Place2visit import best_places
from restaurant import search_restaurant
from Error import error



result = Interface_Saisie()
city = str(result[0])
month = str(result[1])

if city == '' and month == '':
    while city == '' and month == '':
        error()
        result = Interface_Saisie()
        city = str(result[0])
        month = str(result[1])

elif city == '':
    cities = insert_month(month)
    city = city_choice(cities)[0]
    best_place = best_places(city)
    print(city)
    print(month)
    print(best_place)
    
elif month == '':
    bs = insert_city(city)
    dict_meteo = extract(bs)
    month2 = month_choice(dict_meteo)
    best_place = best_places(city)
    print(city)
    print(month2)
    print(best_place)
    
else :
    best_place = best_places(city)
    print(city)
    print(month)
    print(best_place)
