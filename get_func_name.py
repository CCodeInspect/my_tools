#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: pauline
@date 2021年08月30日3:13 下午
"""
# ! /usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
#
#
# @log
# def now():
#     print('2015-3-25')


# now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator

# @logger('DEBUG')
# def today():
# print('2015-3-25')

#
# today()
# print(today.__name__)

# def now():
#     # print(time.time())
#     # a = '123'
#     print('123')
#     # return time.time()
#     # return 0
#
#
# # f = now()
#
# if __name__ == '__main__':
#     print(now().__name__)

#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper()
