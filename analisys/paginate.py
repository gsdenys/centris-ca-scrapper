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
    """
    A helper class for navigating paginated pages on centris.ca using Selenium.
    
    This class interacts with the web elements of the Centris.ca website
    to facilitate traversal across multiple pages. It is tailored to Centris.ca
    and is not guaranteed to work with other websites or web components.
    """

    def __init__(self, driver: webdriver.Chrome) -> None:
        """
        Initializes the Paginate instance with a Selenium WebDriver.

        Args:
            driver (webdriver.Chrome): The active Chrome WebDriver instance
                to be used for interacting with the web pages.
        """
        self.__driver = driver

    def __has_next(self) -> bool:
        """
        Checks if there is a next page available for navigation.

        This method inspects the "next" button on the page and determines
        its availability based on the presence of the 'inactive' CSS class.

        Returns:
            bool: True if the "next" button is active (indicating more pages are available),
                  otherwise False.
        """
        next_btn = self.__driver.find_element(By.CLASS_NAME, 'next')
        attribute_str = next_btn.get_attribute("class")
        attributes = attribute_str.split()
        
        return 'inactive' not in attributes

    def __next_page(self) -> None:
        """
        Navigates to the next page by clicking the "next" button.

        This method assumes the "next" button is present and clickable. It
        should be called only after verifying the presence of a next page
        using the `__has_next` method.
        """
        next_btn = self.__driver.find_element(By.CLASS_NAME, 'next')
        next_btn.click()

    def __iter__(self) -> 'Paginate':
        """
        Initializes the instance as an iterator.

        Returns:
            Paginate: The instance itself to support iteration.
        """
        return self

    def __next__(self) -> webdriver.Chrome:
        """
        Defines the iteration logic for navigating to the next page.

        If a next page is available, this method navigates to it and returns
        the WebDriver instance. If there are no more pages, it raises
        a StopIteration exception to end the iteration.

        Returns:
            webdriver.Chrome: The WebDriver instance after navigating to the next page.

        Raises:
            StopIteration: If no further pages are available.
        """
        if not self.__has_next():
            raise StopIteration
        
        self.__next_page()
        
        return self.__driver.page_source