class Bird:
	count = 0
	def __init__(self,chat):
		self.sound = chat
		Bird.count += 1
	 
	def talk(self):
		return self.sound

class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)