from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

urls = ['url1', 'url2', 'url3', 'url4', 'url5']

xpaths = ['xpath1', 'xpath2']

for url in urls:
    driver.get(url)
    for xpath in xpaths:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            print(f'Element text: {element.text}')
        except:
            print(f'Element not found: {xpath}')

driver.quit()
