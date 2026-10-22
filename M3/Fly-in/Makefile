.PHONY: install run clean debug lint

install:
	pip install flake8 mypy

run:
	python3 main.py

clean:
	rm -rf .mypy_cache
	find . -name "__pycache__" -type d -exec rm -rf {} +

debug:
	python3 -m pdb main.py

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
	--disallow-untyped-defs --check-untyped-defs
