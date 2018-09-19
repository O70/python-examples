# print("Hello Python world");

# message = "Hello Python world!"
# print(message)

# message = "Hello Python Crash Course world!"
# print(mesage)

# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
# 	if car == 'bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())

# n = { 'id': '1', 'name': 'HANZO' }
# print(n)
# print(n['id'])
# print(n.get('id'))

# del n['id']
# print(n)

# for key, value in n.items():
# 	print(key)
# 	print(value)

# for key in n.keys():
# 	print(key)

# for key in n:
# 	print(key)
	# print(val)

# print(n.keys())

# staff = []

# for s in range(30):
# 	staff.append({ 'id': 1, 'name': 'HANZO' })

# for s in staff:
# 	print(s)
# print(staff)

# message = input("Tell me: ")
# print(message)

# n = ""

def greet_user(*p):
	"""Hello"""
	print("Hello")
	print(p)
	return 1

n = greet_user(1, '123')	
print(n)
