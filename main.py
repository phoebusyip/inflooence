
# importing necessary packages
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
ser = Service("C:/Users/chy32/webscrape/chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service = ser, options = op)
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# for holding the resultant list
element_list = []

# for page in range(1, 3, 1):

# page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("C:/Users/chy32/webscrape")
driver.get(page_url)


# title = driver.find_elements_by_class_name("title")
title = driver.find_elements(By.CLASS_NAME, "title")
price = driver.find_elements(By.CLASS_NAME, "price")
description = driver.find_elements(By.CLASS_NAME, "description")
rating = driver.find_elements(By.CLASS_NAME, "ratings")

# price = driver.find_elements_by_class_name("price")
# description = driver.find_elements_by_class_name("description")
# rating = driver.find_elements_by_class_name("ratings")

for i in range(len(title)):
    element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

#closing the driver
driver.close()