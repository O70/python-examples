# -*- coding: utf-8 -

import uuid, pinyin, random

def org():
	print('-----------------orgs-----------------')

	sql = "INSERT INTO BASE_ORG(ID, NAME, SHORTNAME, CODE, ISDEL, LEVELCODE, ORGTYPE, PARENTID) VALUES('{id}', '{name}', '{shortname}', '{code}', '{isdel}', '{levelcode}', '{orgtype}', '{parentid}');"
	items = []
	root = {
		'id': str(uuid.uuid1()).replace('-', ''),
		'name': '总院',
		'shortname': '总院',
		'code': 'ZY',
		'isdel': 0,
		'levelcode': '000001',
		'orgtype': 0,
		'parentid': '',
	}

	print(sql.format(**root))

	letters = list(map(chr, range(ord('A'), ord('Z') + 1)))

	orglist = []

	prefix_level2, prefix_level3, prefix_level4 = '分院%s', '所%s', '科室%s'
	for l2 in range(5):
		id2 = str(uuid.uuid1()).replace('-', '')
		name2 = prefix_level2 % letters[l2]
		lc2 = '000001%06d' % (l2 + 1)
		item2 = {
			'id': id2,
			'name': name2,
			'shortname': name2,
			'code': pinyin.get_initial(name2, '').upper(),
			'isdel': 0,
			'levelcode': lc2,
			'orgtype': 1,
			'parentid': root['id'],	
		}
		print(sql.format(**item2))

		for l3 in range(12):
			id3 = str(uuid.uuid1()).replace('-', '')
			name3 = '%s-%s' % (name2, prefix_level3 % letters[l3])
			lc3 = '%s%06d' % (lc2, l3 + 1)
			item3 = {
				'id': id3,
				'name': name3,
				'shortname': name3,
				'code': pinyin.get_initial(name3, '').upper(),
				'isdel': 0,
				'levelcode': lc3,
				'orgtype': 2,
				'parentid': id2,	
			}
			print(sql.format(**item3))

			for l4 in range(7):
				id4 = str(uuid.uuid1()).replace('-', '')
				name4 = '%s-%s' % (name3, prefix_level4 % letters[l4])
				lc4 = '%s%06d' % (lc3, l4 + 1)
				item4 = {
					'id': id4,
					'name': name4,
					'shortname': name4,
					'code': pinyin.get_initial(name4, '').upper(),
					'isdel': 0,
					'levelcode': lc4,
					'orgtype': 4,
					'parentid': id3,	
				}
				print(sql.format(**item4))

				orglist.append({ 'orgid': id2, 'deptid': id3, 'officeid': id4 })

	return orglist

def user(orgs):
	print('-----------------users-----------------')
	# print(len(orgs))

	firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"

	girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
	boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
	names = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

	admin = "INSERT INTO USER_INFO(ID, NAME, EMAIL, EMPSORT, ISSUPERADMIN, LOGINNAME, ORGID, DEPTID, OFFICEID, MOBILEPH, OFFICEPH, NATION, DICTSEX, DICTPOLITICAL, DICTTITLE, BIRTH) VALUES ('xsy', '徐师玉', 'xsy@example.com', 1, 1, 'xsy', '%s', '%s', '%s', '18819037869', '10000', '汉', '402881e5419aab1101419abb28920006', '68d2b7dd-d93c-45d8-8b10-127374680a83', '0fa12f5f-9290-49a3-a777-b9ad82e774e9', TO_DATE('1970-1-1', 'yyyy-MM-dd'));"
	print(admin % (orgs[0]['orgid'], orgs[0]['deptid'], orgs[0]['officeid']))

	sex = ['402881e5419aab1101419abb60f40007', '402881e5419aab1101419abb28920006']

	users, pys, us = [], [], []
	for i in range(511):
		s = random.choice(range(2))
		us.append(sex[s])
		if s > 0:
			name = boy[random.choice(range(len(boy)))]
		else:
			name = girl[random.choice(range(len(girl)))]
		n = '%s%s%s' % (firstName[random.choice(range(len(firstName)))], 
			name, names[random.choice(range(len(names)))])
		users.append(n)
		pys.append(pinyin.get(n, format = 'strip'))

	if len(users) == len(list(set(users))) and len(list(set(users))) == len(list(set(pys))):
		sql = "INSERT INTO USER_INFO(ID, NAME, EMAIL, EMPSORT, ISSUPERADMIN, LOGINNAME, ORGID, DEPTID, OFFICEID, MOBILEPH, OFFICEPH, NATION, DICTSEX, DICTPOLITICAL, DICTTITLE, BIRTH) VALUES ('{id}', '{name}', '{email}', {empsort}, {issuperadmin}, '{loginname}', '{orgid}', '{deptid}', '{officeid}', '{mobileph}', '{officeph}', '{nation}', '{dictsex}', '{dictpolitical}', '{dicttitle}', TO_DATE('1989-6-4', 'yyyy-MM-dd'));"
		for ui in range(len(users)):
			un = users[ui]
			pun = pinyin.get(un, format = 'strip')
			org = orgs[random.choice(range(len(orgs)))]
			item = {
				'id': str(uuid.uuid1()).replace('-', ''), 
				'name': un, 
				'email': '%s@example.com' % pun, 
				'empsort': ui + 2, 
				'issuperadmin': 0, 
				'loginname': pun, 
				'orgid': org['orgid'], 
				'deptid': org['deptid'], 
				'officeid': org['officeid'], 
				'mobileph': str(18790876578 + (ui + 1)), 
				'officeph': str(10000 + (ui + 1)), 
				'nation': '汉', 
				'dictsex': us[ui], 
				'dictpolitical': '68d2b7dd-d93c-45d8-8b10-127374680a83', 
				'dicttitle': '0fa12f5f-9290-49a3-a777-b9ad82e774e9'
			}
			print(sql.format(**item))
	else:
		user(orgs)

# user(org())

def companys():
	levelid = ['d7d7682b-3ffb-4c04-a34c-549463b8ae36', 'f67a57b5-0c2e-4155-86f8-1199e2214973']

	sql = "INSERT INTO BID_COMPANY(ID, CREATE_DATE, CREATE_USER_ID, LEVEL_ID, NAME) VALUES ('%s', TO_DATE('2019-11-16 17:15:11', 'yyyy-MM-dd HH24:mi:ss'), 'xsy', '%s', 'Company-%03d');"

	for x in range(35):
		print(sql % (str(uuid.uuid1()).replace('-', ''), levelid[random.choice(range(2))], x + 1))

companys()
