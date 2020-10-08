from typing import List

import pydantic


class ErrorDetail(pydantic.BaseModel):
    msg: str
    type: str


class Exception(pydantic.BaseModel):
    detail: List[ErrorDetail]
