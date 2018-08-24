import pygame
from GameSprite import *
class BulletSprite(GameSprite):
	"""子弹精灵"""
	def __init__(self):
		super().__init__("./images/bullet1.png", -2)

	def update(self):
		super().update()
		# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()
