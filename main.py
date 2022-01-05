from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit:int = 10,published: bool=True,sort:Optional[str] = None):
    if published:
        for i in range(limit):
            yield {'Published item': i}
    else:
        for i in range(limit):
            yield {'Unpublished item': i}

# Beware in dynamic routing, move static above dynamic ones

@app.get('/blog/unpublished')
def blog_unpublished():
    return {"Blog": "Unpublished"}

@app.get('/blog/{id}')
def blog(id: int):
    return {"data": "Blog " + str(id)}


@app.get('/blog/{id}/{title}')
def blog_title(id: int, title: str):
    return {"BLOG ID":str(id) , " BLOG TITLE:":title}

@app.get('/about')
def about():
    return {"About Me": "I am a developer"} 

class Blog(BaseModel):
    title: str
    body:str
    published_at:Optional[bool]
    

# @app.post('/blog/{info}')
# def create_blog(info: str):
#     return {"Blog": info}

@app.post('/blog')
def create_blog(request: Blog):
    return {"Blog": f"Blog is created with  {request.title} as title"}


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000)