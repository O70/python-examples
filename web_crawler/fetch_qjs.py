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
			sub_soup = self.get_soup(c.attrs['href'])
			readbox = sub_soup.find('div', { 'id': 'readpage' }).find('div', { 'class': 'readbox' }).find('div', { 'class': 'content' })

			subname = readbox.find_all('h2', { 'class': 'subname' })
			subauther = readbox.find_all('p', { 'class': 'subauther' })
			shi = readbox.find_all('blockquote', { 'class': 'shi' })
			self.logging.info('%s --> subname size: %d, subauthor size: %d, shi size: %d' 
				% (c.string, len(subname), len(subauther), len(shi)))

			self.__data['content'].append({
				'type': c.string,
				'content': []
			})

FetchQjs('http://www.zggdwx.com').processing()
