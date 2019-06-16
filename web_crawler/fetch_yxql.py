# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

data = {
	'title': '幼学琼林',
	'author': '程登吉',
	'abstract': None,
	'content': []
}

class FetchYxql(FetchUtil):
	def __init__(self, url):
		super(FetchYxql, self).__init__(url)

	def processing(self):
		self.get_soup(data['title'])
		data['abstract'] = self.get_abstract()
		