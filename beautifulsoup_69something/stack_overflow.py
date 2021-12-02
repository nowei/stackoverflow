from urllib.parse import urlunparse, urlparse 
from urllib.request import urlretrieve
from selenium import webdriver 
from bs4 import BeautifulSoup as bs
from urllib.request import ( urlopen, urlretrieve)  
from os import sys
import time
import requests


html_text = requests.get("https://www12.honolulu.gov/csdarts/frmApptInt.aspx").text
print(html_text) 
soup = bs(html_text, 'lxml')

driver = webdriver.Chrome()
driver.get("https://www12.honolulu.gov/csdarts/frmApptInt.aspx")

click_eligible = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/div[3]/input") 
click_eligible.click()

click_location = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[1]/p[1]/table/tbody/tr/td/select")
click_location.click()

time.sleep(0.2) 
click_koolau =driver.find_element_by_xpath("//select/option[@value='6']")
click_koolau.click()

find = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[1]/p[1]/table/tbody/tr/td/input[1]")
find.click()

print(driver.page_source)