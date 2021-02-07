# -*- coding: utf-8 -*-

import os, time

def export(dict_path, html_name):
	with open('./tmp.result/' + dict_path) as f:
		keywords = [line.strip() for line in f.readlines()]

	def find(lines):
		locations = []
		for ind, line in enumerate(lines):
			for kw in keywords: 
				if line.find(kw) > -1:
					locations.append({
						'line': ind + 1,
						'text': line,
						'name': kw
					})
		return locations

	contents = []
	counter = 0
	t0 = time.process_time()
	for parent, dirnames, filenames in os.walk('./tmp.plain'):
		for fname in filenames:
			with open('%s/%s' % (parent, fname)) as f:
				locations = find(f.readlines())
				if locations:
					mt = len(locations)
					counter += mt
					contents.append('<div class="table-card">')
					
					contents.append('<h2 class="table-name">Table: %s (<label>%d</label>)</h2>' % (fname.replace('.txt', ''), mt))
					# contents.append('<div class="table-matched">Matched: %d</div>' % mt)
					for loc in locations:
						contents.append('<div class="matched-block">')

						contents.append('<div class="location">Location: <label>%s</label> </div>' % loc['line'])
						contents.append('<div class="keyword">Name: <label>%s</label> </div>' % loc['name'])
						contents.append('<div class="record">%s</div>' 
							% loc['text'].replace(loc['name'], '<label>%s</label>' % loc['name']))

						contents.append('</div>')

					contents.append('</div>')

	contents.insert(0, '<h1><label>%d</label> records were matched</h1>' % counter)

	with open('./index.html') as f: temp = f.read()
	# with open('./tmp.result/check.txt') as f: content = f.read()
	with open('./tmp.result/%s.html' % html_name, 'wt') as f:
		# f.write(temp.replace('#{content}', content))
		f.writelines(temp.replace('#{content}', '\n'.join(contents)))
	print('it took %.6fs in total' % time.process_time() - t0)

export('dicts.bak', 'index')
export('dicts', 'index-v2')
