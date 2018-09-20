
[TOC]

__Python2与Python3区别：__

- `print`
- `/`
- `input`
- `class ClassNmae(object)` , P140
- Inherit `super(SubClassName, self)`/`super()`, P149

## Chapter 2 Variables and simple data types

__String__

- str.title()
- \n\t
- str.[strip() | rstrip() | lstrip()]
- `str in strs`

## Chapter 3 List

__List__

- first: 0, last: -1
- `list.append(val)`
- `list.insert(index, val)`
- `del list[index]`
- `list.pop(null | index)`
- `list.remove(val)`

__Group List__

- `list.sort(null | reverse = True)`，永久性排序，默认还首字母排序
- `sorted(list, null | reverse = True)`，临时排序
- `list.reverse()`，永久性反转
- `len(list)`

## Chapter 4 Operation List

```python
magicians = ['alice', 'david', 'carolina']

for m in magicians:
	print(m)

print(m)
```

__变量`m`会被提升__

`indent`: 语法错误 / 逻辑错误

__Number List__

- range(1, 5, null | step), [1, 5)
```python
for val in range(1, 5):
	print(val)
```
- `list(rang(1, 5))`
- `min(<Number List>)`
- `max(<Number List>)`
- `sum(<Number List>)`

__列表解析__
```python
squ = [val**2 for value in range(1, 11)]
print(squ)
```

__切片__
```python
nums = [1, 2, 3, 4, 5]
print(nums[0:3])
```


__tuple__
```python
n = (2, 4, 6)
```

`tuple`和`list`非常类似，但是`tuple`一旦初始化就不能修改。
可以给`tuple`重新赋值，但是不能修改`tuple`的元素值。

## Chapter 5 if

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
```

- `and`(&&)
- `or`(||)
- `val in list`
- `val not in list`

## Chapter 6 Dict

```python
n = { 'id': '1', 'name': 'HANZO' }
print(n)
print(n['id'])
print(n.get('id'))

del n['id']

for key, value in n.items():
	print(key)
	print(value)
```

- `dict.items()`
- `dict.keys()`，获取键，可省略
- `dict.values()`
- `set(list)`，去除重复值

## Chpater 7 Input And While

- `input()` and `raw_input()`

## Chapter 8 Function

```python
def greet_user():
	"""Hello"""
	print("Hello")

greet_user()	
```

- 位置实参
- 关键字实参
- 默认值

__Module__

- `import module_name`
- `from module_name import function_name[, function_name1, function_name2]`
- `from module_name import function_name as function_alias_name`
- `import module_name as module_alias_name`
- `from module_name import *`

## Chapter 9 Class

- 首字母大写，驼峰命名
- 实例名和模块名采用小写，并在单词之间加下划线
- `class`中的`function`称为`method`
- `__init(self)__`, `self`只想实例本身的引用

```python
class Dog(): # Python2.7: class Dog(object):

	def __init__(self):
		pass
```

__Inherit__

__Import Class__

- `form module_name import ClassName`
- `form module_name import ClassName1, ClassName2, ...`
- `import module_name`
- `from module_name import *`
- 一个`module`中可以有多个`class`

## Chapter 10 File And Exception

__File__

```py
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
```

```py
with open('doc/pi_digits.txt') as file_object:	
	for line in file_object:
		print(line)
```

```py
with open('doc/pi_digits.txt') as file_object:
	lines = file_object.readlines()

print(lines)

for line in lines: 
	print(line.rstrip())
```

```py
# write-only
with open('doc/hello.txt', 'w') as file_object:
	file_object.write("Hello guiwang!\n")
```

```py
# read and write
with open('doc/hello.txt', 'r+') as file_object:
	file_object.write("Hello guiwang!\n")
	print(file_object.read())
```

- `open()`会创建不存在的文件或覆盖
- `r`读取模式，default
- `w`写入模式，文件不存在则创建，覆盖式写入
- `a`附加模式，末尾追加内容，`read-only`
- `r+`读写模式

__Exception__

```py
try:
	print(5/0)
except ZeroDivisionError:
	print("You Cant't divide by zero!")	
```

```py
try:
	answer = 5 / 0
except:
	print("You Cant't divide by zero!")
else:
	print(answer)			
```

__`else`依赖于`try`代码块成功执行__