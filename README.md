# 📦 FastAPI Project Setup

This guide explains how to set up and run the FastAPI project.

---

## ✅ Requirements

- Python 3.10+
- pip installed

---
## 🔹 Setup Instructions

### 1. Create and activate a virtual environment

**macOS/Linux**
```bash
python -m venv venv
source venv/bin/activate    
```
**Windows**
```bash
venv\Scripts\activate 
``` 
 

**Troubleshooting:**
Every Python virtual environment (venv, conda, pyenv, etc.) has its own packages.

**For example:**

If you run pip install yfinance inside one terminal tab or VS Code,
But then run your app from another terminal tab using a different environment,
That new one won’t have yfinance — so it fails.
Check your current Python path:
which python

Then check where pip is installing packages:
which pip

If python and pip point to different paths, they’re not using the same environment.

### 2. Install dependencies like FastAPI, Uvicorn and yfinance

In your terminal:
```pip install -r requirements.txt```

OR

```pip install fastapi uvicorn yfinance```

Globaly:
```pip install --user yfinance```

You can check it installed correctly

```pip list```

Check the selected Python interpreter in VS Code:

### 3. Select the correct interpreter in VS Code
Make sure VS Code is using the correct environment (the one where FastAPI is installed):

Press ```Ctrl+Shift+P``` (or ```Cmd+Shift+P``` on macOS)
Type: ```Python: Select Interpreter```
Choose the environment that has FastAPI installed ```(./venv/...)```.

### 4. Activate your virtual environment

If you have a virtual environment (like venv), activate it:
In your terminal (# for macOS/Linux):
```source venv/bin/activate  ```

### 5. Run the FastAPI server

In your terminal:
```uvicorn main:app --reload```

comments:
app = the FastAPI instance
--reload = auto-reload on changes (for dev)


## TEST

### ✅ 1. Install the required packages (if not yet installed):
```pip install pytest httpx pytest-asyncio```

### ✅ 2 Run the test:
```pytest test_main.py```


