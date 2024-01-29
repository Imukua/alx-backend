#!/usr/bin/env python3
"""script to return pagination parameters"""


def index_range(page, page_size):
    startIdx = (page - 1) * page_size
    endIdx = startIdx + page_size

    return (startIdx, endIdx)
