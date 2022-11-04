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

class Paginate:
    """Paginate class to enable service walk through the centris.ca pages. This
    class is based on the Centris.ca web page and will not work with others sites
    or web components. 
    """
    
    def __init__(self, driver: webdriver.Chrome) -> None:
        """Default builder that receives the chrome web driver and store it at
        the object variable

        Args:
            driver (webdriver.Chrome): The active Chrome web driver
        """
        self.__driver = driver

    def has_next(self) -> bool:
        """Discover if there is another page after the actual. This method is
        based in a element class of the next button, that once the inactive class
        is present there no next page

        Returns:
            bool: True case there is another page, other else False.
        """
        next = self.__driver.find_element(By.CLASS_NAME, 'next')
            
        attribute_str = next.get_attribute("class")
        attributes = attribute_str.split()
        
        if 'inactive' in attributes: return False
        
        return True
    
    def next(self):
        """Method to execute the click over the next button to navigate to the
        next page.
        """
        next = self.__driver.find_element(By.CLASS_NAME, 'next')
        el = next.find_element(By.TAG_NAME, 'a')
        
        el.click()
