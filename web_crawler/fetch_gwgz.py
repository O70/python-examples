# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import element

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

		# c = 0
		for v in typeconts:
			# c += 1
			# if c > 1:
			# 	break

			title = v.find('div', { 'class': 'bookMl' }).string

			content_list = []
			# cc = 0
			for s in v.find_all('span'):
				# cc += 1
				# if cc > 1:
				# 	break
				tag_a = s.find('a')

				sub_soup = self.get_soup(tag_a.attrs['href'])
				# sub_soup = self.get_soup('https://so.gushiwen.org/shiwenv_27166a9a2aa7.aspx')
				cont = (sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
					.find('div', { 'class': 'sons' }).find('div', { 'class': 'cont' }))
				author = cont.find('p', { 'class': 'source' }).get_text()

				paragraphs_list = []

				'''
				1. len(p) == 0
				2. len(p) > 0
				3. p中包含br
				'''
				contson = cont.find('div', { 'class': 'contson' })
				# for kk in contson.children:
				# 	# if type(kk) != bs4.element.NavigableString
				# 	if not isinstance(kk, element.NavigableString):
				# 		print(type(kk))
				# 		print((kk))
				
				if len(contson.find_all('p')) == 0:
					print('%s %d' % (tag_a.string, len(contson.find_all('p'))))

				# if len(contson.find_all('p')) > 0:
				# # print(len(contson.find_all('p')))
				# 	for p in contson.find_all('p'):
				# 		print(tag_a.string)
				# 		paragraphs_list.append(self.replace(p.get_text()))

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

	def get_paragraphs(self, children):
		# def get_string(tag):
		# 	if isinstance(tag, element.NavigableString):
		# 		return tag.string
		# 	else:

		plist = []
		for cs in children:
			if isinstance(cs, element.NavigableString):
				strs = cs.string.strip()
				if len(strs) > 0:
					# print('strs[%s]: %s' % (cs.name, strs))
					# print(strs)
					plist.append(strs)
				# else:
				# 	print('00000: %s' % cs.name)
			else:
				# print(cs.name)
				plist.extend(self.get_paragraphs(cs.children))

		return plist

	def checks(self):
		"""
		INFO:root:https://so.gushiwen.org/shiwenv_ee805a0e1c53.aspx # 寺人披见文公: 0
		INFO:root:https://so.gushiwen.org/shiwenv_c9932c4ec939.aspx # 春王正月: 0
		INFO:root:https://so.gushiwen.org/shiwenv_a53d25ac65fc.aspx # 吴子使札来聘: 0
		INFO:root:https://so.gushiwen.org/shiwenv_a705383d7f48.aspx # 虞师晋师灭夏阳: 0
		INFO:root:https://so.gushiwen.org/shiwenv_8685d24b36b3.aspx # 曾子易箦: 0
		INFO:root:https://so.gushiwen.org/shiwenv_79d7304eaef6.aspx # 晋献文子成室: 0
		INFO:root:https://so.gushiwen.org/shiwenv_734136fefd20.aspx # 鲁共公择言: 0
		INFO:root:https://so.gushiwen.org/shiwenv_2a6f10fb5dec.aspx # 谏逐客书: 0
		INFO:root:https://so.gushiwen.org/shiwenv_20f63f8755a7.aspx # 项羽本纪赞: 0
		INFO:root:https://so.gushiwen.org/shiwenv_4359f64add87.aspx # 孔子世家赞: 0
		INFO:root:https://so.gushiwen.org/shiwenv_c5e1fb9d3e80.aspx # 外戚世家序: 0
		INFO:root:https://so.gushiwen.org/shiwenv_024370e747bc.aspx # 酷吏列传序: 0
		INFO:root:https://so.gushiwen.org/shiwenv_a161c5a3f370.aspx # 景帝令二千石修职诏: 0
		INFO:root:https://so.gushiwen.org/shiwenv_5456a5c04d99.aspx # 武帝求茂才异等诏: 0
		INFO:root:https://so.gushiwen.org/shiwenv_e08287038d66.aspx # 光武帝临淄劳耿弇: 0
		INFO:root:https://so.gushiwen.org/shiwenv_6c1ea9b7dd44.aspx # 陋室铭: 0
		INFO:root:https://so.gushiwen.org/shiwenv_b7ff1ebec1df.aspx # 梓人传: 0
		INFO:root:https://so.gushiwen.org/shiwenv_5164239ca26c.aspx # 谏院题名记: 0
		INFO:root:https://so.gushiwen.org/shiwenv_40c90f9029c1.aspx # 读孟尝君传: 0
		INFO:root:https://so.gushiwen.org/shiwenv_a1ae1e641359.aspx # 司马季主论卜: 0
		"""

		urls = [
			'https://so.gushiwen.org/shiwenv_31e46b58b1ff.aspx', # 郑伯克段于鄢 包含多个p,每个p中仅包含文字

			'https://so.gushiwen.org/shiwenv_27166a9a2aa7.aspx', # 管晏列传 包含多个p,且p包含br和strong

			'https://so.gushiwen.org/shiwenv_ee805a0e1c53.aspx', # 寺人披见文公 仅包含文字
			# 'https://so.gushiwen.org/shiwenv_c9932c4ec939.aspx',
			# 'https://so.gushiwen.org/shiwenv_a53d25ac65fc.aspx',
			# 'https://so.gushiwen.org/shiwenv_a705383d7f48.aspx',
			# 'https://so.gushiwen.org/shiwenv_8685d24b36b3.aspx',
			# 'https://so.gushiwen.org/shiwenv_79d7304eaef6.aspx',
			# 'https://so.gushiwen.org/shiwenv_734136fefd20.aspx',
			# 'https://so.gushiwen.org/shiwenv_2a6f10fb5dec.aspx',
			# 'https://so.gushiwen.org/shiwenv_20f63f8755a7.aspx',
			# 'https://so.gushiwen.org/shiwenv_4359f64add87.aspx',
			# 'https://so.gushiwen.org/shiwenv_c5e1fb9d3e80.aspx',
			# 'https://so.gushiwen.org/shiwenv_024370e747bc.aspx',
			# 'https://so.gushiwen.org/shiwenv_a161c5a3f370.aspx',
			# 'https://so.gushiwen.org/shiwenv_5456a5c04d99.aspx',
			# 'https://so.gushiwen.org/shiwenv_e08287038d66.aspx',
			# 'https://so.gushiwen.org/shiwenv_6c1ea9b7dd44.aspx',
			# 'https://so.gushiwen.org/shiwenv_b7ff1ebec1df.aspx',
			'https://so.gushiwen.org/shiwenv_5164239ca26c.aspx', # 谏院题名记 直接包含文字和br
			# 'https://so.gushiwen.org/shiwenv_40c90f9029c1.aspx',
			# 'https://so.gushiwen.org/shiwenv_a1ae1e641359.aspx'
		]

		for x in urls:
			soup = self.get_soup(x)
			cont = (soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
					.find('div', { 'class': 'sons' }).find('div', { 'class': 'cont' }))
			title = cont.find('h1')
			print('************Title: %s' % title.string)
			contson = cont.find('div', { 'class': 'contson' })
			plist = self.get_paragraphs(contson.children)
			# print(plist)
			self.__data['content'].append({
				'title': title.string,
				'content': plist
			})
			# for s in contson.children:
			# 	# if not isinstance(s, element.NavigableString):
			# 	print(type(s))
			# 	# if isinstance(s, element.NavigableString):

		self.to_json('./jsons/guwenguanzhi.json', self.__data)


fg = FetchGwgz('https://so.gushiwen.org')
fg.checks()
