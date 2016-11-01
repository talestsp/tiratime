import pandas as pd


def summarize_players(data):
	ratings_json = []
	for jogador in data.columns.tolist()[1:]:
		ratings_jogador = data[jogador].dropna()
		ratings_json.append({"jogador": jogador, "rating": round(ratings_jogador.mean(), 3), "n_ratings": len(ratings_jogador)})
	#
	ratings = pd.DataFrame(ratings_json).sort_values(by="rating", ascending=False)
	ratings[["jogador", "rating", "n_ratings"]]
	ratings = ratings.reset_index(drop=True)
	ratings.to_csv("data/2-ratings.csv", index=False)
	#
	return ratings

def clean_data(data):
	del data["Indicação de data e hora"]
	cols = data.columns.tolist()
	#limpa as colunas
	new_cols = []
	for coluna in cols:
		coluna = coluna.replace(" - Quantas estrelas (1 até 5)", "")
		new_cols.append(coluna)
	data.columns = new_cols
	#
	data = data.rename(columns={'Digite seu nome': 'Avaliador'})
	return data

def centroid_closest_voters(data, ratings=None):
	if ratings is None:
		ratings = summarize_players(clean_data(data))
	#
	reference = ratings['rating']
	reference.index = ratings['jogador']
	reference = reference.sort_values()
	#para cada avaliador...
	evaluators_me = []
	avaliadores = data['Avaliador'].tolist()
	#
	for avaliador in avaliadores:
		avaliador_data = data[data['Avaliador'] == avaliador]
		del avaliador_data['Avaliador']
		#
		mean_error = abs(avaliador_data - reference)
		#se nao votou no jogador, o erro eh 4 (maior erro possivel)
		mean_error = mean_error.fillna(4)
		evaluators_me.append({'Avaliador': avaliador, 'Erro Médio': mean_error.iloc[0].mean()})
	#
	voting_distances = pd.DataFrame(evaluators_me)
	voting_distances.sort_values(by="Erro Médio")
	return voting_distances


path = "data/2.csv"
data = pd.read_csv(path)

data = clean_data(data)
ratings = summarize_players(data)
voting_distances = centroid_closest_voters(data, ratings)



