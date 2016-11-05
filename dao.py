#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from os import listdir
from jogador import Jogador

DATA_DIR = "data/"

class JogadorDAO:

	def __init__(self, ratings_filename):
		'''
		ratings_filename: 
					nome do arquivo de ratings do jogadores no diretorio data/
					se o arquivo não existir, gere ele com data/preproc.py
		'''
		self.data = self.load_data(ratings_filename)

	def load_data(self, ratings_filename):
		data = pd.read_csv(DATA_DIR + ratings_filename)
		data['Rating'] = data['Rating'].astype(float)

		return data

	def get_data(self):
		return self.data

	def get_util_data(self, use="recent"):
		'''
		Pega os dados dos jogadores que vao jogar no dia
		'''
		quem_vai = self.quem_vai_jogar()
		util_data = pd.merge(self.data, quem_vai, on='Jogador', how='inner')

		return util_data

	def get_jogadores_do_dia(self):
		'''
		Retorna uma lista dos jogadores do dia do raxa
		'''
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
		'''
		Retorna um data frame de uma coluna com os jogadores que vão jogar no dia
		'''
		data = pd.read_csv("quem_vai_jogar/quem_vai_jogar.csv")
		data = data[data['Vai'] == 1]
		del data['Vai']
		return data
