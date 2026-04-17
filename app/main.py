from fastapi import FastAPI
from routers import subject


app = FastAPI()


app.include_router(subject.router)