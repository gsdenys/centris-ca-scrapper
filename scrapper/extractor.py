from pandas import Timestamp
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from scrapper.paginate import Paginate
from scrapper.residence import Residence
from scrapper.database import save

from selenium.webdriver.common.by import By


class Type:
    RENT = ('rent', 'https://www.centris.ca/en/properties~for-rent?view=Thumbnail')
    SALE = ('sale', 'https://www.centris.ca/en/properties~for-sale?view=Thumbnail')


class Extractor:
    def __init__(self, tp: Type, page: int) -> None:
        self.__type = tp
        self.__page = page

        self.__driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.__driver.get(tp[1])

        self.__paginate = Paginate(self.__driver)
        self.__goto_page()

    def __del__(self):
        self.__driver.close()

    def __goto_page(self) -> bool:
        for page in range(1, self.__page):
            if self.__paginate.has_next():
                self.__paginate.next()

        return page == self.__page

    def run(self):
        while True:
            items = self.__driver.find_elements(
                By.CLASS_NAME, 'property-thumbnail-item'
            )
            
            data = []

            for item in items:
                r = Residence(item)
                ads = r.address()
                data.append(
                    [
                        r.price(),
                        self.__type[0],
                        r.category(),
                        r.room(),
                        r.bath(),
                        ads.region(),
                        ads.city(),
                        ads.neighborhood(),
                        ads.district(),
                        Timestamp.now(),
                        self.__page
                    ]
                )
                
            save(data=data)
            
            if not self.__paginate.has_next():
                break
            
            self.__paginate.next()
            self.__page += 1