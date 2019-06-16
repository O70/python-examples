# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

class FetchGwgz(FetchUtil):
	def __init__(self, url):
		super(FetchGwgz, self).__init__(url)
		self.__data = {
			'title': '古文观止',
			'abstract': None,
			'content': []
		}

	def processing(self):
		soup = self.get_soup('/search.aspx?value=%s' % self.__data['title'])
		self.set_content(soup)
		self.to_json('./jsons/guwenguanzhi.json', self.__data)

	def set_content(self, soup):
		typeconts = (soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
			.find('div', { 'class': 'sons' }).find_all('div', { 'class': 'typecont' }))
		self.logging.info('%s 共%d卷' % (self.__data['title'], len(typeconts)))

		for v in typeconts:
			title = v.find('div', { 'class': 'bookMl' }).string

			content_list = []
			for s in v.find_all('span'):
				tag_a = s.find('a')

				sub_soup = self.get_soup(tag_a.attrs['href'])
				cont = (sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
					.find('div', { 'class': 'sons' }).find('div', { 'class': 'cont' }))
				author = cont.find('p', { 'class': 'source' }).get_text()

				paragraphs_list = []

				'''
				1. len(p) == 0
				2. len(p) > 0
				3. p中包含br
				'''
				if len(cont.find('div', { 'class': 'contson' }).find_all('p')) > 0:
				# print(len(cont.find('div', { 'class': 'contson' }).find_all('p')))
					for p in cont.find('div', { 'class': 'contson' }).find_all('p'):
						print(tag_a.string)
						paragraphs_list.append(self.replace(p.get_text()))

				content_list.append({
					'chapter': tag_a.string,
					'source': s.get_text().replace(tag_a.string, ''), 
					'author': author,
					'paragraphs': paragraphs_list
				})

			self.__data['content'].append({
				'title': title,
				'content': content_list
			})