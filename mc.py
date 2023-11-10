import ast
import numpy as np

kernel = 7
MODEL_FILE_NAME = "dictionary/dictionary.txt"

class MarkovChain():
    def __init__(self):
        self.dictionary = {}
        self.K = kernel

    def train (self, data):
        for i in range(len(data) - self.K):
            X = data[i : i + self.K]
            Y = data[i + self.K]
            if self.dictionary.get(X) is None:
                self.dictionary[X] = {}
                self.dictionary[X][Y] = 1
            else:
                if self.dictionary[X].get(Y) is None:
                    self.dictionary[X][Y] = 1
                else:
                    self.dictionary[X][Y] += 1

        for kx in self.dictionary.keys():
            psum = float(sum(self.dictionary[kx].values()))
            for k in self.dictionary[kx].keys():
                self.dictionary[kx][k] = self.dictionary[kx][k] / psum

        self.save_dictionary()

    def sample_next(self, ctx):
        ctx = ctx[-self.K:]
        if self.dictionary.get(ctx) is None:
            return " "
        possible_chars = list(self.dictionary[ctx].keys())
        possible_values = list(self.dictionary[ctx].values())

        return np.random.choice(possible_chars, p=possible_values)

    def generate(self, prompt, max_len):
        sentence = prompt
        ctx = prompt[-self.K:]
        for _ix in range(max_len):
            next_prediction = self.sample_next(ctx)
            sentence += next_prediction
            ctx = sentence[-self.K:]
        return sentence
  
    def save_dictionary(self):
        if bool(self.dictionary) is False:
            print('Nothing to save - the dictionary is empty.')
            return
        with open(MODEL_FILE_NAME, "w") as file:
            file.write(str(self.dictionary))

    def read_dictionary(self):
        with open(MODEL_FILE_NAME) as file:
            chain_string = file.read()
        self.dictionary = ast.literal_eval(chain_string)

    def print_dictionary(self):
        print(self.dictionary)
        
    def evaluate_dictionary(self):
        max_subfields = 0
        max_field = None
        for field, subfields in self.dictionary.items():
            if len(subfields) > max_subfields:
                max_subfields = len(subfields)
                max_field = field
        print(max_field, self.dictionary[max_field])