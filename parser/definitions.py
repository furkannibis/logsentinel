from pydantic import BaseModel
from typing import Union, List


class LOG_SENTINEL_DEF(BaseModel):
    buffer: int = 1000