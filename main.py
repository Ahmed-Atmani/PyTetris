from draw import Draw
from constants import *
import pygame
from pygame.locals import *

from game import Game


def MainLoop():
	RUN = True
	FPS = 60
	CLOCK = pygame.time.Clock()
	pygame.key.set_repeat(500, 500)

	### DRAW UPDATE
	
	def RedrawDisplay():
		# window.blit(object, (x, y))
		
		DRAW.UpdateDraw()

		for row in range(len(DRAW.TilesMatrix.TilesMatrix.Matrix)):
			for col in range(len(DRAW.TilesMatrix.TilesMatrix.Matrix[row])):
				WINDOW.blit(WINDOW, DRAW.TilesMatrix.TilesMatrix.Matrix[row][col],
							[col * BlockSize, row * BlockSize, BlockSize, BlockSize])

		pygame.display.update()

	### RUN UPDATE

	TimeInterval = 1000
	timeCounter = 0

	while RUN:
		CLOCK.tick(FPS)

		passedTime = CLOCK.get_time()
		timeCounter += passedTime
		if timeCounter >= TimeInterval:
			timeCounter -= TimeInterval
			DRAW.GAME.GameLoop()
			RedrawDisplay()


		for Event in pygame.event.get():
			if Event.type == pygame.QUIT: # QUIT
				RUN = False
			if Event.type == pygame.KEYDOWN:
				if Event.key == K_UP: # quick falldown
					# print("UP Pressed!")
					pass
				elif Event.key == K_DOWN: # move down
					DRAW.GAME.MoveShapeDown()
					# print("DOWN Pressed!")
				elif Event.key == K_LEFT: # move left
					DRAW.GAME.MoveShapeLeft()
					# print("LEFT Pressed!")
				elif Event.key == K_RIGHT: # move right
					DRAW.GAME.MoveShapeRight()
					# print("RIGHT Pressed!")
				elif Event.key == K_RSHIFT: # rotate CW
					DRAW.GAME.RotateShape("R")
					# print("RSHIFT Pressed!")
				elif Event.key == K_RCTRL: # rotate CCW
					DRAW.GAME.RotateShape("L")
					# print("RCTRL Pressed!")
				elif Event.key == K_p:
					DRAW.GAME.PlaceShape()
					# print("P Pressed!")
				
			RedrawDisplay()

			
		# RedrawDisplay()
		
		# pygame.draw.rect(WINDOW, WhiteColor.Value, [400, 300, 50, 25])


# SETUP WINDOW
WINDOW = pygame.display.set_mode(ScreenResolution)
pygame.display.set_caption("pyTetris by Ahmed")
WINDOW.fill(WhiteColor.Value)

# START GAME
DRAW = Draw(WINDOW)
DRAW.GAME.StartGame()




# ### DEBUG ###

# # DEBUG Piece 1
# for i in range(4):
# 	DRAW.GAME.MoveShapeDown()
# DRAW.GAME.CurrentShape.RotateClockwise()
# DRAW.GAME.PlaceShape()

# # DEBUG Piece 2
# for i in range(9):
# 	DRAW.GAME.MoveShapeDown()
# for i in range(3):
# 	DRAW.GAME.MoveShapeLeft()
# DRAW.GAME.CurrentShape.RotateCounterClockwise()
# DRAW.GAME.PlaceShape()

# # DEBUG Print Matrix
# DRAW.GAME.Matrix.PrintMatrix()

MainLoop()
