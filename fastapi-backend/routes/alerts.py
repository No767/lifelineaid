import asyncpg
from fastapi import APIRouter, Request, status as fastapi_status
from fastapi.responses import ORJSONResponse, Response

from utils import CreateAlertModel

alerts_router = APIRouter(prefix="/alerts", default_response_class=ORJSONResponse)


@alerts_router.post("/create")
async def create_alert(json_request: CreateAlertModel, request: Request) -> Response:
    """Creates a new alert with the specified JSON model"""
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
        return Response(status_code=fastapi_status.HTTP_201_CREATED)
    return Response(status_code=fastapi_status.HTTP_202_ACCEPTED)


@alerts_router.get("/search")
async def search_alerts(title: str, request: Request) -> ORJSONResponse:
    """Using full-text search, searches for an alert that has the given title"""
    sql = """
    SELECT title, description, created_at
    FROM alert
    WHERE title % $1
    ORDER BY similarity(title, $1) DESC
    LIMIT 100;
    """
    pool: asyncpg.Pool = request.app.pool_state["pool"]
    rows = await pool.fetch(sql, title)
    return ORJSONResponse(rows)
