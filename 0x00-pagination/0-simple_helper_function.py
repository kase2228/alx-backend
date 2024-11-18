#!/usr/bin/env python3
"""
    prints the start and end index of the provided
    page arguments
"""
def index_range(page: int, page_size:int) -> tuple:
    """"
        accepts page number and size
        returns tuple of size two: 
            Start index and
            end index
    """
    start_index = (page -1) * page_size
    end_index = start_index + page_size
    A = (start_index, end_index)
    return A