# types of methods
	# instance methods
		# methods that access instance variables
		# self sshould be th efirst parameter
		# accessed by using self insede the class and by 
		# using object name outside the class

	
	# class method 
		# method that access static/class-level variables
		# cls should be the first parameter
		# accessed by using class name inside and outsied the class
		# @classmethod decorartor is required

# static method
# methods that do not access static/instance variables
# can be parameterless or parameterized 
# accessed by using class name both inside and outside the class
# @staticmethod decorator is required


class student:
	__school_name = 'sunway'
	__school_address = 'maitidevi'
	def __init__(self, fn , ln, addr, a):
		self.first_name = fn
		self.last_name = ln
		self.addrerss = addr
		self.__age = a

	def get_full_name(self):
		return f'{self.first_name} {self.last_name}'
	

	@classmethod
	def get_school_name(cls):
		return cls.__school_name
	
	@staticmethod
	def add(i, j):
		print(i+j)
	
	def get_first_name(self):
		return self.__first_name
	
	def get_age(self):
		return self.__age
	
	def set_age(self, new_age):
		if new_age < 0:
			print('Age cannot be less then zero')
		else:
			self.__age = new_age

s = student('ram', 'hari', 'ktm', 30)
print(student.get_school_name())
student.add(3,4)
s.set_age(-10)
print(s.get_age())
