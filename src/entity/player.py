import numpy as np
import pandas as pd

class Player:

    def __init__(self, id, name, ratings):
        self.id = id
        self.name = name
        self.ratings = ratings

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {"name": self.name, "mean": self.mean(), "median": self.median(), "mad": self.mad(), "id": self.id}

    def mean(self):
        return round(np.mean(self.ratings), 2)

    def median(self):
        return round(np.median(self.ratings), 2)

    def mad(self):
        return round(pd.Series(self.ratings).mad(), 2)