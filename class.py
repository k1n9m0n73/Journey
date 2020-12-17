class person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def my_func(self):
		print("information about ", self.name)


p1 = person("joe", 26, "male")

p1.my_func()
print()

def info():
	print("name: " + p1.name)
	print("sex: " + p1.sex)
	age = p1.age
	txt = "age: {}"
	print(txt.format(age))

info()
print()

#p1.age = 23
#info()

p2 = person("lilly", 24, "female")

p2.my_func()
print()

def info1():
	print("name: ", p2.name)
	print("sex: ", p2.sex)
	print("age: ", p2.age)

info1()
print()

class student(person):
	def __init__(self, name, age, sex, year):
		super().__init__(name, age, sex)
		self.graduationyear = year
	def my_message(self):
		print(self.name, " a", self.age," years old ", self.sex, " just graduated with the class of", self.graduationyear)


s1 = student("mike", 19, "male", 2017)
s1.my_func()
s1.my_message()

