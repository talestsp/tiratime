# tiratime

# Executando
#### python MAIN.py num_times tamanho_time metodo_tiratime
* **num_times**: quantidade de times
* **tamanho_time**: num de jogadores por time
* **metodo_tiratime**: elevador ou foco_media

# Requirements
* pandas

usa o pip install para instalar essas libs

# data/preproc.py
Rode esse script para preprocessar os dados baixados do formulario de votos
Ah, o csv do formulario de votos deve estar em **data/raw_data**

# quem_vai_jogar/quem_vai_jogar.csv
Marcar com 1, quem for jogar

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
* Oção para selecionar quais jogadores irão jogar no dia
* Enviar email para todo mundo informando os times