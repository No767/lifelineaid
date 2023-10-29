import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

import asyncpg
from dotenv import load_dotenv
from fastapi import FastAPI

from routes import alerts_router, pins_router
from utils import PoolState

load_dotenv()

COCKROACH_URI = os.environ["COCKROACH_URI"]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[PoolState]:
    async with asyncpg.create_pool(dsn=COCKROACH_URI, max_size=25, min_size=25) as pool:
        app.pool_state = {"pool": pool}
        yield app.pool_state


app = FastAPI(lifespan=lifespan)
app.include_router(pins_router)
app.include_router(alerts_router)
