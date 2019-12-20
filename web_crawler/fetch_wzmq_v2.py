# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import BeautifulSoup, element
import re

class FetchWzmq(FetchUtil):
	def __init__(self, url = None):
		super(FetchWzmq, self).__init__(url)
		self.__data = {
			'title': '文字蒙求',
			'abstract': [],
			'content': []
		}

	def processing(self):
		# soup = self.get_soup(self.url)
		with open('files/wiki_wenzimengqiu.html') as f:
			soup = BeautifulSoup(f.read(), "html.parser")
		self.set_content(soup)
		self.to_json('./jsons/wenzimengqiu.json', self.__data)

	def set_content(self, soup):
		soup_tr = soup.find_all('tr', id = re.compile('^p[0-9]+'))
		total = len(soup_tr)
		print('Total tr:', total)

		alen = 2
		for i in range(alen):
			for x in soup_tr[i].contents[1].children:
				if x.string:
					self.__data['abstract'].append(x.string)

		for i in range(alen, total):
			tr = soup_tr[i]
			sub_title = tr.find(colspan = 2)
			if sub_title:
				self.__data['content'].append({
					'title': sub_title.contents[0]['id'].replace(self.__data['title'], ''),
					'paragraphs': []
				})
			else:
				content = self.__data['content']
				para = content[len(content) - 1]['paragraphs']
				td = tr.contents[1]
				for x in td.children:
					if isinstance(x, element.NavigableString):
						para.append(x.string)
					else:
						txt = x.get_text()
						if txt:
							para.append(txt)

# FetchWzmq('https://ctext.org/wiki.pl?if=gb&chapter=912588&remap=gb').processing()
FetchWzmq().processing()
