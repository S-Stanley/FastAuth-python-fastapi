from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import users

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def get():
	return ('API is running')

app.include_router(users.router)