from position import Position
from color import Color

class Shape:

	def __init__(self):
		self.ShapeName = ""
		self.Position = self.InitPosition = Position(5, 0)
		self.Orientations = []
		self.CurrentOrientation = 0
		self.Color = Color()

	def MoveUp(self):
		self.Position.Add(0, -1)
	def MoveDown(self):
		self.Position.Add(0, 1)

	def MoveRight(self):
		self.Position.Add(1, 0)
	def MoveLeft(self):
		self.Position.Add(-1, 0)

	def RotateClockwise(self):
		self.CurrentOrientation = (self.CurrentOrientation + 1) % len(self.Orientations)
		# Check if shape doesn't go through borders of the interface
		
	def RotateCounterClockwise(self):
		self.CurrentOrientation = (self.CurrentOrientation - 1) % len(self.Orientations)
		# Check if shape doesn't go through borders of the interface

	def GetCurrentOrientation(self):
		return self.Orientations[self.CurrentOrientation]
	
	def PrintShape(self):
		temp = ""
		for row in range(len(self.Orientations[self.CurrentOrientation])):
			for col in range(len(self.Orientations[self.CurrentOrientation][row])):
				if self.Orientations[self.CurrentOrientation][row][col] == 0:
					temp += " "
				else:
					temp += self.Color.ColorChar
			temp += "\n"
		
		print(temp)
