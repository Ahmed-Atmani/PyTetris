from constants import *
from shapebase import Shape
from position import Position

class I_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = IShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 1, 1, 1]	],

			[	[1],
				[1],
				[1],
				[1]	]
		]

class L_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = LShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 0],
				[1, 0],
				[1, 1]	],

			[	[1, 1, 1],
				[1, 0, 0]	],

			[	[1, 1],
				[0, 1],
				[0, 1]	],

			[	[0, 0, 1],
				[1, 1, 1]	]
		]


class R_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = RShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1],
				[0, 1],
				[1, 1]	],

			[	[1, 0, 0],
				[1, 1, 1]	],

			[	[1, 1],
				[1, 0],
				[1, 0]	],

			[	[1, 1, 1],
				[0, 0, 1]	]
		]

class T_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = TShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 0],
				[1, 1],
				[1, 0]	],

			[	[1, 1, 1],	
				[0, 1, 0]	],

			[	[0, 1],
				[1, 1],
				[0, 1]	],


			[	[0, 1, 0],
				[1, 1, 1]	]
		]

class S_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = SShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 0],
				[1, 1],
				[0, 1]	],

			[	[0, 1, 1],	
				[1, 1, 0]	]
		]

class Z_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = ZShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1],
				[1, 1],
				[1, 0]	],

			[	[1, 1, 0],	
				[0, 1, 1]	]
		]

class O_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = OShape
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 1],
				[1, 1]	]
		]
