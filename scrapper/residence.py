# CENTRIS-CA-SCRAPPER
# Copyright (C) 2022  gsdenys.github.io

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from selenium import webdriver
from selenium.webdriver.common.by import By

from scrapper.address import Address

CATEGORIES = {
    "HOUSE": "HOUSE",
    "HOME": "HOUSE",
    "CONDOMINIUM": "HOUSE",
    "STUDIO": "STUDIO",
    "LOFT": "STUDIO",
    "CONDO": "CONDO",
    "DUPLEX": "CONDO",
    "QUINTUPLEX": "CONDO",
    "LOT": "LOT"
}

class Residence:
    """Class perform actions over the residence DOM object and extract all
    provided information.
    """

    def __init__(self, item: webdriver.Chrome) -> None:
        """Default builder that receives an item correspondent to the residence
        ande store it in the object variable.

        This builder also create the address array that will be used latter to
        parse many address line

        Args:
            item (webdriver.Chrome): The residence item
        """
        self.__item = item

    def price(self) -> float:
        """Obtains the price from DOM residence item.

        Returns:
            float: the residence price 
        """
        selector = "a>div.price>span"

        price_el = self.__item.find_element(By.CSS_SELECTOR, selector)
        price = price_el.text.replace('$', '').replace(',', '')

        return float(price)

    def __quantity(self, selector: str) -> int:
        """Private method to based on received selector perform an extraction and
        returns an integer.

        Args:
            selector (str): the selector to perform extraction

        Returns:
            int: the value of extraction
        """
        try:
            item = self.__item.find_element(By.CSS_SELECTOR, selector)
            return int(item.text)
        except:
            return 0

    def room(self) -> int:
        """Extract the number of rooms

        Returns:
            int: the number of rooms
        """
        return self.__quantity("div>a>div>div.cac")

    def bath(self) -> int:
        """Extract the number of bathrooms

        Returns:
            int: the number of bathrooms
        """
        return self.__quantity("div>a>div>div.sdb")

    def category(self) -> str:
        """Obtains the category of residence (condo, maison, duplex, etc)

        Returns:
            str: the category
        """
        selector = "a>div.location-container>span.category>div"

        el = self.__item.find_element(By.CSS_SELECTOR, selector)
        cats = el.text.split()
        
        # Case has no information about category
        if len(cats) == 0: return None
        
        try:
            return CATEGORIES[cats[0].upper()]
        except:
            return None
        
    def address(self) -> Address:
        """Obtains the address parser

        Returns:
            Address: the address parser
        """
        selector = "a>div.location-container>span.address>div"

        els = self.__item.find_elements(By.CSS_SELECTOR, selector)

        address_list = []
        for i in els:
            address_list.append(i.text)
        
        return Address(address_list)
    
