# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from pydantic import Field
from typetree.dependencies import SchemaConfig
from typetree.aspects.models.urn_bamm_com_catena_x010_context import UrnBammComCatenaX010Context
from typetree.aspects.models.urn_bamm_com_catena_x010_type import UrnBammComCatenaX010Type

def toStr(d: date) -> str:
    return str(d)

class PartTypization(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PartTypization - a model defined in OpenAPI

        catena_x_unique_id: The catena_x_unique_id of this PartTypization.
        local_identifier: The local_identifier of this PartTypization.
        part_name: The part_name of this PartTypization.
        part_name_customer: The part_name_customer of this PartTypization [Optional].
        created_on: The created_on of this PartTypization.
        modified_on: The modified_on of this PartTypization [Optional].
        released_on: The released_on of this PartTypization [Optional].
        type: The type of this PartTypization [Optional].
        version: The version of this PartTypization.
        context: The context of this PartTypization [Optional].
        description: The description of this PartTypization.
    """

    catena_x_unique_id: Optional[str] = Field(None, alias='catenaXUniqueId')
    local_identifier: Optional[list[object]] = Field(None, alias='localIdentifier')
    part_name: Optional[str] = Field(None, alias='partName')
    part_name_customer: Optional[str] = Field(None, alias='partNameCustomer')
    created_on: Optional[str] = Field(None, alias='createdOn')
    modified_on: Optional[str] = Field(None, alias='modifiedOn')
    released_on: Optional[str] = Field(None, alias='releasedOn')
    type: Optional[UrnBammComCatenaX010Type] = None
    version: Optional[str] = None
    context: Optional[UrnBammComCatenaX010Context] = None
    description: Optional[str] = None

    class Config(SchemaConfig):
        ...

    """
    @validator("catena_x_unique_id")
    def catena_x_unique_id_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", value)
        return value
    """

PartTypization.update_forward_refs()