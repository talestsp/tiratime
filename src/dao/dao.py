import pandas as pd
from src.entity.player import Player

USERNAME_COLNAME = "Qual é seu nome?"
DATETIME_COLNAME = "Carimbo de data/hora"
EMPTY_COLUMS_PREFIX = "Unnamed:"


def load_players(data_file_path):
    raw_data = pd.read_csv(data_file_path)
    return build_players(raw_data)

def build_players(data):
    players = []
    for colname in data.columns:
        if colname == USERNAME_COLNAME or colname == DATETIME_COLNAME or colname.startswith(EMPTY_COLUMS_PREFIX):
            continue

        players.append(Player(id=None,
                              name=colname,
                              ratings=data[colname].tolist()))

    return players