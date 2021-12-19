class notepad:
	def execute(self):
		print("This is notepad++")

class pycharm:
	def execute(self):
		print("This is pycharm")

class laptop:
	def code(self,ide):
		ide.execute()


ide=pycharm()

lap1=laptop()

lap1.code(ide)