class student:
	#class/static variable
	school="iitt"
	#m1,m2,m3 are instance variables
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	#instance variable
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	
	@classmethod
	def scl(cls):
		return cls.school

	@staticmethod
	def info():
		print("This won't do anything but still needs an object before it")
	
s1=student(29,45,24)
s2=student(74,23,31)

print(s1.avg())
print(student.scl())
student.info()