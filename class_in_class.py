class student:
	school="iitt"
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		self.lap = self.laptop()

	def show(self):
		print(self.name,self.rollno)
		self.lap.show()
	
	class laptop:
		def __init__(self):
			self.brand = "dell"
			self.series = "latitude"
			self.model = "e6320"
			self.processor = "i5"
			self.ram = "4gb"
		
		def show(self):
			print(self.brand,self.series,self.model,self.processor,self.ram)
		
		
s1=student("Lakshmikanth",4)
s2=student("lk",21)

s1.show()

s2.show()