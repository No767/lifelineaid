from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from contextlib import asynccontextmanager
import asyncpg
from fastapi.responses import ORJSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

COCKROACH_URI = os.environ["COCKROACH_URI"]

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     pool = await asyncpg.create_pool(dsn=COCKROACH_URI, max_size=25, min_size=25, command_timeout=30)
#     yield
#     await pool.close()
#
# async def init_app():
#     return await asyncpg.create_pool(dsn=COCKROACH_URI, max_size=25, min_size=25)
    
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with asyncpg.create_pool(dsn=COCKROACH_URI, max_size=25, min_size=25) as pool:
        
#         app.state.pool = pool
#         return pool

app = FastAPI()
app.state.help = "help"

# router = APIRouter(prefix="/dev", default_response_class=ORJSONResponse)
    


# # @app.route("/bulk-pins", methods=["GET"])
# # async def bulk_pins(x_coordinate: int, y_coordinate: int) -> None:
class PostPinModel(BaseModel):
    title: str
    description: str
    filter_type: str
    x_coordinate: float
    y_coordinate: float
    
class ShowcaseModel(BaseModel):
    name: str
    description: str


@app.get("/dev/search")
async def showcase_search(q: str):
    sql = """
    SELECT name, description
    FROM devtest
    WHERE name % $1
    ORDER BY similarity(name, $1) DESC
    LIMIT 100;
    """
    conn = await asyncpg.connect(dsn=COCKROACH_URI)
    rows = await conn.fetch(sql, q)

    response = ORJSONResponse(rows)
    await conn.close()
    return response

@app.post("/dev/create")
async def create_showcase(content: ShowcaseModel):
    sql = """
    INSERT INTO devtest (name, description)
    VALUES ($1, $2);
    """

    conn = await asyncpg.connect(dsn=COCKROACH_URI)
    status = await conn.execute(sql, content.name, content.description)
    if status[-1] != "0":
        return ORJSONResponse(content="", status_code=201)
    return ORJSONResponse(content="", status_code=203)

@app.delete("/dev/delete/{id}")
async def delete_showcase(id: int):
    sql = """
    DELETE FROM devtest
    WHERE id = $1;
    """
    conn = await asyncpg.connect(dsn=COCKROACH_URI)
    status = await conn.execute(sql, id)
    if status[-1] != "0":
        return ORJSONResponse(content="", status_code=200)
    return ORJSONResponse(content="", status_code=404)
    
# @app.route("/create_pins", methods=["POST"])
# async def create_pins(content: PostPinModel) -> None:
    
