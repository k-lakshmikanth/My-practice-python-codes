class pi:
	def __init__(self,n,a,d):
		self.name=n
		self.age=a
		self.designation=d
		
	def name1(self):
		print("hello,he is",self.name)
	def age(self):
		print(self.name,"is",self.age,"years old")
	def des1(self):
		print(self.name,"is",self.designation)


obj1=pi("lk",18,"student")
obj2=pi("keerthi",10,"student")

obj1.name1()
pi.age(obj1)
obj1.des1()

print(obj1.name)