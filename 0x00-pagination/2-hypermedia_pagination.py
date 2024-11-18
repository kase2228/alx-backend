#!/usr/bin/env python3
"""
    prints the start and end index of the provided
    page arguments
"""
import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """"
        accepts page number and size
        returns tuple of size two:
            Start index and
            end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    A = (start_index, end_index)
    return A


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page
        """
        assert isinstance(
            page, int) and page > 0, "arguments should be +ve integers."
        assert isinstance(
            page_size, int
                ) and page_size > 0, "arguments should be +ve integers."

        data = self.dataset()
        length = len(data)
        start, end = index_range(page, page_size)

        if (start < length):
            return data[start:end]
        return []
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        "Return a dictionary of some important parameters"

        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = (total_items + page_size-1) // page_size

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
