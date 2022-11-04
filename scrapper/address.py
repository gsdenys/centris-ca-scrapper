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
import re

from scrapper.city import cities


class Address:
    """Address parser for the address extracted from centris.ca web site.
    """

    def __init__(self, address: list[str]) -> None:
        """Default builder that receives a address list and store it as object 
        variable.

        Args:
            address (list[str]): the address list
        """
        self.__address = address

        self._city = None
        self._region = None
        self._district = None
        self._neighborhood = None

    def address(self) -> str:
        """Obtain the full address as extracted from the site

        Returns:
            str: _description_
        """
        # Case has no address provided it should return None
        if len(self.__address) == 0:
            return None

        # Case the provided address is a empty string it should return None
        if len(self.__address[0].strip()) == 0:
            return None

        return self.__address[0].upper()

    def city(self) -> str:
        """Obtains the city name

        Returns:
            str: the city name
        """

        if self._city is None:
            # Case city/district not exists the program should return None
            if len(self.__address) < 2:
                return None

            # Replace all informations after city name by empty string. At the
            # replacing, the city name is converted by Upper Case
            self._city = re.sub(r'[\s]\(.*\)', '', self.__address[1]).upper()

        return self._city

    def region(self) -> str:
        """Obtains the region from city name

        Returns:
            str: the region
        """
        # Every time that regions was not calculated yet and the city information
        # exist, the region should be obtained from city dictionary
        if self._region is None and self.city() is not None:
            self._region = cities[self.city()]

        return self._region

    def district(self) -> str:
        """Obtains the district

        Returns:
            str: the district
        """
        if self._district is None:
            # Case city/district not exists the program should return None
            if len(self.__address) < 2:
                return None

            # Replace all information
            self._district = self.__address[1]
            self._district = re.sub(r'.*\(', '', self._district)
            self._district = re.sub(r'\).*', '', self._district)

            # Case have no information about district it should return None
            if len(self._district.strip()) == 0:
                return None

            self._district = self._district.upper()

            # Case the district is the same of city it should return None
            if self._district == self.city():
                return None

        return self._district

    def neighborhood(self) -> str:
        """Obtains the neighborhood

        Returns:
            str: the neighborhood
        """
        if self._neighborhood is None:
            # Case has no information about neighborhood
            if len(self.__address) < 3:
                return None

            # Case the info about neighborhood is None
            if self.__address[2] is None:
                return None

            self._neighborhood = self.__address[2].replace(
                'Neighbourhood ', '')
            self._neighborhood = self._neighborhood.upper()

        # case the neighborhood is a
        if len(self._neighborhood.strip()) == 0:
            return None

        return self._neighborhood
