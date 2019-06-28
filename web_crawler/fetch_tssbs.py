# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import element

class FetchTssbs(FetchUtil):
	def __init__(self, url):
		super(FetchTssbs, self).__init__(url)
		self.__data = {
			'title': '唐诗三百首',
			'abstract': '《唐诗三百首》是一部流传很广的唐诗选集。唐朝（618年~907年）二百八十九年间，是中国诗歌发展的黄金时代，云蒸霞蔚，名家辈出，唐诗数量多达五万余首。',
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

				sub_soup = self.get_soup(s.find('a').attrs['href'])
				cont = (sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
					.find('div', { 'class': 'sons' }).find('div', { 'class': 'cont' }))
				author = cont.find('p', { 'class': 'source' }).get_text()

				paragraphs_list = []
				for p in cont.find('div', { 'class': 'contson' }).children:
					if isinstance(p, element.NavigableString):
						paragraphs_list.append(p.string.strip())

				chapter = s.find('a').string.strip()
				sc = cont.find('h1').string.strip()
				subchapter = None
				if chapter != sc:
					subchapter = sc

				content_list.append({
					'chapter': chapter,
					'subchapter': subchapter,
					'author': author,
					'paragraphs': paragraphs_list
				})

			self.logging.info('%s 共%d首' % (ml.string, len(content_list)))
			total += len(content_list)
			self.__data['content'].append({
				'type': ml.string,
				'content': content_list
			})

		self.logging.info('%s 共%d首' % (self.__data['title'], total))

# FetchTssbs('https://so.gushiwen.org').processing()
