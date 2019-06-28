# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

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
			self.__data['content'].append({
				'type': c.string,
				'href': c.attrs['href']	
			})

FetchQjs('http://www.zggdwx.com').processing()
