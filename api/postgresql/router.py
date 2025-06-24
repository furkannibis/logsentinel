from fastapi import APIRouter
from parser.linux.postgre import SLOG_PSQL


postgresql_router = APIRouter()

@postgresql_router.get("/log/postgresql")
async def postgresql_main_router():
    psql_log = SLOG_PSQL()
    return psql_log.psql