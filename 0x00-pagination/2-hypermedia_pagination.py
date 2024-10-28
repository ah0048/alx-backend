#!/usr/bin/env python3
'''server class and index_range function'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing a start index and an end index'''
    if page <= 0 or page_size < 0:
        return "invalid page or page size"
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        '''return the appropriate page of the dataset'''
        try:
            assert isinstance(page, int)
            assert isinstance(page_size, int)
            assert page > 0
            assert page_size > 0
            dataset = self.dataset()
            start, end = index_range(page, page_size)
            if start >= len(dataset):
                return []
            return dataset[start:end]
        except AssertionError:
            raise AssertionError

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''return a dictionary with the following key-value pairs'''
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
