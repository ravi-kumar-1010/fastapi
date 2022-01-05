from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {"data": "Ravi Kumar"}


@app.get('/about')
def about():
    return {"About Me": "I am a developer"}
