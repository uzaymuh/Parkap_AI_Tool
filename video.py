from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Chrome('C:/Users/onurs/Desktop/chromedriver.exe')
driver.get('http://seyret.nigde.bel.tr/')

time.sleep(3)

driver.save_screenshot("shot.png")
