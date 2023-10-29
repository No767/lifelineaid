import asyncpg
from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from utils import CreatePinModel, PinInfo

pins_router = APIRouter(prefix="/pins", default_response_class=ORJSONResponse)


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
