#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from random import randint, shuffle
from dao import JogadorDAO
from time_futebol import TimeFutebol
from jogador import Jogador

class TiraTime:

	nomes_times = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "I"]

	def __init__(self, ratings_filename, new_players=None):
		'''
		ratings_filename: nome do csv com os ratings dos jogadores

		new_players: 
					lista de dicionario estilo json
					cada dicionario para um jogador com as keys 'jogador' e 'ratings'
					'jogador' eh uma string com o nome
					'ratings' eh uma lista de ratings
					exemplo
					new_players = [{"Nome": "Fulano", "ratings": [3.1, 3.5]}]
		'''
		self.ratings_filename = ratings_filename
		self.new_players = new_players

	def tira_time(self, num_times, tamanho_times, method='elevador'):
		num_times = int(num_times)
		tamanho_times = int(tamanho_times)

		self.jogadores = JogadorDAO(self.ratings_filename).get_jogadores_do_dia_pelo_csv()
		if self.new_players is not None:
			self.jogadores = self.add_new_players(self.jogadores, self.new_players)

		shuffle(self.jogadores)
		jogadores_df = self.get_jogadores_df(self.jogadores)

		self.show_jogadores_do_dia(jogadores_df)

		# method = elevador
		# implementa o convencional tira time em rodadas
		# os melhores n jogadores são os capitães
		# em cada rodada cada capitão tira o melhor jogador disponível pro seu time
		# o detalhe aqui é que em cada rodada, os times que estiverem pior, escolhem primeiro

		# method = foco_media
		# cada um dos n capitães são escolhido random
		# em cada rodada o capitão escolhe o jogador que faz a média do time ser a mais proxima da média geral
		# média geral é a média de TODOS os jogadores do raxa

		if method == "elevador":
			times = self.tira_time_elevador(num_times, tamanho_times)

			self.show_times(times)
			self.show_jogadores_sobraram()
		
		elif method == "foco_media":
			media_geral_jogadores = self.get_jogadores_df(self.jogadores)["points"].mean()
			times = self.tira_time_foco_media(num_times, tamanho_times, media_geral_jogadores)

			self.show_times(times)
			self.show_jogadores_sobraram()
			
		else:
			raise Exception("Método para escolha de times não reconhecido")

		return times

	def add_new_players(self, jogadores, new_players):
		for new_player in new_players:
			jogador = Jogador(nome=new_player['jogador'], ratings=new_player['ratings'])
			jogadores.append(jogador)

		return jogadores


	def tira_time_elevador(self, num_times, tamanho_times):
		times = self.start_times_elevador(num_times)
		times = self.rodadas_elevador(times, tamanho_times)

		return times

	def start_times_elevador(self, num_times):
		times = []

		for i in range(num_times):
			nome = self.nomes_times[i]
			times.append( TimeFutebol(nome=nome) )

		shuffle(times)
		return times

	def rodadas_elevador(self, times, tamanho_times):
		while (not self.completou_times(times, tamanho_times)) and (len(self.jogadores) != 0):

			for time in times:
				if len(self.jogadores) == 0:
					break

				melhor_jogador = self.get_melhor_jogador(self.jogadores)
				time.add_jogador(melhor_jogador)
				
				#jogador ja foi alocado pro time, remove ele
				self.jogadores.remove(melhor_jogador)

				#ordena times do pior para o melhor para o pior começar escolhendo
				times = sorted(times, key=lambda x: x.get_pontos_time())

		return times

	def tira_time_foco_media(self, num_times, tamanho_times, media_geral_jogadores):
		times = self.start_times_foco_media(num_times)
		times = self.rodadas_foco_media(times, tamanho_times, media_geral_jogadores)

		return times

	def start_times_foco_media(self, num_times):
		times = []

		for i in range(num_times):
			nome = self.nomes_times[i]
			time = TimeFutebol(nome=nome)

			jogador = self.jogadores[ randint(0, len(self.jogadores) - 1 ) ]
			time.add_jogador(jogador)

			self.jogadores.remove(jogador)

			times.append( time )

		return times

	def rodadas_foco_media(self, times, tamanho_times, media_geral_jogadores):
		while (not self.completou_times(times, tamanho_times)) and (len(self.jogadores) != 0):

			for time in times:
				if len(self.jogadores) == 0:
					break	

				# será escolhido o jogador que, caso seja adicionado no... 
				# ...time, o time fique com a media bem perto da media geral
				melhor_opcao = {"jogador": None, "diff": 999999}
				pontos_time = time.get_pontos_jogadores()

				for jogador in self.jogadores:
					media = self.mean(pontos_time + [jogador.get_media_pontos()] )

					diff = abs(media - media_geral_jogadores)

					if diff < melhor_opcao['diff']:
						melhor_opcao = {"jogador": jogador, "diff": diff}

				time.add_jogador(melhor_opcao['jogador'])
				#jogador ja foi alocado pro time, remove ele
				self.jogadores.remove(melhor_opcao['jogador'])
				
				#ordena times do pior para o melhor para o pior começar escolhendo
				times = sorted(times, key=lambda x: x.get_pontos_time())

		return times

	def mean(self, lista):
		return sum(lista) / float(len(lista))

	def completou_times(self, times, tamanho_times):
		for time in times:
			if time.tamanho_time() < tamanho_times:
				return False
		return True

	def get_jogadores_df(self, jogadores):
		jogadores_json = []
		
		for jogador in jogadores:
			nome = jogador.nome
			points = jogador.get_media_pontos()
			ratings = jogador.ratings

			jogador_dict = {"jogador": nome, "points": points, "n_ratings": len(ratings)}
			jogadores_json.append(jogador_dict)

		jogadores_df = pd.DataFrame(jogadores_json)

		return jogadores_df

	def get_melhor_jogador(self, jogadores):
		melhor = jogadores[0]
		for jogador in jogadores:
			if jogador.get_media_pontos() > melhor.get_media_pontos():
				melhor = jogador
		return melhor


	def show_jogadores_do_dia(self, jogadores_df):
		print ("")
		print ("=============================================================")
		print ("Total jogadores:", "[", len(self.jogadores), "]")
		print ("Media geral:", "[", round(jogadores_df.points.mean(), 3), "]")
		ranking = jogadores_df.sort_values(by='points', ascending=False)[['jogador', 'points', 'n_ratings']]
		ranking.index = range(1, len(ranking) + 1)
		print (ranking)
		print ("=============================================================")
		print ("\n\n")

	def show_times(self, times):
		times_df = pd.DataFrame()
		
		for time in times:
			time_df = time.get_time_df()			
			times_df = times_df.append(time_df)

			print ("**** TIME", time.nome, "****")
			print ("Pontuacao do time: [", round(time_df['points'].sum(), 3), "]")
			print ("Media do time: [", round(time_df['points'].mean(), 3), "]")
			print ("")
			print (time_df[['jogador', 'points', 'n_ratings']].sort_values(by="points", ascending=False))
			print ("************************************************************")
			print ("")

	def show_jogadores_sobraram(self):
		if len(self.jogadores) == 0:
			print ("Não sobrou jogador")
			return

		jogadores_json = []

		for j in self.jogadores:
			jogador = {"jogador": j.nome, "points": j.get_media_pontos(), "n_ratings": len(j.ratings)}
			jogadores_json.append(jogador)

		sobrou_df = pd.DataFrame(jogadores_json)
		sobrou_df['time'] = "Sem Time"

		print ("\n\nSobraram os seguintes jogadores")
		print (sobrou_df[['jogador', 'points', 'n_ratings']])
		print ("********************************")

