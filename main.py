#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tira_time import TiraTime

# exemplo de como rodar 
# python3 main.py 6 3 mean elevador

if len(sys.argv) != 5:
	######################################################################################
	TAMANHO_TIMES = 6
	NUMERO_DE_TIMES = 3

	# os points do jogador vão ser o quê? média ou mediana ou moda dos ratings?
	# CRITERIO_PONTOS_JOGADOR deve ser 'mean', 'median' ou 'mode'
	CRITERIO_PONTOS_JOGADOR = 'mean'

	# METODO_DE_TIRAR_TIME = elevador
	# implementa o convencional tira time em rodadas
	# os melhores n jogadores são os capitães
	# em cada rodada cada capitão tira o melhor jogador disponível pro seu time
	# o detalhe aqui é que em cada rodada, os times que estiverem pior, escolhem primeiro

	# METODO_DE_TIRAR_TIME = foco_media_time
	# cada um dos n capitães são escolhido random
	# em cada rodada o capitão escolhe o jogador que faz a média do time ser a média geral
	# média geral é a média de TODOS os jogadores do raxa
	METODO_DE_TIRAR_TIME = 'elevador'
	######################################################################################

else:
	TAMANHO_TIMES = sys.argv[1]
	NUMERO_DE_TIMES = sys.argv[2]
	CRITERIO_PONTOS_JOGADOR = sys.argv[3]
	METODO_DE_TIRAR_TIME = sys.argv[4]


tt = TiraTime(tamanho_times=TAMANHO_TIMES, method_points_jogador=CRITERIO_PONTOS_JOGADOR)
tt.tira_time(num_times=NUMERO_DE_TIMES, method=METODO_DE_TIRAR_TIME)
