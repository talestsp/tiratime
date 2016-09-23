# tiratime

# Executando
#### python main.py tamanho_time num_times metodo_sumarizar_rating metodo_tiratime
* **tamanho_time**: num de jogadores por time
* **num_times**: quantidade de times
* **metodo_sumarizar_rating**: dados os ratings por jogador, é pra tirar a mean, median ou mode? melhor usar mean

* **metodo_tiratime**: elevador ou foco_media

# Requirements
* pandas
* statistics

usa o pip install

# More info
#### Ratings
Será considerado os ratings dados na ultima tabela colocada no projeto.
Se o jogador não tiver sido avaliado (ratiado) ele pega na tabela anterior e por aih vai

As tabelas serão prenchidas via Google Forms ou semelhante
Nesse form vai ter uma foto do atleta (kkk) junto do nome
Vc dá de 1 a 5 pontos nele

####Metodo de tirar time
#####elevador
implementa o convencional tira time em rodadas os melhores n jogadores são os capitães em cada rodada cada capitão tira o melhor jogador disponível pro seu time o detalhe aqui é que em cada rodada, os times que estiverem pior escolhem primeiro

##### foco_media
cada um dos n capitães são escolhido random em cada rodada o capitão escolhe o jogador que faz a média do time ser a média geral média geral é a média de TODOS os jogadores do raxa

# TODO
Oção para selecionar quais jogadores irão jogar no dia
Enviar email para todo mundo informando os times