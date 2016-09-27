#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from os import listdir
from jogador import Jogador

class JogadorDAO:
	DATA_DIR = "data/"
	data = None

	def __init__(self):
		self.data = self.load_data()

	def load_data(self):
		data_all = listdir("data/")
		data_files = []

		#remove o que nao for arquivo de dados
		for f in data_all:
			if (".csv" in f) and (f[-1] != "~"):
				data_files.append(f)

		data_files = sorted(data_files, reverse=True)

		data = pd.DataFrame()

		for data_file in data_files:
			file_data = pd.read_csv(self.DATA_DIR + data_file)

			# insere no DF o numero da tabela de ratings...
			# importante para considerar apenas os ratings mais recentes por jogador
			# se na ultima tabela de rating o jogador nao avaliado, pega a outra tabela de rating mais recente
			file_data['source'] = data_file

			data = data.append(file_data)
		data['Rating'] = data['Rating'].astype(float)

		return data


	def get_util_data(self, use="recent"):
		#use = 'recent' - pega o rating mais recentes de cada jogador
		#use = 'all' - pega todo o historico de ratings de cada jogador

		lista_nomes_jogadores = self.get_lista_jogadores()
		util_data = pd.DataFrame()

		for nome_jogador in lista_nomes_jogadores:

			# todos o historico de ratings do jogador
			all_jogador_data = self.data[ self.data['Jogador'] == nome_jogador ]

			#pega os ratings da ultima tabela (source) em que o jogador ou avaliado
			recent_source_jogador_data = max( all_jogador_data['source'] )
			recent_jogador_data = all_jogador_data[ all_jogador_data['source'] == recent_source_jogador_data ]

			util_data = util_data.append(recent_jogador_data)

		quem_vai = self.quem_vai_jogar()

		util_data = (pd.merge(util_data, quem_vai, on='Jogador', how='inner'))

		return util_data

	def get_jogadores(self, ):
		lista_nomes_jogadores = self.get_lista_jogadores()
		lista_jogadores = []

		data_util = self.get_util_data()

		for nome_jogador in lista_nomes_jogadores:
			if nome_jogador in data_util.Jogador.tolist():		
				jogador_data = data_util[ data_util['Jogador'] == nome_jogador ]
				ratings = jogador_data['Rating'].tolist()

				jogador = Jogador(nome=nome_jogador, ratings=ratings)

				lista_jogadores.append(jogador)

		return lista_jogadores


	def get_lista_jogadores(self):
		return self.data['Jogador'].drop_duplicates().tolist()

	def quem_vai_jogar(self):
		data = pd.read_csv("quem_vai_jogar/quem_vai_jogar.csv")
		data = data[data['Vai'] == 1]
		del data['Vai']
		return data

