import os
import sys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configuring the chrome driver for platform
BASE_DIR = os.path.dirname(__file__)

if sys.platform == 'linux':
    executable_path = os.path.join(BASE_DIR, 'drivers', 'chromedriver')
else:
    executable_path = os.path.join(BASE_DIR, 'drivers', 'chromedriver.exe')

# creating configurations to the driver
options = Options()
options.add_argument('start-maximized')
options.add_argument('--incognito')

driver = WebDriver(
    executable_path=executable_path,
    options=options
)

# navengando on the page of the unicartagena
path = 'http://sma.unicartagena.edu.co:8090/smaix12/'
driver.get(path)

# creating an explicit wait driver
driver_wait = WebDriverWait(driver=driver, timeout=20)


def get_element(path):
    return driver_wait.until(EC.element_to_be_clickable((By.XPATH, path)))
