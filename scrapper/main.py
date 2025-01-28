from selenium import webdriver   
    
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from scrapper.paginate import Paginate





def __execute(url: str) -> list:
    data = []
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    
    driver.close()
    return data
    
def main():
    for url in URLS:
        data = __execute(url=url)