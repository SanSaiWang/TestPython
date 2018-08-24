import pygame
from plane_sprites import *
from Background import *
from EnemySprite import *
from HeroSprite import *
from BulletSprite import *
class PlaneGame(object):
	"""飞机大战主游戏"""
	def __init__(self):
			# pygame.init()
			print("游戏初始化")
			self.screen = pygame.display.set_mode(SCREEN_RECT.size)
			print(SCREEN_RECT.size)
			self.clock = pygame.time.Clock()
			self.__create_sprites()
			pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
			pygame.time.set_timer(HERO_FIRE_EVENT, 600)
	def start_game(self):
			print("游戏开始...")
			while True:
				self.clock.tick(60)
				# 事件监听
				self.__event_handler()
				# 检测碰撞
				self.__check_collide()
				# 更新精灵组
				self.__update_sprites()
				#更新屏幕显示
				pygame.display.update()
	def __event_handler(self):
				"""事件监听"""
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						PlaneGame.__game_over()
					elif event.type == CREATE_ENEMY_EVENT:
						print("敌机出场...")
						self.enemy_group.add(EnemySprite())
					keys_pressed = pygame.key.get_pressed()
					if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_DOWN]:
						self.hero.speed = 2
					elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_UP]:
						self.hero.speed = -2
					else:
						self.hero.speed = 0
					if event.type == HERO_FIRE_EVENT:
						self.hero.fire()
	def __check_collide(self):
			# 1. 子弹摧毁敌机
			pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
			# 2. 敌机撞毁英雄
			enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
			# 判断列表是否有内容
			if len(enemies) > 0:
				# 让英雄牺牲
				self.hero.kill()
				# 结束游戏
				PlaneGame.__game_over()

	def __update_sprites(self):
				"""更新精灵组"""

				for group in [self.back_group, self.enemy_group, self.hero_group,self.hero.bullets]:
					group.update()
					group.draw(self.screen)

	def __create_sprites(self):
				"""创建精灵组"""

				# 背景组
				self.back_group = pygame.sprite.Group()
				# 敌机组
				self.enemy_group = pygame.sprite.Group()
				# 英雄组
				self.hero_group = pygame.sprite.Group()
				
				# 创建背景精灵和精灵组
				bg1 = Background()
				bg2 = Background(True)
				bg1.rect.y = 0
				bg2.rect.y = -bg2.rect.height

				self.back_group = pygame.sprite.Group(bg1, bg2)
				# 英雄组
				self.hero = HeroSprite()
				self.hero_group = pygame.sprite.Group(self.hero)

	@staticmethod
	def __game_over():
			"""游戏结束"""
			print("游戏结束")
			pygame.quit()
			exit()
if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()