### Fonction best city to go per month
from selenium import webdriver
import os

def insert_month(month):
    ## Choix du mois préféré
    PATH = os.getcwd() + "/chromedriver"
    driver = webdriver.Chrome(PATH)
    month = month.lower()
    if month == "février":
        month = "fevrier"
    elif month == "décembre":
        month = "decembre"
       
    driver.get("https://partir.ouest-france.fr/meteo/oupartiren"+month+".php")
    driver.find_element_by_class_name("didomi-continue-without-agreeing").click()
    ## Decomposition du Xpath en z et e
    z = "//*[@id='middle']/table[3]/tbody/tr[" 
    e = "]/td[1]/a[1]" 
    ## Creation d'une liste de xpath pour les 10 premières villes de la liste
    xpaths=[]
    for i in range(1,11):
        xpath = z+str(i)+e
        xpaths.append(xpath)
        i=+1
    ## Dictionnaire des villes
    villes=[] 
    for i in range(1, len(xpaths)+1):
        xpath=z+str(i)+e
        abc = driver.find_element_by_xpath(xpath)
        ville=abc.text
        villes.append(ville)
    driver.close()
    return villes
