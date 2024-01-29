#!/usr/bin/env python3
"""script to return pagination parameters"""


def index_range(page, page_size):
    startIdx = page - 1
    endIdx = page_size

    return (startIdx, endIdx)
