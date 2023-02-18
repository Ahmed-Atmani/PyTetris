from random import randrange
from position import Position
from matrix import Matrix
from constants import *
from color import Color
import pygame

""" when drawing a tile, make sure to change the color to the color of the shape
"""

class TilesMatrix:
	def __init__(self, window, game, rows=10, columns=20):
		self.TilesMatrix = Matrix(rows, columns)
		self.Window = window
		self.Game = game
		self.GridPosition = Position((0, 0))
		self.UpdateTilesMatrix()

	def GetColor(self, char):
		if isinstance(char, str):
			return ColorDictionary[char].Value
		return BlackColor.Value

	def GetRect(self, row, col):
		return pygame.draw.rect(self.Window,
								self.GetColor(self.Game.Matrix.Matrix[row][col]),
								[	col * BlockSize, 
									row * BlockSize, 
									BlockSize,
									BlockSize])

	def UpdateTilesMatrix(self):
		for row in range(len(self.TilesMatrix.Matrix)):
			for col in range(len(self.TilesMatrix.Matrix[row])):
				self.TilesMatrix.SetElement(col, 
											row,
											self.GetRect(row, col))

	def AddCurrentShape(self):
		current = self.Game.CurrentShape
		xOffset = current.Position.X
		yOffset = current.Position.Y
		color = current.Color.Value
		currentMatrix = current.GetCurrentOrientation()
		rows = len(currentMatrix)
		cols = len(currentMatrix[0])
		
		for row in range(rows):
			for col in range(cols):
				if currentMatrix[row][col] == 1: # to avoid overlapping black over existing shape
					self.TilesMatrix.SetElement(col + xOffset,
												row + yOffset,
												pygame.draw.rect(self.Window,
																 color,
																 [	(col + xOffset) * BlockSize, 
																	(row + yOffset) * BlockSize, 
																	BlockSize,
																	BlockSize]))
