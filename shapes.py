from constants import *
from shapebase import Shape
from position import Position

class I_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = IShape
		self.Color = IColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 0, 0, 0],
				[1, 1, 1, 1],
				[0, 0, 0, 0],
				[0, 0, 0, 0]	],
			
			[	[0, 0, 1, 0],
				[0, 0, 1, 0],
				[0, 0, 1, 0],
				[0, 0, 1, 0]	],

			[	[0, 0, 0, 0],
				[0, 0, 0, 0],
				[1, 1, 1, 1],
				[0, 0, 0, 0]	],

			[	[0, 1, 0, 0],
				[0, 1, 0, 0],
				[0, 1, 0, 0],
				[0, 1, 0, 0]	]
		]

class L_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = LShape
		self.Color = LColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1, 0],
				[0, 1, 0],
				[0, 1, 1]	],

			[	[0, 0, 0],
				[1, 1, 1],
				[1, 0, 0]	],

			[	[1, 1, 0],
				[0, 1, 0],
				[0, 1, 0]	],

			[	[0, 0, 1],
				[1, 1, 1],
				[0, 0, 0]	]
		]


class R_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = RShape
		self.Color = RColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1, 0],
				[0, 1, 0],
				[1, 1, 0]	],

			[	[1, 0, 0],
				[1, 1, 1],
				[0, 0, 0]	],

			[	[0, 1, 1],
				[0, 1, 0],
				[0, 1, 0]	],

			[	[0, 0, 0],
				[1, 1, 1],
				[0, 0, 1]	]
		]

class T_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = TShape
		self.Color = TColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1, 0],
				[0, 1, 1],
				[0, 1, 0]	],

			[	[0, 0, 0],
				[1, 1, 1],	
				[0, 1, 0]	],

			[	[0, 1, 0],
				[1, 1, 0],
				[0, 1, 0]	],


			[	[0, 1, 0],
				[1, 1, 1],
				[0, 0, 0]	]
		]

class S_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = SShape
		self.Color = SColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[0, 1, 1],	
				[1, 1, 0],
				[0, 0, 0]	],
				
			[	[0, 1, 0],
				[0, 1, 1],
				[0, 0, 1]	],

			[	[0, 0, 0],
				[0, 1, 1],	
				[1, 1, 0]
							],
				
			[	[1, 0, 0],
				[1, 1, 0],
				[0, 1, 0]	],
		]

class Z_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = ZShape
		self.Color = ZColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 1, 0],	
				[0, 1, 1],
				[0, 0, 0]	],
				
			[	[0, 0, 1],
				[0, 1, 1],
				[0, 1, 0]	],

			[	[0, 0, 0],
				[1, 1, 0],	
				[0, 1, 1]
							],
				
			[	[0, 1, 0],
				[1, 1, 0],
				[1, 0, 0]	],
		]

class O_Shape(Shape):

	def __init__(self ):
		super().__init__( )
		self.ShapeName = OShape
		self.Color = OColor
		self.InitOrientations()

	def InitOrientations(self):
		self.Orientations = [

			[	[1, 1],
				[1, 1]	]
		]
