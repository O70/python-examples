# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
import re

class FetchWzmq(FetchUtil):
	def __init__(self, url):
		super(FetchWzmq, self).__init__(url)
		self.__data = {
			'title': '文字蒙求',
			'abstract': [],
			'content': []
		}

	def processing(self):
		soup = self.get_soup(self.url)
		print(soup)
		self.set_content(soup)
		self.to_json('./jsons/wenzimengqiu.json', self.__data)

	def set_content(self, soup):
		soup_tr = soup.find_all('tr', id = re.compile('^p[0-9]+'))
		# print(len(soup_tr))

		# for tr in soup_tr:
		# 	print(tr.name, tr['class'])

FetchWzmq('https://ctext.org/wiki.pl?if=gb&chapter=912588&remap=gb').processing()
