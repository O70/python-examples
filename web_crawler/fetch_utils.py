# -*- coding: utf-8 -*-

import json, requests
from bs4 import BeautifulSoup
from opencc import OpenCC

class FetchUtils(object):
	def __init__(self):
		super(FetchUtils, self).__init__()

	def get_text(self):
		print('fetch....')
