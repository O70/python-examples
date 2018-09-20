# with open('doc/pi_digits.txt') as file_object:
# 	print(file_object)
# 	contents = file_object.read()
# 	print(contents.rstrip())

# with open('doc/pi_digits.txt') as file_object:	
# 	for line in file_object:
# 		print(line)

# with open('doc/pi_digits.txt') as file_object:
# 	lines = file_object.readlines()

# print(lines)

# for line in lines: 
# 	print(line.rstrip())

# var = 'guiwang'
# print('gui' in var)
# print('guia' in var)

# with open('doc/hello.txt', 'w') as file_object:
# 	file_object.write("Hello guiwang2!\n")
# 	# print(file_object.read())

# with open('doc/hello.txt', 'a') as file_object:
# 	file_object.write('Welcome!\n')
# 	file_object.write('Welcome2!\n')
# 	file_object.write('Welcome3!\n')
# 	print(file_object.read())

# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You Cant't divide by zero!")	

try:
	answer = 5 / 0
except:
	print("You Cant't divide by zero!")
else:
	print(answer)	