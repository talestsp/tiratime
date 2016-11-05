'''
Script para gerar o arquivo de ratings a partir do csv baixado com os dados do form
'''


import pandas as pd

raw_data_path_file = "data/raw_data/raw_data2.csv"

raw_data = pd.read_csv(raw_data_path_file)

if "Indicação de data e hora" in raw_data.columns.tolist():
    del raw_data["Indicação de data e hora"]

if "Digite seu nome" in raw_data.columns.tolist():
    del raw_data["Digite seu nome"]

cols = raw_data.columns.tolist()

data_json = []
for row_jogador in cols:
  for ratings_row in raw_data[row_jogador].iteritems():
    rating = ratings_row[1]
    nome_jogador = row_jogador.split(" - ")[0]
    
    try:
    	rating = float(rating)
    	data_json.append( {"Jogador": nome_jogador, "Rating": rating} )

    except ValueError:
    	ratings_multiplos = rating.split(";")
    	ratings_multiplos = list(map(int, ratings_multiplos))
    	media_ratings_multiplos = sum(ratings_multiplos) / float(len(ratings_multiplos))
    	rating = float(media_ratings_multiplos)
    	data_json.append( {"Jogador": nome_jogador, "Rating": rating} )

data = pd.DataFrame(data_json).dropna()

data.to_csv("data/2.csv", index=False)
