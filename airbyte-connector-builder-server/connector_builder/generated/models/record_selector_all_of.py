# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.dpath_extractor import DpathExtractor
from connector_builder.generated.models.record_filter import RecordFilter


class RecordSelectorAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RecordSelectorAllOf - a model defined in OpenAPI

        extractor: The extractor of this RecordSelectorAllOf.
        record_filter: The record_filter of this RecordSelectorAllOf [Optional].
    """

    extractor: DpathExtractor
    record_filter: Optional[RecordFilter] = None

RecordSelectorAllOf.update_forward_refs()
