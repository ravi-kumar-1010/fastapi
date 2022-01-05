from fastapi import FastAPI
app = FastAPI()

@app.get('/blog')
def index(limit: int,published: bool):
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
