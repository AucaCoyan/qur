from typing import List


def write_column(data, into_table):
    pass


def write(columns: List, data, table):
    """Takes a single row and writes into the table"""
    for column in columns:
        write_column(data, table)
    print("writing data")
