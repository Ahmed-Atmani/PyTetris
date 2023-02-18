class MyQueue:
	def __init__(self):
		self.Elements = []

	def Enqueue(self, value):
		self.Elements += [value]

	def Serve(self):
		temp = self.Elements[0]
		self.Elements = self.Elements[1 : len(self.Elements)]
		
		return temp
		