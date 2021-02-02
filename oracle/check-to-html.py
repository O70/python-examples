# -*- coding: utf-8 -*-

import os, time

with open('./tmp.result/dicts') as f:
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
				
				contents.append('<h2 class="table-name">Table: %s</h2>' % fname.replace('.txt', ''))
				contents.append('<div class="table-matched">Matched: %d</div>' % mt)
				for loc in locations:
					contents.append('<div class="matched-block">')

					contents.append('<div class="keyword">Name: <label>%s</label> </div>' % loc['name'])
					contents.append('<div class="location">Location: <label>%s</label> </div>' % loc['line'])
					contents.append('<div class="record">%s</div>' 
						% loc['text'].replace(loc['name'], '<label>%s</label>' % loc['name']))

					contents.append('</div>')

				contents.append('</div>')

contents.insert(0, '<div class="tips"><label>%d</label> records were matched, it took <label>%.6fs</label> in total </div>' 
	% (counter, time.process_time() - t0))

with open('./index.html') as f: temp = f.read()
# with open('./tmp.result/check.txt') as f: content = f.read()
with open('./tmp.result/index.html', 'wt') as f:
	# f.write(temp.replace('#{content}', content))
	f.writelines(temp.replace('#{content}', '\n'.join(contents)))

