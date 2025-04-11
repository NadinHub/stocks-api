📦 Requirements
Python 3.10+
pip installed

✅ 1.  Create and activate a virtual environment

In your terminal (# macOS/Linux):
python -m venv venv
source venv/bin/activate  


Troubleshooting:
Every Python virtual environment (venv, conda, pyenv, etc.) has its own packages.

For example:

If you run pip install yfinance inside one terminal tab or VS Code,
But then run your app from another terminal tab using a different environment,
That new one won’t have yfinance — so it fails.
Check your current Python path:
which python

Then check where pip is installing packages:
which pip

If python and pip point to different paths, they’re not using the same environment.

✅ 2. Install dependencies like FastAPI, Uvicorn and yfinance

In your terminal:
pip install -r requirements.txt

OR

pip install fastapi uvicorn yfinance

Globaly:
pip install --user yfinance

You can check it installed correctly

pip list

✅ 3. Activate your virtual environment

If you have a virtual environment (like venv), activate it:
In your terminal (# for macOS/Linux):
source venv/bin/activate  

✅ 4. Run the FastAPI server

In your terminal:
uvicorn main:app --reload

comments:
app = the FastAPI instance
--reload = auto-reload on changes (for dev)


TEST

✅ 1. Install the required packages (if not yet installed):
pip install pytest httpx pytest-asyncio

✅ 2 Run the test:
pytest test_main.py


