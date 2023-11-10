SRC='src'

train:
	python3 ${SRC}/mc_train.py

generate:
	python3 ${SRC}/mc_generate.py $(prompt)