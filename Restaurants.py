from selenium import webdriver
import time

def search_restaurant(city):
    
    website = 'https://www.tripadvisor.fr/Restaurants'
    import pyautogui
    path = '/Users/Laetitia/OneDrive/Documents/MS dS2E/Projet Kevin/chromedriver'
    driver = webdriver.Chrome(path)
    driver.get(website)
    time.sleep(5)
    #pyautogui.press("enter")
   # drive.find_element("id","onetrust-accept-btn-handler").click()
    driver.find_element("id","onetrust-reject-all-handler").click()
    
    
    
    time.sleep(5)
    #driver.find_element( "xpath",'//*[@id="accept-recommended-btn-handler"]').click()
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').click()
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/input[1]').send_keys(city)
 
    driver.find_element("xpath",'//*[@id="component_6"]/div/div/form/button[3]').click()
    time.sleep(4)
    driver.find_element("xpath",'//*[@id="search-filters"]/ul/li[4]/a').click()
    time.sleep(4)
    results=driver.find_elements("xpath",'//div[@class="result-title"]/span')
    [print(i.text) for i in results]

    restaurants = driver.find_elements("xpath",'//div[@class="result-title"]')
    #result = driver.page_source
    #results=driver.find_elements("class name",'search-results-list')
    
    driver.close()
