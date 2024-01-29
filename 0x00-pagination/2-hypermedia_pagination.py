#!/usr/bin/env python3


"""
script to returns paginated dataset
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns start and end index
    """

    startIdx = (page - 1) * page_size
    endIdx = page * page_size
    return startIdx, endIdx


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
        """gets paginated dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns dict type paginatted results
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        totaPages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if page < totaPages else None,
            'prev_page': page - 1 if page > 0 else None,
            'total_pages': totaPages
        }
