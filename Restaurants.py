from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

def search_restaurant(city):
    
    website = 'https://www.tripadvisor.fr/Restaurants'
    path = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(path)
    driver.get(website)
    restaurants=[]
    time.sleep(5)
    driver.find_element("id","onetrust-reject-all-handler").click()
    
    time.sleep(5)
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').click()
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').send_keys(city)
    time.sleep(5)
    driver.find_element("xpath",'//*[@id="typeahead_results"]/a[1]').click()
    time.sleep(5)
    html=driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    List_of_rest=bs.find_all('a', class_='oHGMl')
    for j in range (0,10):
        restaurants.append(List_of_rest[j].text)
    driver.close()
    return restaurants
