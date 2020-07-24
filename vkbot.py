import vk
import time

s = vk.Session(access_token='9f747a4c1f7dab6100d6193df545fd97ed74c6dca8cf82b58a6343d2bc9e51b0f19f1076f54d0aeb4d735')
api = vk.API(s, v='5.120', lang='ru', timeout=10)

def getIds(memberlist: list, sleppt):
	finallist = []
	for i in memberlist:
		a = api.users.get(user_ids=i)
		a = a[0].get('id')
		finallist.append(a)
		time.sleep(sleppt)
	return finallist

fname = input("Введите имя файла с аккаунтами вк: ")
count = input("Введите кол-во получаемых id: ")
slepptime = int(input('Введите время между запросами (по умолчанию - 3 секунды): '))

idsarr = []

try:	

	print(f'Примерное время работы: ~ {len(idsarr)+1 * slepptime * 2} секунд ({round((len(idsarr)+1) * slepptime / 60, 2)} мин.)')
	
	with open(f'{fname}.txt', 'r') as f:
		for i in f:
			a = i.strip()
			a = a.split('/')
			idsarr.append(a[3])

	idsarr = getIds(idsarr, slepptime)

	with open(f'parsed - {time.time()}.txt', 'w') as f:
		for i in idsarr:
			d = api.groups.get(user_id=i, count=count, extended=1)
			d = d.get('items')
			for j in d:
				f.write(f"https://vk.com/public{j.get('id')}" + '\n')
			time.sleep(slepptime)

except Exception as e:
	print(f'Ошибка! - {e}')
	raise


