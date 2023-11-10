import os

from mc import MarkovChain
from mc_utils import load_data

directory_path = os.environ["DATA_TEXT_ESENIN"]

data = load_data(directory_path)

mc = MarkovChain()

mc.train(data)
mc.evaluate_dictionary()
