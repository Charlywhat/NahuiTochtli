class Animate():
	def __init__(self, images, speed):
		self.counter = 10
		self.index = 0
		self.speed = speed
		self.images = images
		self.current_image = self.images[self.index]
		
	def play(self):
		if self.counter > 0:
			self.counter -= self.speed
		else:
			self.index += 1
			try:
				self.current_image = self.images[self.index]
			except:
				self.index = 0
				self.current_image = self.images[self.index]
			self.counter = 10
				
	def stop(self):
		self.counter = 10
		self.index = 0
		self.current_image = self.images[self.index]
	
	def get_current_image(self):
		return self.current_image


class SFX():
	def __init__(self, sfx, freq = 60):
		self.counter = 60
		self.freq = freq
		self.sfx = sfx
		self.playable = True
	
	def update(self):
		if self.counter > 0:
			self.counter -= self.freq
		else:
			self.counter = 60
		if self.counter == 60: self.playable = True
		else: self.playable = False
	
	def is_playing(self):
		if self.sfx.get_num_channels() > 0:
			return True
		else: return False
		
	def is_playable(self):
		return self.playable
	
	def get_sfx(self):
		return self.sfx
