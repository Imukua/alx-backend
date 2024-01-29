#!/usr/bin/env python3
"""
returns start and end index
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns start and end index
    """
 
    return ((page-1) * page_size, page_size * page)
