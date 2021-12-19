class a:
	def show(self):
		print("class a show")
		
class b(a):
	def show(self):									#-|this method overrid method show in class a
		print("class b show")						#_|because b had its own show

b1=b()
b1.show()