from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel
from random import randrange
import uvicorn
import psycopg2
import time
from psycopg2.extras import RealDictCursor

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try: # for doing connect have to write belo code within try:
        conn = psycopg2.connect(host="localhost", database='fastapi',
                                user="postgres", password='#@Pyadmin@#',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Database connection was failed")
        print("Error: ", error)
        time.sleep(2.00)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 1}]


def find_post(id):
    for i, value in enumerate(my_posts):
        if value["id"] == id:
            index = i
            return index, value
    return None, None


@app.get(path="/post", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts""")
    post = cursor.fetchall()
    return {"data": post}


@app.post(path="/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10000)
    my_posts.append(post_dict)
    return {"Data": post_dict}


@app.get(path="/posts/{id}")
def get_user(id: int):
    _, post = find_post(id)

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" The id {id} is not exist in the Database")

    return {"Searching": post}


@app.put(path="/posts/{id}")
def update(id: int, post: Post):
    index, _ = find_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"post with id: {id} does not exist")
    post_dic = post.dict()
    post_dic["id"] = id
    my_posts[index] = post_dic
    return {"post": my_posts}


@app.patch(path="/posts/{id}")
def update_unique(id: int, post: Post):
    index, _ = find_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"post with id: {id} does not exist")
    post_dic = post.dict()
    post_dic["id"] = id
    my_posts[index] = post_dic
    return {"post": my_posts}


@app.delete(path="/posts/{id}")
def delete_id(id: int):
    index, _ = find_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return my_posts


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
