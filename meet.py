from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import time


username = getpass.getuser()
link = input("Enter your meet link here: ") 
"""*******************OPTIONS***********************"""
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir=C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome("chromedriver.exe",options=options)

driver.get(link)
start = time.time()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div").click()
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div").click()
 
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span"))
    )
finally:
    element.click()

#driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span/span").click()