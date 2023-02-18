from color import Color

# Resolutions & Dimensions
MatrixDimensions = (10, 20)
ScreenResolution = (500, 600)
BlockSize = 25

# Shapes
IShape = "I"
LShape = "L"
RShape = "R"
SShape = "S"
ZShape = "Z"
TShape = "T"
OShape = "O"

ShapesList = [
	IShape,
	LShape,
	RShape,
	SShape,
	ZShape,
	TShape,
	OShape ]

# Colors
IColor = 		Color((0, 	255, 	255), 	"C") # Cyan
LColor = 		Color((255, 127, 	0), 	"O") # Orange
RColor = 		Color((0, 	0, 		255), 	"B") # Blue
SColor = 		Color((0, 	255, 	0), 	"G") # Green
ZColor = 		Color((255, 0, 		0), 	"R") # Red
TColor = 		Color((128, 0, 		128), 	"P") # Purple
OColor = 		Color((255, 255, 	0), 	"Y") # Yellow
BlackColor = 	Color((0, 	0, 		0), 	"#") # Black
WhiteColor = 	Color((255, 255, 	255), 	"@") # White

# ColorDictionary
ColorDictionary = {	IShape: IColor,
					LShape: LColor,
					RShape: RColor,
					SShape: SColor,
					ZShape: ZColor,
					OShape: OColor,
					TShape: TColor	}

ColorList = [	IColor,
				LColor,
				RColor,
				SColor,
				ZColor,
				TColor,
				OColor ]
