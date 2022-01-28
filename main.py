import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import blog

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog from db'}
    else:
        return {'data': f'{limit} unpublished blog from db'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': "Blog is created with title as {blog.title}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="9000")
