from game import Game
from tilesmatrix import TilesMatrix
from constants import *
import pygame

class Draw:
	def __init__(self, Window):
		self.GAME = Game()
		self.Window = Window
		self.TilesMatrix = TilesMatrix(self.Window, self.GAME)

	def InitDraw(self):
		pass

	def UpdateDraw(self):
		self.TilesMatrix.UpdateTilesMatrix()
		self.TilesMatrix.AddCurrentShape()
	
	def UpdateDrawQueue(self):
		pass

	def DrawBlock(self, row, col, color):
		pass
