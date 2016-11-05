class Jogador():

	def __init__(self, nome, ratings):
		self.ratings = ratings
		self.nome = nome

	def get_media_pontos(self):
		return round(sum(self.ratings) / float(len(self.ratings)), 3)


