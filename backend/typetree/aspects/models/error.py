# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Error(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Error - a model defined in OpenAPI

        message: The message of this Error [Optional].
        path: The path of this Error [Optional].
        details: The details of this Error.
        code: The code of this Error [Optional].
    """

    message: Optional[str] = None
    path: Optional[str] = None
    details: Dict[str, Any]
    code: Optional[str] = None

    @validator("message")
    def message_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("path")
    def path_min_length(cls, value):
        assert len(value) >= 1
        return value

Error.update_forward_refs()