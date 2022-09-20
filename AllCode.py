#### Fonction best month to go ###

from bs4 import BeautifulSoup
from selenium import webdriver
import time  
import pandas as pd 

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
    for i in range(12):
        positif = bs.find_all('b', class_='uppercase_big')[i]
        lst_month.append(positif.string)
    for i in range(1,13):
        fav = bs.find_all(class_='hidden-xs nopaddingleft')[i]
        lst_situation.append(fav.get_text())
    dict_meteo = dict(zip(lst_month, lst_situation))
    return dict_meteo

#### Fonction best city to go per month

def insert_month(month):
    ## Choix du mois préféré (mp)
    PATH = "/Users/hugol/chromedriver"
    driver = webdriver.Chrome(PATH)
    month = month.lower()
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
    df = pd.DataFrame(villes)
    df.rename(columns = {0:'Top 10 Villes à visiter en '+month}, inplace = True)
    driver.close()
    return df

#### Fonction first interface ###

from tkinter import *

def Interface_Saisie():
    root = Tk()
    root.title("Trip Planner")
    lc = []
    lm = []
    def quit():
        city = city_insert.get()
        month = month_insert.get()
        lc.append(city)
        lm.append(month)
        root.destroy()
    ##
    city_label = Label(root, text='Choisissez une ville :')
    city_label.grid(row=0, column=0)
    ##
    month_label = Label(root, text='Choisissez un mois :')
    month_label.grid(pady=18, padx=18, row=0, column=2)
    ##
    city_insert = Entry(root)
    city_insert.grid(pady=18, padx=18, row=0, column=1)
    ##
    month_insert = Entry(root)
    month_insert.grid(pady=18, padx=18, row=0, column=3)
    ##
    b1 = Button(root, text='Valider votre choix', command=quit)
    b1.grid(pady=10, row=1, column=3)
    root.mainloop()
    return lc[0], lm[0]

#### 10 best places ###

def best_places(city):
    PATH = "/Users/hugol/chromedriver"
    driver = webdriver.Chrome(PATH)
    city = city.lower()
    driver.get("https://generationvoyage.fr/visiter-"+city+"-faire-voir/")
    driver.find_element_by_class_name("css-bcexub").click()
    todo= driver.find_elements_by_class_name("title_lvl3")
    tds=[]
    for i in range(min(len(todo),10)):
        todo= driver.find_elements_by_class_name("title_lvl3")
        td= todo[i].text
        tds.append(td)
    driver.close()
    return tds

#### Code final ###

result = Interface_Saisie()
city = str(result[0])
month = str(result[1])
'''
if city == '':
    Interface1
elif month == '':
    Interface2
'''
bs = insert_city(city)
dict_meteo = extract(bs)
df_city = insert_month(month)
best_place = best_places(city)
print(dict_meteo) # Dictionnaire avec la situation meteo relier a un mois
print(df_city)
print(best_place)




