class TimeFutebol:

	def __init__(self, nome):
		self.nome = nome
		self.jogadores = []

	def add_jogador(self, jogador):
		self.jogadores.append(jogador)

	def get_pontos_time(self):
		soma = 0
		for jogador in self.jogadores:
			soma += jogador.get_media_pontos()
		return soma

	def tamanho_time(self):
		return len(self.jogadores)

	def get_jogadores(self):
		nomes = []
		for j in self.jogadores:
			nomes.append(j.nome)
		return nomes

	def get_pontos_jogadores(self):
		pontos = []
		for j in self.jogadores:
			pontos.append(j.get_media_pontos())
		return pontos
