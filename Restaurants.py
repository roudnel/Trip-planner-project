from selenium import webdriver
import time


def search_restaurant():
    
    search="Paris"
    website = 'https://www.tripadvisor.fr/Restaurants'
    import pyautogui
    path = 'chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get(website)
    time.sleep(5)
    restaurants=[]
    time.sleep(5)
    driver.find_element("id","onetrust-reject-all-handler").click()
    
    time.sleep(5)
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').click()
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').send_keys(search)
    time.sleep(5)
    driver.find_element("xpath",'//*[@id="typeahead_results"]/a[1]').click()
    time.sleep(5)
    html=driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    results=driver.find_elements("xpath",' //*[@id="EATERY_LIST_CONTENTS"]')
    List_of_rest=bs.find_all('a', class_='oHGMl')
    for j in range (0,10):
        restaurants.append(List_of_rest[j].text)
    return restaurants
    
   
    
    driver.close()

