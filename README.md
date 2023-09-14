APi for an ML-Algorithm

Environment:

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands:

```Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

activate

```
source .venv/bin/activate
```

Running API using uvicorn:
uvicorn main:app --reload

For render:
uvicorn main:app --host 0.0.0.0 --port 10000

Freezing pip installs:

```
pip freeze > requirements.txt
```
