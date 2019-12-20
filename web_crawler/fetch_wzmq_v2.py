# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import BeautifulSoup, element
import re

class FetchWzmq(FetchUtil):
	def __init__(self, url = None):
		super(FetchWzmq, self).__init__(url)
		self.__data = {
			'title': '文字蒙求',
			'author': '王筠（1784-1854），字贯山，号菉友。清山东安丘人，道光元年（1821）举人，曾任陕西乡宁知县。他的著作有《说文释例》《说文解字句读》《文字蒙求》等。',
			'abstract': '《文字蒙求》包括天地類之純形；人類之純形；動物之純形；植物之純形；衣服器械屋宇之純形；一字象兩物形者；由象形字省之仍是象形者；避它字而變其形者；物多此形因兼其用以象之者；其形不能顯白因加同類字以定之；以會意定象形而别加一形者等内容。',
			'preface': [],
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
					self.__data['preface'].append(x.string)

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
