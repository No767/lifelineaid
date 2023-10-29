import asyncio
import uvloop
import asyncpg
import os
from dotenv import load_dotenv
from pathlib import Path
import orjson
from typing import Any, TypedDict

import shapely.geometry
from shapely.geometry import Point
import shapely.wkb
from shapely.geometry.base import BaseGeometry
from shapely.wkt import dumps, loads

class PinDict(TypedDict):
    point: str
    title: str
    description: str
    
class PinInfo:
    __slots__ = ("point", "title", "description")
    
    def __init__(self, entry: PinDict):
        self.point = entry["point"]
        self.title = entry["title"]
        self.description = entry["description"]
        
    def to_dict(self):
        parsed_point = loads(self.point)
        return {
            "point": (parsed_point.x, parsed_point.y),
            "title": self.title,
            "description": self.description
        }

ENV_PATH = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=ENV_PATH)

COCKROACH_URI = os.environ["COCKROACH_URI"]

async def init_codecs(conn: asyncpg.connection.Connection):
    
    def encode_geometry(geometry: Any) -> bytes:
        if not hasattr(geometry, '__geo_interface__'):
            raise TypeError(f'{geometry} does not conform to geo interface')
        shape = shapely.geometry.asShape(geometry)
        return shapely.wkb.dumps(shape)


    def decode_geometry(wkb: bytes) -> BaseGeometry:
        return shapely.wkb.loads(wkb)


    await conn.set_type_codec(
        'geometry',  # also works for 'geography'
        schema="",
        encoder=encode_geometry,
        decoder=decode_geometry,
        format='binary',
    )

async def main():
    async with asyncpg.create_pool(dsn=COCKROACH_URI, init=init_codecs) as pool:
        make_point_query = """
        SELECT (SELECT ST_AsText(location_geom)) AS point, title, description
        FROM pin
        LIMIT 100;
        """
        res = await pool.fetch(make_point_query)
        # rows = [PinInfo(row).to_dict() for row in res]
        print(res)
        # print(type(rows))
        
uvloop.run(main())