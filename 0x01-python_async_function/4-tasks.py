#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function
task_wait_n.The code is nearly identical to wait_n except
task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function for task_wait_n"""
    wait_sec = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(wait_sec)
