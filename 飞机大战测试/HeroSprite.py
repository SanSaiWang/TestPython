import pygame
from GameSprite import *
from plane_sprites import *
from BulletSprite import *
class HeroSprite(GameSprite):
	def __init__(self):
		self.imagename = "./images/hero.gif"
		super().__init__(self.imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		# 创建子弹的精灵组
		self.bullets = pygame.sprite.Group()


	def update(self):
		self.rect.x += self.speed
		# 判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		print("发射子弹。。。")
		
		bullet = BulletSprite()
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.top - 20
		self.bullets.add(bullet)


		bullet1 = BulletSprite()
		bullet1.rect.centerx = self.rect.centerx - 35
		bullet1.rect.y = self.rect.top +35
		self.bullets.add(bullet1)

		bullet2 = BulletSprite()
		bullet2.rect.centerx = self.rect.centerx + 35
		bullet2.rect.y = self.rect.top + 35
		self.bullets.add(bullet2)

		

