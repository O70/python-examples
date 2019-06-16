# -*- coding: utf-8 -*-

import json, requests, logging
from bs4 import BeautifulSoup
from opencc import OpenCC

class FetchUtil(object):
	def __init__(self, url):
		super(FetchUtil, self).__init__()
		self.url = url
		self.logging = logging
		self.logging.basicConfig(level=logging.INFO)

	def get_soup(self, uri):
		url = self.url + uri
		self.logging.info(url)
		response = requests.get(url)
		return BeautifulSoup(response.text, "html.parser")

	def replace(self, txt):
		return txt.strip().replace(' ', '').replace('.', '。').replace(',', '，').replace('?', '？').replace('!', '！').replace(':', '：').replace('\n', '')

	def convert(self, txt):
		return OpenCC('s2t').convert(txt)

	def to_json(self, path, data):
		with open(path, 'w', encoding='utf-8') as file_object:
			json.dump(json.loads(self.convert(json.dumps(data, ensure_ascii = False))), file_object, sort_keys = False, indent = 2, ensure_ascii = False)