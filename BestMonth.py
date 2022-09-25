#### Fonction best month to go ###

from bs4 import BeautifulSoup
from selenium import webdriver
import time  

def insert_city(city): 
    path= '/Users/hugol/chromedriver'
    driver = webdriver.Chrome(path)
    url = 'https://www.ou-et-quand.net/partir/quand/'
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("sd-cmp-1pO44").click()
    driver.find_element_by_id('villepays').send_keys(city)
    time.sleep(1)
    driver.find_element_by_class_name('submit').click()
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    driver.close()
    return bs

def extract(bs):
    lst_month = []
    lst_situation = []
    lst_met_danger = []
    lst_met_warning = []
    lst_met_success = []
    for i in range(12):
        positif = bs.find_all('b', class_='uppercase_big')[i]
        lst_month.append(positif.string)
    for i in range(1,13):
        fav = bs.find_all(class_='hidden-xs nopaddingleft')[i]
        lst_situation.append(fav.get_text())
        
    #récupération météo en rouges
    for i in bs.find_all('tr', class_='danger-full'):
        for j in range (1,2):
            aj=i.find_all('b')[j]
            lst_met_danger.append(aj.get_text())
            
    #récupération météo en jaune
    for i in bs.find_all('tr', class_='warning'):
        for j in range (1,2):
            aj=i.find_all('b')[j]
            lst_met_warning.append(aj.get_text())
            
    #récupération météo en vert
    for i in bs.find_all('tr', class_='success'):
        for j in range (1,2):
            aj=i.find_all('b')[j]
            lst_met_success.append(aj.get_text())

    dict_meteo = dict(zip(lst_month, lst_situation))
    return dict_meteo , lst_met_success , lst_met_warning ,lst_met_danger

