#!/usr/bin/env python3
"""
Module defines a  function named index_range
that takes two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size 2 having the start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
