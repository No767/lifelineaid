import asyncpg
from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from utils import CreateAlertModel

alerts_router = APIRouter(prefix="/alerts", default_response_class=ORJSONResponse)


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
