#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from random import randint
from dao import JogadorDAO
from time_futebol import TimeFutebol

class TiraTime:

	jogadores = []
	nomes_times = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
	tamanho_times = None

	def __init__(self, tamanho_times):
		self.tamanho_times = int(tamanho_times)

	def tira_time(self, num_times, method='elevador'):
		print ("")
		num_times = int(num_times)
		jogadores = JogadorDAO().get_jogadores()
		self.jogadores = sorted(jogadores, key=lambda x: x.get_media_pontos(), reverse=True)
		jogadores_df = self.get_jogadores_df(self.jogadores)

		print ("=============================================================")
		print ("Total jogadores:", len(self.jogadores))
		print (jogadores_df[['jogador', 'points', 'n_ratings']])
		print ("=============================================================")
		print ("\n\n")

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
			times = self.tira_time_elevador(num_times)
		
		elif method == "foco_media":
			media_geral_jogadores = self.get_jogadores_df(self.jogadores)["points"].mean()
			times = self.tira_time_foco_media(num_times, media_geral_jogadores)
			
		else:
			print ("Método para escolha de times não reconhecido")
			return

		return times


	def tira_time_elevador(self, num_times):
		times = self.start_times_elevador(num_times)
		times = self.rodadas_elevador(times)

		self.show_times(times)
		self.show_jogadores_sobraram()

	def start_times_elevador(self, num_times):
		times = []

		for i in range(num_times):
			nome = self.nomes_times[i]
			times.append( TimeFutebol(nome=nome) )

		return times

	def rodadas_elevador(self, times):
		while (not self.completou_times(times)) and (len(self.jogadores) != 0):

			for time in times:
				if len(self.jogadores) == 0:
					break

				melhor_jogador = self.jogadores[0]
				time.add_jogador(melhor_jogador)
				
				#jogador ja foi alocado pro time, remove ele
				self.jogadores = self.jogadores[1:]

				#ordena times do pior para o melhor para o pior começar escolhendo
				times = sorted(times, key=lambda x: x.get_pontos_time())

		return times



	def tira_time_foco_media(self, num_times, media_geral_jogadores):
		times = self.start_times_foco_media(num_times)
		times = self.rodadas_foco_media(times, media_geral_jogadores)

		self.show_times(times)
		self.show_jogadores_sobraram()


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

	def rodadas_foco_media(self, times, media_geral_jogadores):
		while (not self.completou_times(times)) and (len(self.jogadores) != 0):

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







	def show_times(self, times):
		times_json = []
		
		for time in times:
		
			for jogador in time.jogadores:
				jogador_json = {"time": time.nome, "jogador": jogador.nome, "points": jogador.get_media_pontos(), 'n_ratings': len(jogador.ratings)} 
				times_json.append(jogador_json)

		times_df = pd.DataFrame(times_json)

		for time in times_df.time.drop_duplicates().tolist():
			time_df = times_df[ times_df['time'] == time ]
			print ("**** TIME", time, "****")
			print ("Pontuacao do time: [", round(time_df['points'].sum(), 3), "]")
			print ("Media do time: [", round(time_df['points'].mean(), 3), "]")
			print ("")
			print (time_df[['jogador', 'points', 'n_ratings']])
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

	def completou_times(self, times):
		for time in times:
			if time.tamanho_time() < self.tamanho_times:
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

		return pd.DataFrame(jogadores_json)

	def quem_vai_jogar(self, jogadores_df):
		vai_jogar = []
		print ("Pressione <Enter> para confirmar...")
		print ("Pressione qualquer outra coisa para negar...")

		for nome in jogadores_df['jogador'].iteritems():
			nome = nome[1]
			print ("")
			resp = raw_input(nome.upper() + " vai jogar?")
			if len(resp) == 0:
				vai_jogar.append(nome)
				print (nome + " vai")
			else:
				print (nome + " não vai")

		return vai_jogar