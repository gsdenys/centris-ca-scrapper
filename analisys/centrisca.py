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

# Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Use chrome driver manager
from webdriver_manager.chrome import ChromeDriverManager as DriverManager

# Custom Types to cover the infos from centris.ca
from operations import Operation

# Constants
BASE_URL = 'https://www.centris.ca/en/properties'
"""
str: The base URL for accessing property listings on Centris.ca.
"""

PAGE_VIEW = 'Summary'
"""
str: The default page view for Centris.ca URLs.
"""

POPUP_AGREE_BTN_ID = 'didomi-notice-agree-button'
"""
str: The ID of the button used to agree to cookies or dismiss a popup on Centris.ca.
"""

NEXT_BTN_CLASS_NAME = 'next'
"""
str: The CSS class name for the "Next" button used for pagination.
"""

INACTIVE_NEXT_BTN_CLASS_NAME = 'inactive'
"""
str: The CSS class name for the inactive "Next" button, indicating no further pages exist.
"""


def _get_url(operation: Operation, search_region: str = '') -> str:
    """
    Constructs a Centris.ca URL based on the operation and search region.

    Args:
        operation (Operation): The type of operation (e.g., Operation.FOR_SALE or Operation.FOR_RENT).
        search_region (str, optional): The search region (e.g., 'montreal-lasalle').
            Defaults to an empty string.

    Returns:
        str: A properly formatted Centris.ca URL.
    """
    search_region = f"~{search_region}" if search_region else ''
    return f"{BASE_URL}~{operation.value}{search_region}?view={PAGE_VIEW}"


class Paginate:
    """
    A helper class for navigating paginated pages on centris.ca using Selenium.
    
    This class interacts with the web elements of the Centris.ca website
    to facilitate traversal across multiple pages. It is tailored to Centris.ca
    and is not guaranteed to work with other websites or web components.
    """

    def __init__(self, operation: Operation, search_region: str, handle_popup: bool = True) -> None:
        """
        Initializes the Paginate instance and a Selenium WebDriver.

        The WebDriver is configured to navigate to the Centris.ca website
        based on the specified operation and search region.

        Args:
            operation (Operation): The operation type, e.g., FOR_SALE or FOR_RENT.
            search_region (str): The region to search in, e.g., 'montreal-lasalle'.
            handle_popup (bool, optional): Whether to handle popups. Defaults to True.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Required for running as root
        # chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920x1080")
        
        self.__driver = webdriver.Chrome(service=Service(DriverManager().install()), options=chrome_options)
        self.__driver.get(_get_url(operation, search_region))

        if handle_popup:
            self.__remove_popup()

    def __remove_popup(self) -> None:
        """
        Removes a popup by clicking the "Agree" button.
        """
        try:
            el = self.__driver.find_element(By.ID, POPUP_AGREE_BTN_ID)
            el.click()
        except NoSuchElementException:
            logging.warning("Popup button not found. Skipping popup removal.")
    
    def __has_next(self) -> bool:
        """
        Checks if there is a next page available for navigation.
        """
        next_btn = self.__driver.find_element(By.CLASS_NAME, NEXT_BTN_CLASS_NAME)
        return INACTIVE_NEXT_BTN_CLASS_NAME not in next_btn.get_attribute("class").split()

    def __next_page(self) -> None:
        """
        Navigates to the next page by clicking the "next" button.
        """
        next_btn = self.__driver.find_element(By.CLASS_NAME, NEXT_BTN_CLASS_NAME)
        next_btn.click()

    def __iter__(self) -> 'Paginate':
        return self

    def __next__(self) -> str:
        """
        Navigates to the next page and returns its HTML content.
        """
        if not self.__has_next():
            raise StopIteration
        
        self.__next_page()
        return self.__driver.page_source

    def close(self) -> None:
        """
        Closes the Selenium WebDriver session.
        """
        self.__driver.close()

    def quit(self) -> None:
        """
        Quits the Selenium WebDriver session.
        """
        self.__driver.quit()