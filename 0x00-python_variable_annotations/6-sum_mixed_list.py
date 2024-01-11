#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum as a float.
from typing import List, Union
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Computes the sum of a list of floating-point numbers.
    """
    return float(sum(input_list))
