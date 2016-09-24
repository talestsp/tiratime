class Jogador():
	nome = ""
	ratings = None

	def __init__(self, nome, ratings):
		self.ratings = ratings
		self.nome = nome

	def get_media_pontos(self):
		return sum(self.ratings) / float(len(self.ratings))


