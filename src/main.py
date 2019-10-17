from src.dao.dao import load_players
from src.data_processment import make_teams

players = load_players("data/dados.csv")

teams = make_teams.traditional(players, n_teams=3, n_player_team=5)
teams.sort(key=lambda team : team.rating()["total"], reverse=False)

for team in teams:
    players_table = team.get_players_table()
    players_table = players_table.set_index(players_table.index + 1)
    players_table.columns = ["Jogador", "Pontos", "Variação"]

    print("Team:", team.name, team.rating()["total"])
    print(players_table)

    print()
