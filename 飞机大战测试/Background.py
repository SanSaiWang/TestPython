from GameSprite import *
from plane_sprites import *
class Background(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = "./images/background.png"
		super().__init__(self.imagename,2)
		if is_alt:
			self.rect.y = - self.rect.height
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height