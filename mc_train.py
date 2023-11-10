from mc import MarkovChain
from mc_utils import load_data

directory_path = 'data'

data = load_data(directory_path)

mc = MarkovChain()

mc.train(data)
mc.evaluate_dictionary()
