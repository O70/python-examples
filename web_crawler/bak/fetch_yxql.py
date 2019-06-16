# -*- coding: utf-8 -*-

from fetch_utils import FetchUtils

data = {
	'title': '幼学琼林',
	'author': '程登吉',
	'abstract': None,
	'content': []
}

fu = FetchUtils()
soup = fu.get_soup('https://so.gushiwen.org/search.aspx?value=幼学琼林')
abstract = soup.find('div', { 'class': 'sonspic' }).find('div', { 'class': 'cont' }).find_all('p')[1]

a = abstract.get_text().replace(abstract.find('a').get_text(), '')
# print(fu.replace(a))


import re

s = '人之初，性本善，性相近，習相遠。'
a = re.match(r'[，]', s)

print(a)
# print(a.groups())
print(type(a))

print(re.sub(r'[，]', ',', s))
print(re.sub(r'[。]', '.', s))