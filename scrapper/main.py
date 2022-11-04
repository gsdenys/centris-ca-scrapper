from selenium import webdriver   
    
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from scrapper.paginate import Paginate


URLS = [
    'https://www.centris.ca/en/properties~for-rent?view=Thumbnail', 
    'https://www.centris.ca/en/properties~for-sale?view=Thumbnail'
]
