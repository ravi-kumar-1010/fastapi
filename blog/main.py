from fastapi import FastAPI
from . import schemas
from . import models
from .database import engine
from . import crud
app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):
    return {"title":request.title,"body":request.body}