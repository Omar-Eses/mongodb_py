from fastapi import FastAPI

app = FastAPI()

import ssl
import motor.motor_asyncio
uri = "mongodb+srv://tariqsnaser:123@cluster0.640cmau.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = motor.motor_asyncio.AsyncIOMotorClient(uri)


@app.get("/")
async def root():
    d = {'name':'tariq', 'age':23}
    coll  = client['test']
    r = await client.test.test.insert_one(d)
    print(r.inserted_id)
    return {"message": "Hello World"}
