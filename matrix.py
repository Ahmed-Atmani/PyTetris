class Matrix:
	def __init__(self, rows, columns, matrix=None):
		self.Rows = rows
		self.Columns = columns
		if matrix == None:
			self.Matrix = [ [0]*rows for i in range(columns) ]
		else:
			self.Matrix = matrix
	
	def GetElement(self, X, Y):
		return self.Matrix[Y][X]

	def SetElement(self, X, Y, value):
		self.Matrix[Y][X] = value

	def PrintMatrix(self):
		temp = ""
		for col in range(self.Columns):
			for row in range(self.Rows):
				temp += str(self.GetElement(row, col)) + " "
			temp += "\n"
		
		print(temp)

	def PrintMatrixDebug(self):
			temp = ""
			for col in range(self.Columns):
				for row in range(self.Rows):
					if self.GetElement(row, col) == 0:
						temp += '- '
					else:
						temp += str(self.GetElement(row, col)) + " "
				temp += "\n"
			
			print(temp)
