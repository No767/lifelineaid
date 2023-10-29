import asyncpg
from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse, Response

from utils import CreatePinModel, PinInfo

pins_router = APIRouter(prefix="/pins", default_response_class=ORJSONResponse)


@pins_router.post("/create")
async def create_pin(json_request: CreatePinModel, request: Request) -> Response:
    """Creates a new pin from the specified JSON model"""
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

    # We should be using transactions here but...
    # Atomic operations should be guaranteed
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    status = await pool.execute(
        make_point_query,
        json_request.title,
        json_request.description,
        json_request.filter_type,
        json_request.x_coordinate,
        json_request.y_coordinate,
    )
    if status[-1] != "0":
        return Response(status_code=status.HTTP_201_OK)
    return Response(status_code=status.HTTP_202_OK)


@pins_router.get("/fetch")
async def fetch_pins(request: Request) -> ORJSONResponse:
    """Returns current pins and their information. Max is 100."""
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
