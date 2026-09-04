# Makefile for Physics 11 Deep Understanding Book

.PHONY: all figures book clean

all: book

figures:
	python scripts/generate_figures.py

book:
	python scripts/build_book.py

clean:
	rm -rf dist preview
