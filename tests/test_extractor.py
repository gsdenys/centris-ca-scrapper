import time
from scrapper.extractor import Type, Extractor
from scrapper.paginate import Paginate
from scrapper.database import ENGINE

from selenium.webdriver.common.by import By

import pandas as pd

def test_new():
    ex = Extractor(Type.RENT, 5)
    
    assert ex is not None
    assert ex._Extractor__driver is not None
    
    driver = ex._Extractor__driver
    current_page = driver.find_element(By.CLASS_NAME, 'pager-current')
    
    assert current_page.text.startswith('5')
    
def test_run():
    ex = Extractor(Type.RENT, 5)
    
    driver = ex._Extractor__driver
    pg = Paginate(driver=driver)
    
    end = driver.find_element(By.CLASS_NAME, 'goLast')
    end.find_element(By.TAG_NAME, 'a').click()

    time.sleep(1)

    ex.run()
    
    df = pd.read_sql('SELECT * FROM items', ENGINE)
    assert len(df.index) > 0