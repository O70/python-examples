# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import element

# http://www.zggdwx.com/qianjiashi.html

class FetchQjs(FetchUtil):
	def __init__(self, url):
		super(FetchQjs, self).__init__(url)
		self.__data = {
			'title': '千家诗',
			'author': '南宋谢枋得/明代王相',
			'abstract': [],
			'content': []
		}	

	def processing(self):
		soup = self.get_soup('/qianjiashi.html')
		self.set_content(soup)
		self.to_json('./jsons/qianjiashi.json', self.__data)

	def set_content(self, soup):
		lc = soup.find('div', { 'id': 'left-content' })
		introduction = lc.find('fieldset', { 'class': 'introduction' }).find('div').find_all('p')
		for i in introduction:
			self.__data['abstract'].append(i.get_text())

		catalog = lc.find('fieldset', { 'class': 'catalog' }).find('div').find_all('a')
		for c in catalog:
			sub_soup = self.get_soup(c.attrs['href'])
			readbox = sub_soup.find('div', { 'id': 'readpage' }).find('div', { 'class': 'readbox' }).find('div', { 'class': 'content' })

			subname = readbox.find_all('h2', { 'class': 'subname' })
			subauther = readbox.find_all('p', { 'class': 'subauther' })
			shi = readbox.find_all('blockquote', { 'class': 'shi' })
			self.logging.info('%s --> subname size: %d, subauthor size: %d, shi size: %d' 
				% (c.string, len(subname), len(subauther), len(shi)))

			content_list = []

			first = readbox.find('h2')
			content_list.append({
				"chapter": first.string,
				"author": None,
				"paragraphs": []
			})
			for h in first.next_siblings:
				if h.name != None:
					if h.name == 'h2':
						content_list.append({
							"chapter": h.string,
							"author": None,
							"paragraphs": []
						})
					elif h.name == 'p':
						if content_list[len(content_list) - 1]['author'] == None:
							content_list[len(content_list) - 1]['author'] = h.string
					elif h.name == 'blockquote':
						pass

			# for rb in readbox.children:
			# 	if isinstance(rb, element.NavigableString):
			# 		continue

			# 	tag_name = rb.name
			# 	if tag_name == 'h2':
			# 		content_list.append({ 'chapter': rb.string })
			# 	elif tag_name == 'p':
			# 		content_list[len(content_list) - 1]['author'] = rb.string
			# 	elif tag_name == 'blockquote':
			# 		# print(content_list[len(content_list) - 1])
			# 		content_list[len(content_list) - 1]['paragraphs'] = rb.get_text()
			# 		for s in rb.children:
			# 			# print(s)
			# 			pass

			# {
		 #          "chapter": "行宮",
		 #          "subchapter": null,
		 #          "author": "唐代：元稹 ",
		 #          "paragraphs": [
		 #            "寥落古行宮，宮花寂寞紅。",
		 #            "白頭宮女在，閒坐說玄宗。"
		 #          ]
		 #        }

			self.__data['content'].append({
				'type': c.string,
				'content': content_list
			})

FetchQjs('http://www.zggdwx.com').processing()
