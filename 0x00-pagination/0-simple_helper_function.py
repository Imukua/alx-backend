#!/usr/bin/env python3
"""script to return pagination parameters"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns start and end index
    """

    startIdx = (page - 1) * page_size
    endIdx = page * page_size
    return startIdx, endIdx
