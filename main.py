from typing import Optional
import os

import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Topic(BaseModel):
    id: int
    name: str
    description: str


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/topics/{topic_id}")
def get_topic(topic_id: int, q: Optional[str] = None):
    return {"topic_id": topic_id, "q": q}


@app.put("/topics/{topic_id}")
def update_topic(topic_id: int, topic: Topic):
    return {"topic_name": topic.name, "topic_id": topic_id}


@app.get("/initdb")
def db_init():
    db = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_NAME"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host="db",
        port=5432,
    )

    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
    )
    cursor.close()
    db.close()

    return {"message": "Init Database"}
