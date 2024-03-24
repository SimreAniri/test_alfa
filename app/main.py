from fastapi import FastAPI

from app.table.router import router as table_users

app = FastAPI()

app.include_router(table_users)