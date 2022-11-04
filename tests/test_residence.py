from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from scrapper.residence import Residence, CATEGORIES


def test_price():
    url = "https://www.centris.ca/en/properties~for-rent~montreal-island?view=Thumbnail"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    item = driver.find_element(By.CLASS_NAME, 'property-thumbnail-item')

    res = Residence(item=item)
    price = res.price()

    driver.close()

    assert type(price) == float
    assert 0 < price < 999999


def test_room():
    url = "https://www.centris.ca/en/properties~for-rent~montreal-island?view=Thumbnail"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    item = driver.find_element(By.CLASS_NAME, 'property-thumbnail-item')

    res = Residence(item=item)
    room = res.room()

    driver.close()

    assert 15 > room >= 0


def test_bath():
    url = "https://www.centris.ca/en/properties~for-rent~montreal-island?view=Thumbnail"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    item = driver.find_element(By.CLASS_NAME, 'property-thumbnail-item')

    res = Residence(item=item)
    bath = res.bath()

    driver.close()

    assert 5 > bath > 0


def test_category():
    url = "https://www.centris.ca/en/properties~for-rent~montreal-island?view=Thumbnail"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    item = driver.find_element(By.CLASS_NAME, 'property-thumbnail-item')

    res = Residence(item=item)
    cat = res.category()

    driver.close()

    assert cat in CATEGORIES.keys()


def test_address():
    url = "https://www.centris.ca/en/properties~for-rent~montreal-island?view=Thumbnail"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    item = driver.find_element(By.CLASS_NAME, 'property-thumbnail-item')

    res = Residence(item=item)
    address = res.address()
    city = address.city()

    driver.close()

    assert city == 'MONTRÉAL'
