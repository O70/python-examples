# -*- coding: utf-8 -*-

from fetch_yxql import FetchYxql
from fetch_zgxw import FetchZgxw

a = FetchYxql()
print(a.get_soup())
b = FetchZgxw()
print(b.get_soup())