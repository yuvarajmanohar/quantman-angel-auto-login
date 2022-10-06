import os
import pyotp
import logging
import time
import sys
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

username = os.environ.get("USERNAMES")
password = os.environ.get("PASSWORDS")
totp = pyotp.TOTP(os.environ.get("TOTP"))

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://smartapi.angelbroking.com/publisher-login?api_key=YPPSOZ12")
#driver.maximize_window()

logging.info('Entering Login Name')
driver.find_element("id","client-code").send_keys(username)

logging.info('Entering Login Password')
driver.find_element("id","password").send_keys(password)

logging.info('Entering TOTP')
driver.find_element("id","totp").send_keys(totp.now())

driver.find_element(By.XPATH,'//button[@id="sign-in"]').click()

# Wait for login process to complete. 
time.sleep(5)

def isDisplayed():
    try:
        driver.find_element("id","client-code").send_keys(username)
    except NoSuchElementException:
        return False
    return True

if (isDisplayed() == True):
    logging.critical('Quantman login FAILED')
    sys.exit(1)
else:
    logging.info('Quantman login PASS')

# Close the driver
driver.close()
