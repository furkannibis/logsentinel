from pydantic import BaseModel
from typing import Union, List


class PSQL_DEF(BaseModel):
    path: Union[List[str]]
    buffer: int = 1000