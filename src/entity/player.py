import numpy as np
import pandas as pd

class Player:

    def __init__(self, id, name, ratings):
        self.id = id
        self.name = name
        self.ratings = ratings

    def mean(self):
        return np.mean(self.ratings)

    def median(self):
        return np.median(self.ratings)

    def mad(self):
        return pd.Series(self.ratings).mad()