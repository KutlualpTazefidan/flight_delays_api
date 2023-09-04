Environment:

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands:

````Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```sh
python -m venv .venv
.venv\Scripts\Activate.ps1
````
