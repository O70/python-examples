# -*- coding: utf-8 -*-

import json, requests
from bs4 import BeautifulSoup
from opencc import OpenCC

class FetchUtils(object):
	def __init__(self):
		super(FetchUtils, self).__init__()

	def get_soup(self, url):
		response = requests.get(url)
		return BeautifulSoup(response.text, "html.parser")

	def replace(self, txt):
		return txt.strip().replace(' ', '').replace('.', '。').replace(',', '，').replace('?', '？').replace('!', '！').replace('\n', '')

	def convert(self, txt):
		return OpenCC('s2t').convert(txt)