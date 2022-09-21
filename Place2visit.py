### 10 best places to visit
from selenium import webdriver

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
    return tds         ##### PROBLEME CERTAINES VILLES NE MARCHE PAS
