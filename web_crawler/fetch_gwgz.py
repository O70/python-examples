# -*- coding: utf-8 -*-

from fetch_util import FetchUtil
from bs4 import element

class FetchGwgz(FetchUtil):
	def __init__(self, url):
		super(FetchGwgz, self).__init__(url)
		self.__data = {
			'title': '古文观止',
			'abstract': [
				'《古文观止》是清人吴楚材、吴调侯于康熙三十三年（1694年）选定的古代散文选本。二吴均是浙江绍兴人，长期设馆授徒，该书是清朝康熙年间选编的一部供学塾使用的文学读本，此书是为学生编的教材。',
				'《古文观止》收自东周至明代的文章222篇，全书12卷，以收散文为主，兼取骈文。题名“观止”是指该书所选的都是名篇佳作，是人们所能读到的尽善尽美的至文了。',
				'《古文观止》由清代吴兴祚审定并作序，序言中称“以此正蒙养而裨后学”，当时为读书人的启蒙读物。康熙三十四年（1695年）正式镌版印刷。'
			],
			'content': []
		}

	def processing(self):
		soup = self.get_soup('/search.aspx?value=%s' % self.__data['title'])
		self.set_content(soup)
		self.to_json('./jsons/guwenguanzhi.json', self.__data)

	def set_content(self, soup):
		typeconts = (soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
			.find('div', { 'class': 'sons' }).find_all('div', { 'class': 'typecont' }))

		vlen = 0
		for v in typeconts:
			title = v.find('div', { 'class': 'bookMl' }).string

			content_list = []
			tag_span = v.find_all('span')
			vlen += len(tag_span)
			for s in tag_span:
				tag_a = s.find('a')

				sub_soup = self.get_soup(tag_a.attrs['href'])
				cont = (sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'left' })
					.find('div', { 'class': 'sons' }).find('div', { 'class': 'cont' }))
				author = cont.find('p', { 'class': 'source' }).get_text()

				paragraphs_list = []

				'''
				1. 郑伯克段于鄢 包含多个p,每个p中仅包含文字
				2. 管晏列传 包含多个p,且p包含br和strong
				3. 寺人披见文公 仅包含文字
				4. 谏院题名记 直接包含文字和br
				'''
				contson = cont.find('div', { 'class': 'contson' })

				content_list.append({
					'chapter': tag_a.string,
					'source': s.get_text().replace(tag_a.string, ''), 
					'author': author,
					'paragraphs': self.get_paragraphs(contson.children)
				})

			self.__data['content'].append({
				'title': title,
				'content': content_list
			})

		self.logging.info('%s 共%d卷 %d篇' % (self.__data['title'], len(typeconts), vlen))

	def get_paragraphs(self, children):
		plist = []
		for cs in children:
			if isinstance(cs, element.NavigableString):
				strs = cs.string.strip()
				if len(strs) > 0:
					plist.append(strs)
			else:
				plist.extend(self.get_paragraphs(cs.children))

		return plist

	# Deprecated	
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


# fg = FetchGwgz('https://so.gushiwen.org')
# fg.checks()
