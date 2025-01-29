# CENTRIS-CA-SCRAPPER
# Copyright (C) 2025  gsdenys.github.io

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

from enum import Enum

class Operation(Enum):
    """
    Enumeration representing the type of operation in the Centris.ca scraper.

    This enumeration provides two options:
    - FOR_SALE: Represents a property that is available for sale.
    - FOR_RENT: Represents a property that is available for rent.
    """
    FOR_SALE = 'for-sale'
    FOR_RENT = 'for-rent'

    def __str__(self) -> str:
        """
        Provides a string representation of the operation.

        Returns:
            str: A user-friendly description of the operation type.
        """
        return self.value
    
    def desc(self) -> str:
        """
        Provides a user-friendly description of the operation type.

        Returns:
            str: A description of the operation type.
        """
        if self == Operation.FOR_SALE:
            return "This operation represents a property that is available for sale."
        elif self == Operation.FOR_RENT:
            return "This operation represents a property that is available for rent."
        else:
            return "Unknown operation."
