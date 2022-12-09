# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring


class BearerAuthenticatorAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    BearerAuthenticatorAllOf - a model defined in OpenAPI

        api_token: The api_token of this BearerAuthenticatorAllOf.
        config: The config of this BearerAuthenticatorAllOf.
    """

    api_token: AnyOfInterpolatedStringstring = Field(alias="api_token")
    config: Dict[str, Any] = Field(alias="config")

BearerAuthenticatorAllOf.update_forward_refs()