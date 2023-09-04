APi for an ML-Algorithm

Environment:

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands:

````Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
````

activate

````
source .venv/bin/activate
````

Running API using uvicorn:
uvicorn flight_delay_ml_api:app --reload