from fastapi import APIRouter

postgresql_router = APIRouter()

@postgresql_router.get("/log/postgresql")
async def postgresql_main_router():
    return {"message": "hello psql"}