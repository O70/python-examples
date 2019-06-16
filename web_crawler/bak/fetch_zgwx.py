# -*- coding: utf-8 -*-

import json, requests
from bs4 import BeautifulSoup, element
from opencc import OpenCC

data = {
	'title': '增广贤文',
	'author': '佚名',
	'abstract': None,
	'content': []
}

url = 'https://so.gushiwen.org'

def get_soup(uri):
	response = requests.get('%s%s' % (url, uri))
	return BeautifulSoup(response.text, "html.parser")

def replace_symbol(txt):
	return txt.strip().replace('.', '。').replace(',', '，').replace('?', '？').replace('!', '！').replace('\n', '')

soup = get_soup('/search.aspx?value=%s' % data['title'])	

abstract = None
try:
	abstract = soup.find('div', { 'class': 'sonspic' }).find('div', { 'class': 'cont' }).find_all('p')[1]
except Exception as e:
	print('Get abstract error: %s' % e)
else:
	data['abstract'] = replace_symbol(abstract.get_text().replace(abstract.find('a').get_text(), ''))

for s in soup.find_all('div', { 'class': 'sons' }):
	sub_soup = get_soup(s.find('a').attrs['href'])
	cont = sub_soup.find('div', { 'class': 'main3' }).find('div', { 'class': 'cont' })
	chapter = cont.find('h1').find('span').find('b').string

	paragraphs_list = []
	paragraphs = cont.find('div', { 'class': 'contson' })
	if not paragraphs.find('p') is None:
		paragraphs = paragraphs.find('p')
	for p in paragraphs:
		p = p.string
		if not p is None and len(p.strip()) > 0:
			paragraphs_list.append(replace_symbol(p))

	print(len(paragraphs_list))			
	data['content'].append({
		'chapter': cont.find('h1').find('span').find('b').string,
		'paragraphs': paragraphs_list
	})

cc = OpenCC('s2t')
with open('./jsons/zengguangxianwen.json', 'w', encoding='utf-8') as file_object:
	json.dump(json.loads(cc.convert(json.dumps(data, ensure_ascii = False))), file_object, sort_keys = False, indent = 2, ensure_ascii = False)
	