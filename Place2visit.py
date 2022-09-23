from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import pyautogui

def best_places(city):
    PATH = "/Users/hugol/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.tripadvisor.fr/")
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="onetrust-reject-btn-container"]').click()
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='lithium-root']/main/div[1]/div[2]/div/div/div[1]/a").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/form/input[1]").send_keys(city)
    time.sleep(2)
    pyautogui.press("enter")
    driver.find_element_by_xpath("//*[@id='global-nav-attractions']").click()
    time.sleep(5)
    lst_place=[]
    for i in range(1, 11):
        place = driver.find_element_by_xpath("//*[@id='lithium-root']/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[2]/section[4]/div/div/span/div/div[2]/div/span["+str(i)+"]/div/article/div[2]/header/div/div/a[1]/h3/div/span/div").text
        lst_place.append(place)
    driver.close()
    return lst_place

