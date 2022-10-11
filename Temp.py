from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

def extract_temp(city):
    path= os.getcwd() + '/chromedriver'
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
    lst_month = []
    lst_temp = []
    for i in range(12):
        positif = bs.find_all('b', class_='uppercase_big')[i]
        lst_month.append(positif.string)
    for i in range(1,13):
        temp = driver.find_element_by_xpath('//*[@id="contenu_page"]/section[2]/div[2]/table/tbody/tr['+str(i)+']/td[3]').text
        lst_temp.append(temp)
        dict_temp = dict(zip(lst_month, lst_temp))
    driver.close()
    return dict_temp
