.PHONY: install run format


install:
		pip install -r requirements.txt
		python -m pip install --upgrade pip
		echo "-dependencies installed"


run:
		python ./main.py


format:
		black . --exclude /alembic/*
		echo "-code is formatted with black"