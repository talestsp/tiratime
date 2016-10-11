import pandas as pd
import json

path_fixa = "data/fixa.json"
path_movel = "data/movel.json"

fixa_dict = literal_eval(open(path_fixa).read())
movel_dict = literal_eval(open(path_movel).read())

fixa = pd.read_json(path_fixa)
movel = pd.read_json(path_movel)

