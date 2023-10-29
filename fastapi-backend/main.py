import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

import asyncpg
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import ORJSONResponse

from utils import CreateAlertModel, CreatePinModel, PinInfo, PoolState

load_dotenv()

COCKROACH_URI = os.environ["COCKROACH_URI"]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[PoolState]:
    async with asyncpg.create_pool(dsn=COCKROACH_URI, max_size=25, min_size=25) as pool:
        app.pool_state = {"pool": pool}
        yield app.pool_state


app = FastAPI(lifespan=lifespan)

pins_router = APIRouter(prefix="/pins", default_response_class=ORJSONResponse)
alerts_router = APIRouter(prefix="/alerts", default_response_class=ORJSONResponse)
dev_router = APIRouter(prefix="/dev", default_response_class=ORJSONResponse)


@pins_router.post("/create")
async def create_pin(json_request: CreatePinModel, request: Request):
    # 1. Title
    # 2. Desc
    # 3. filter_type
    # 4. x, 5. y, 6. srid
    # This query makes the SRID from the coords + adds it into the database
    make_point_query = """
        WITH mp_srid AS (
            SELECT ST_MakePoint($4, $5)
        ) 
        INSERT INTO pin (title, description, filter_type, x_coordinate, y_coordinate, location_geom)
        VALUES ($1, $2, $3, $4, $5, (
            SELECT st_makepoint FROM mp_srid
            )
        );
    """
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    await pool.execute(
        make_point_query,
        json_request.title,
        json_request.description,
        json_request.filter_type,
        json_request.x_coordinate,
        json_request.y_coordinate,
    )
    return ORJSONResponse(content="", status_code=200)


@pins_router.get("/fetch")
async def fetch_pins(request: Request):
    # Bulk fetches pins
    query = """
    SELECT (SELECT ST_AsText(location_geom)) AS point, title, description
    FROM pin
    LIMIT 100;
    """
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    res = await pool.fetch(query)
    parsed_records = [PinInfo(row).to_dict() for row in res]
    return ORJSONResponse(content=parsed_records, status_code=200)


@alerts_router.post("/create")
async def create_alert(json_request: CreateAlertModel, request: Request):
    # Sub for user one
    query = """
    INSERT INTO alert (agency_id, title, description, x_coordinate, y_coordinate)
    VALUES (1, $1, $2, $3, $4);
    """
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    status = await pool.execute(
        query,
        json_request.title,
        json_request.description,
        json_request.x_coordinate,
        json_request.y_coordinate,
    )
    if status[-1] != "0":
        return ORJSONResponse(content="", status_code=200)
    return ORJSONResponse(content="", status_code=400)


@alerts_router.get("/search")
async def search_alerts(title: str, request: Request):
    sql = """
    SELECT title, description, created_at
    FROM alert
    WHERE title % $1
    ORDER BY similarity(title, $1) DESC
    LIMIT 100;
    """
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    rows = await pool.fetch(sql, title)
    response = ORJSONResponse(rows)
    return response


app.include_router(pins_router)
app.include_router(dev_router)
app.include_router(alerts_router)
