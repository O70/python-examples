
class Dog():
	"""一次模拟小狗的简单尝试"""

	def __init__(self, name, age):
		"""Initial params"""
		self.name = name
		self.age = age

	def sit(self):
		"""蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""打滚"""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print(my_dog.name.title())
print(my_dog.age)

my_dog.sit()
my_dog.roll_over()