#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: pauline
@date 2021年08月30日3:07 下午
"""

import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        print('[%0.8fs] %s -> %r ' % (elapsed, name, result))
        return result

    return clocked


@functools.lru_cache(maxsize=2, typed=False)
@clock
def get_now():
    import time
    # print(time.time())
    return 0


@functools.lru_cache(maxsize=2)
@clock
def fibonacci(n):  # 调用函数
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    get_now()
    fibonacci(10)
