# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

class FetchYxql(FetchUtil):
	def __init__(self, url):
		super(FetchYxql, self).__init__(url)
		self.__data = {
			'title': '幼学琼林',
			'author': '程登吉',
			'abstract': None,
			'content': []
		}

	def processing(self):
		soup = self.get_soup('/search.aspx?value=%s' % self.__data['title'])
		sonspic_cont = soup.find('div', { 'class': 'sonspic' }).find('div', { 'class': 'cont' }).find_all('p')
		self.set_abstract(sonspic_cont)
		self.set_content(sonspic_cont)
		self.to_json('./jsons/youxueqionglin.json', self.__data)
		# self.to_json('/Users/Guiwang/Workspace/Pythons/chinese-poetry/mengxue/youxueqionglin.json', self.__data)

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

		bookcont = soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' }).find('div', { 'class': 'sons' }).find_all('div', { 'class': 'bookcont' })
		for bc in bookcont:
			title = bc.find('div', { 'class': 'bookMl' }).string

			content_list = []
			for t in bc.find_all('span'):
				tag_a = t.find('a')
				parg_soup = self.get_soup(tag_a.attrs['href'])

				contson = parg_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'contson' })
				paragraphs_list = []
				for p in contson.find_all('p'):
					paragraphs_list.append(self.replace(p.string))

				content_list.append({
					'chapter': tag_a.string,
					'paragraphs': paragraphs_list
				})

			self.__data['content'].append({
				'title': title,
				'content': content_list
			})

