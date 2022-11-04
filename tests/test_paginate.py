from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from scrapper.paginate import Paginate 

url = "https://www.centris.ca/en/properties~for-rent?view=Thumbnail"

def test_has_next():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    
    pg = Paginate(driver=driver)
    
    assert pg.has_next()
    
    end = driver.find_element(By.CLASS_NAME, 'goLast')
    end.find_element(By.TAG_NAME, 'a').click()
    
    assert not pg.has_next()
    
    driver.close()

def test_next():
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    
    current_page = driver.find_element(By.CLASS_NAME, 'pager-current')
    assert current_page.text.startswith('1')
    
    pg = Paginate(driver=driver)
    pg.next()
    
    current_page = driver.find_element(By.CLASS_NAME, 'pager-current')
    assert current_page.text.startswith('2')
    
    driver.close()