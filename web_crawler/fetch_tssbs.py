# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

class FetchTssbs(FetchUtil):
	def __init__(self, url):
		super(FetchTssbs, self).__init__(url)
		self.__data = {
			'title': '唐诗三百首',
			'abstract': '',
			'content': []
		}		

	def processing(self):
		soup = self.get_soup('/search.aspx?value=%s' % self.__data['title'])
		self.set_content(soup)
		self.to_json('./jsons/tangshisanbaishou.json', self.__data)

	def set_content(self, soup):
		typeconts = (soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
			.find('div', { 'class': 'sons' }).find_all('div', { 'class': 'typecont' }))

		total = 0
		for tc in typeconts:
			ml = tc.find('div', { 'class': 'bookMl' })

			content_list = []
			for s in tc.find_all('span'):
				ta = s.text
				author = None
				if ta.find('(') > -1:
					author = ta[ta.find('(') + 1:len(ta) - 1]
				content_list.append({
					'chapter': s.find('a').string,
					'author': author,
					'paragraphs': []
				})

			self.logging.info('%s 共%d首' % (ml.string, len(content_list)))
			total += len(content_list)
			self.__data['content'].append({
				'type': ml.string,
				'content': content_list
			})

		self.logging.info('%s 共%d首' % (self.__data['title'], total))

FetchTssbs('https://so.gushiwen.org').processing()
