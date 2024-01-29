#!/usr/bin/env python3
"""script to return pagination parameters"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    startIdx = (page - 1) * page_size
    endIdx = page * page_size
    return startIdx, endIdx
