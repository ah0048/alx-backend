#!/usr/bin/env python3
"""Write a function named index_range that takes two integer"""


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing a start index and an end index'''
    if page <= 0 or page_size < 0:
        return "invalid page or page size"
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
