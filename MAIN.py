#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tira_time import TiraTime

# exemplo de como rodar 
# python3 main.py 6 3 mean elevador

if len(sys.argv) != 4:
	######################################################################################
	NUMERO_DE_TIMES = 3
	TAMANHO_TIMES = 6

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
	NUMERO_DE_TIMES = sys.argv[1]
	TAMANHO_TIMES = sys.argv[2]
	METODO_DE_TIRAR_TIME = sys.argv[3]


tt = TiraTime(tamanho_times=TAMANHO_TIMES)
times = tt.tira_time(num_times=NUMERO_DE_TIMES, method=METODO_DE_TIRAR_TIME)


medias = []

for time in times:
	medias.append(time.get_pontos_time() / time.tamanho_time())

print (medias)