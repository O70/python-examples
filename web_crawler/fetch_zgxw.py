# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

class FetchZgxw(FetchUtil):
	def __init__(self, url):
		super(FetchZgxw, self).__init__(url)
		self.__data = {
			'title': '增广贤文',
			'author': '佚名',
			'abstract': None,
			'content': []
		}

	def processing(self):
		soup = self.get_soup('/search.aspx?value=%s' % self.__data['title'])
		sonspic_cont = soup.find('div', { 'class': 'sonspic' }).find('div', { 'class': 'cont' }).find_all('p')
		self.set_abstract(sonspic_cont)
		self.set_content(sonspic_cont)
		self.to_json('./jsons/zengguangxianwen.json', self.__data)

	def set_abstract(self, sonspic_cont):
		abstract = None
		try:
			abstract = sonspic_cont[1]
		except Exception as e:
			print('Get abstract error: %s' % e)
		else:
			self.__data['abstract'] = self.replace(abstract.get_text().replace(abstract.find('a').get_text(), ''))

	def set_content(self, sonspic_cont):
		uri = sonspic_cont[0].find('a').attrs['href']
		soup = self.get_soup(uri)

		for s in soup.find('div', { 'class': 'sons' }).find_all('a'):
			sub_soup = self.get_soup(s.attrs['href'])
			cont = sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'cont' })
			chapter = cont.find('h1').find('span').find('b').string
			paragraphs_list = []
			paragraphs = cont.find('div', { 'class': 'contson' })
			if not paragraphs.find('p') is None:
				paragraphs = paragraphs.find('p')
			for p in paragraphs:
				p = p.string
				if not p is None and len(p.strip()) > 0:
					paragraphs_list.append(self.replace(p))

			self.logging.info('%s %s 共%d行' % (self.__data['title'], chapter, len(paragraphs_list)))
			self.__data['content'].append({
				'chapter': cont.find('h1').find('span').find('b').string,
				'paragraphs': paragraphs_list
			})