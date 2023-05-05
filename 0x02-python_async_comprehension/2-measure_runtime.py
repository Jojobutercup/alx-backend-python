#!/usr/bin/env python3
"""
A coroutine that measures the total runtime of four parallel
async comprehensions using asyncio.gather().
"""

import time
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of async_comprehension called
    4 times in parallel."""
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    return end_time - start_time


async def main() -> None:
    """Runs the measure_runtime coroutine and prints the total runtime."""
    print(f"Total runtime: {await measure_runtime():.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
