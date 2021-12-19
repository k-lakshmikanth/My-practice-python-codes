class A:
	def __init__(self):
		print("This is init of A")
	
	def feature1(self):
		print("This is feature1")
	def feature2(self):
		print("This is feature2")
		
class B(A):
	def __init__(self):
	#super(). calls Method from class A-------------------------------------------------------------
		super().__init__()
	#-----------------------------------------------------------------------------------------------
		print("This is init of B")
	def feature3(self):
		print("This is feature3")
	def feature4(self):
		print("This is feature4")	
		
		
b1 = B()

