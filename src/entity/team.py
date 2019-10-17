import pandas as pd
import numpy as np
import copy

class Team:

    def __init__(self, name, players=[]):
        self.name = name
        self.players = copy.deepcopy(players)

    def add_player(self, player):
        self.players.append(player)

    def rating(self):
        players_rating = [player.mean() for player in self.players]

        if self.size() > 0:
            return {"name": self.name,
                    "total": round(np.sum(players_rating), 2),
                    "mean": round(np.mean(players_rating), 2)}
        else:
            return {"name": self.name,
                    "total": 0,
                    "mean": 0}

    def get_players(self):
        return self.players

    def get_players_table(self):
        return pd.DataFrame([player.to_json() for player in self.players])[["name", "mean", "mad"]]


    def size(self):
        return len(self.players)

