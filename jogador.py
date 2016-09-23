from statistics import mean, median, mode

class Jogador():
	nome = ""
	ratings = None

	def __init__(self, nome, ratings):
		self.ratings = ratings
		self.nome = nome

	def get_points(self, points_method="mean"):
		if points_method == "mean":
			return mean(self.ratings)

		if points_method == "median":
			return median(self.ratings)
		
		if points_method == "mode":
			return mode(self.ratings)



