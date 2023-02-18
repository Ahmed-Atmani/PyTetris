from telnetlib import GA
from matrix import Matrix
from myqueue import MyQueue
from constants import *
from shapes import *
from random import randrange

class Game:
	def __init__(self, rows=10, columns=20):
		self.Matrix = Matrix(rows, columns)
		self.ShapeOnHold = Shape()
		self.CurrentShape = Shape()
		self.NextShapes = MyQueue()
		self.LinesCleared = 0
		self.SwappedHold = False # True if item was swapped
		self.ReadyToFreeze = False # True if piece has block under AND hasn't moved

		self.InitInterface()

	def GameLoop(self):
		if self.ReadyToFreeze:
			self.PlaceShape()
			return
		
		self.MoveShapeDown()

	def StartGame(self):
		pass

	def HasBlockUnder(self):
		pass

	def InitInterface(self):
		for i in range(3):
			self.EnqueueNewShape()
		self.ServeShape()

	def ServeShape(self):
		self.CurrentShape = self.NextShapes.Serve()
		self.EnqueueNewShape()
	
	def PlaceShape(self):
		for row in range(len(self.CurrentShape.GetCurrentOrientation())):
			for col in range(len(self.CurrentShape.GetCurrentOrientation()[row])):
				if self.CurrentShape.GetCurrentOrientation()[row][col] == 1:
					self.Matrix.SetElement	(col + self.CurrentShape.Position.X,
											 row + self.CurrentShape.Position.Y,
											 self.CurrentShape.ShapeName)
		self.SwappedHold = False
		self.ServeShape()

	def EnqueueNewShape(self):
		def GetNewShape():
			letter = ShapesList[randrange(0, len(ShapesList))]
			res = None
			
			if letter == OShape:
				res = O_Shape()
			elif letter == SShape:
				res = S_Shape()
			elif letter == ZShape:
				res = Z_Shape()
			elif letter == IShape:
				res = I_Shape()
			elif letter == LShape:
				res = L_Shape()
			elif letter == RShape:
				res = R_Shape()
			elif letter == TShape:
				res = T_Shape()
			else:
				print("Wrong letter (interface/EnqueueNewShape/GetNewShape)")

			return res
			
		self.NextShapes.Enqueue(GetNewShape())
	
	def SwapWithHold(self):
		if self.SwappedHold:
			return

		temp = self.ShapeOnHold
		self.ShapeOnHold = self.CurrentShape
		self.CurrentShape = temp
		# * set temp.position to init *
		self.CurrentShape.Position = self.CurrentShape.InitPosition
		# restart dropdown
	
	def IncrementLinesCleared(self):
		self.LinesCleared += 1
		# render text

	def RotateShape(self, direction):
		if direction == "R":
			self.CurrentShape.RotateClockwise()
			self.ReadyToFreeze = False
		elif direction == "L":
			self.CurrentShape.RotateCounterClockwise()
			self.ReadyToFreeze = False
		else:
			print(f"Wrong Rotate direction, expected \"R\" or \"L\", given: \"{direction}\"\n(game.py/RotateShape)")

		### CHANGE POSITION OF PIECE IF PIECEMATRIX OUT OF BOUNDARIES

	def MoveShapeUp(self):
		self.CurrentShape.MoveUp()
		self.ReadyToFreeze = False # optional?
		
	def MoveShapeDown(self):
		self.CurrentShape.MoveDown()
		if self.HasBlockUnder():
			self.ReadyToFreeze = True
	
	def MoveShapeRight(self):
		### ONLY MOVE IF IN BOUNDARIES
		self.CurrentShape.MoveRight()
		self.ReadyToFreeze = False

	def MoveShapeLeft(self):
		### ONLY MOVE IF IN BOUNDARIES
		self.CurrentShape.MoveLeft()
		self.ReadyToFreeze = False

