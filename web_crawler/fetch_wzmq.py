# -*- coding: utf-8 -*-

from fetch_util import FetchUtil

class FetchWzmq(FetchUtil):
	"""docstring for FetchWzmq"""
	def __init__(self, url):
		super(FetchWzmq, self).__init__(url)

	def processing(self):
		soup = self.get_soup('/Search_Result.aspx?Type=0&Field=all&Value=文字蒙求')
		# self.set_content(soup)
		# self.to_json('./jsons/guwenguanzhi.json', self.__data)		
		target = soup.find('td', { 'class': 'sreach_result' }).find_all('a')[1]

		next_soup = self.get_soup('/' + target.attrs['href'])
		print(next_soup)

FetchWzmq('https://www.gujiguan.com').processing()
