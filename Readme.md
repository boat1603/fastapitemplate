# Setup

### (Optional) Create virtual environment using:

```
$ python -m venv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```
    
# Run Server

```
$ uvicorn main:app --host 0.0.0.0 --port 8000
```

# Development
When add new lib you can add your new lib trough

```
$ pip freeze > requirements.txt 
```