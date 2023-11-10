import sys
from mc import MarkovChain

PROMPT = sys.argv[1]
LENGTH = 500

mc = MarkovChain()
mc.read_dictionary()

text_generated = mc.generate(PROMPT, LENGTH)

print(text_generated)