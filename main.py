from datetime import datetime

import joboffer
import table
from status import *

# import status as * so you dont need to import status.Status.PENDING
# just Status.PENDING


def check_dates():
    """Check all the dates in the notice column, and returns a list of upcoming communications"""
    print("Nothing to do today, hurray!")


def main():
    print("Qur is working")


if __name__ == "__main__":
    joboffer.add(
        "Carlos",
        "Mercadolibre, puesto de fullstack",
        "http://mercadolibre.com",
        datetime.now(),
        datetime.today(),
        Status.PENDING,
        log=["me llego la oferta"],
    )
    table.write(columns=["my_column"], data="my_data", table="my_table")
    # TODO:
    #   connect to google sheets, pandas or excel
