#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from numpy import var
from tira_time import TiraTime

# exemplo de como rodar 
# python3 main.py 6 3 mean elevador


# METODO_DE_TIRAR_TIME = elevador
# implementa o convencional tira time em rodadas
# os melhores n jogadores são os capitães
# em cada rodada cada capitão tira o melhor jogador disponível pro seu time
# o detalhe aqui é que em cada rodada, os times que estiverem pior, escolhem primeiro

# METODO_DE_TIRAR_TIME = foco_media
# cada um dos n capitães são escolhido random
# em cada rodada o capitão escolhe o jogador que faz a média do time ser a média geral
# média geral é a média de TODOS os jogadores do raxa


NUMERO_DE_TIMES = sys.argv[1]
TAMANHO_TIMES = sys.argv[2]
METODO_DE_TIRAR_TIME = sys.argv[3]

ratings_filename="3.csv"
new_players = [{"jogador": "FULANO TESTE", "ratings": [3.2, 3.8, 3.6]}]
new_players = None

tt = TiraTime(	
				ratings_filename=ratings_filename, 
				new_players=new_players
			 )



times = tt.tira_time(	
					num_times=NUMERO_DE_TIMES, 
					tamanho_times=TAMANHO_TIMES, 
					method=METODO_DE_TIRAR_TIME
				)

times_points = []

for time in times:
	times_points.append(time.get_pontos_time() / int(TAMANHO_TIMES))

print("Variancia dos times:", var(times_points))
print("\n\n\n")




