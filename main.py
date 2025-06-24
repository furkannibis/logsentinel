from fastapi import FastAPI

from api.postgresql.router import postgresql_router

app = FastAPI()
app.include_router(router=postgresql_router)
