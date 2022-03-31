from fastapi import FastAPI

from somewhere import db
from somewhere.models import Topic

app = FastAPI()


@app.get("/")
async def hello():
    return {"Hello": "World"}


@app.get("/topics/{topic_id}")
async def get_topic(topic_id: int):
    topic = Topic(id=topic_id, name="test")

    return topic


@app.put("/topics/{topic_id}")
async def update_topic(topic_id: int, topic: Topic):
    return {"topic_name": topic.name, "topic_id": topic_id}


@app.get("/initdb")
async def db_init():
    db.init()

    return {"message": "Init Database"}
