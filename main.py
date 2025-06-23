from fastapi import FastAPI

from api.postgresql.router import postgresql_router

from parser.log_sentinel import Logsentinel

log_sentinel_parser = Logsentinel()

app = FastAPI()
app.include_router(router=postgresql_router)

@app.get("/")
async def root():
    return {"message": "hello, world!"}
