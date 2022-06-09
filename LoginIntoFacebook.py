from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

elem = browser.find_element(by=By.XPATH, value='//*[.="Allow essential and optional cookies"]')
print(elem)
elem.click()
