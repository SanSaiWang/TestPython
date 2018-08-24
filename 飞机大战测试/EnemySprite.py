import pygame
from GameSprite import *
from plane_sprites import *
import random
class EnemySprite(GameSprite):
	def __init__(self):
		self.imagename = "./images/enemy0.png"
		super().__init__(self.imagename)
		self.rect.x = 0
		self.maxX = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,self.maxX)
		self.speed = random.randint(1,10)

	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			print("敌机已屏幕")
			self.kill()

	def __del__(self):
		print("敌机挂了 %s" % self.rect)
