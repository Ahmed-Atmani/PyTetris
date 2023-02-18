class Position:
	def __init__(self, x=0, y=0):
		self.X = x
		self.Y = y
	
	def __str__(self) -> str:
		return f"[ {self.X} ; {self.Y} ]"
	
	def Add(self, *args):
		if isinstance(args[0], Position):
			self.X += args[0].X
			self.Y += args[0].Y
		elif (	len(args) == 2
			and	isinstance(args[0] ,int)
			and isinstance(args[1] ,int)):
			self.X += args[0]
			self.Y += args[1]
		else:
			print("wrong arguments (Position/Add)")

	def Factor(self, *args):
		if len(args) == 1:
			self.X *= args[0]
			self.Y *= args[0]
		elif len(args) == 2:
			self.X *= args[0]
			self.Y *= args[1]
		else:
			print("wrong arguments (Position/Factor)")
