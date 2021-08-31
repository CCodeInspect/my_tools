#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: pauline
@date 2021年08月30日3:07 下午
"""

import requests, json
from src.base.http_class import Http
from src.base.run_test import injectable, test, YaoudTestCase, inject
from src.data.csv import get_data
from src.url. import 

http =Http()
data = get_data('src/data/csv/')
class Test(YaoudTestCase):
