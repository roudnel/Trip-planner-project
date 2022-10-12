#### Fonction best month to go ###

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def insert_city(city): 
    path = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(path)
    url = 'https://www.ou-et-quand.net/partir/quand/'
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "sd-cmp-1pO44").click()
    driver.find_element(By.ID, 'villepays').send_keys(city)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'submit').click()
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    driver.close()
    return bs

def extract(bs):
    lst_month = []
    lst_situation = []
 
    for i in range(12):
        positif = bs.find_all('b', class_='uppercase_big')[i]
        lst_month.append(positif.string)
    for i in range(1,13):
        fav = bs.find_all(class_='hidden-xs nopaddingleft')[i]
        lst_situation.append(fav.get_text())
    dict_meteo = dict(zip(lst_month, lst_situation))
    return dict_meteo
