#!/usr/bin/env python3
"""
    Write a type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_list: list of strings and integers
    """
    sum = 0
    for mem in mxd_lst:
        sum += mem
    return sum
