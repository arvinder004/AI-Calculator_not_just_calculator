'''FASTAPI for api server
Pillow for image processing
Uvicorn to run server
pydantic for schema/type checking
google.generativeai
python-dotenv'''

from contextlib import asynccontextmanager # asynchronous server
from fastapi import FastAPI # api server
from fastapi.middleware.cors import CORSMiddleware # to avoid cors errors
import uvicorn
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    return {'message':'Server is running'}

if __name__ == '__main__':
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload = (ENV == "dev"))    