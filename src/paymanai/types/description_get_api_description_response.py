# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DescriptionGetAPIDescriptionResponse"]


class DescriptionGetAPIDescriptionResponse(BaseModel):
    description: Optional[str] = None

    openapi_spec: Optional[Dict[str, object]] = FieldInfo(alias="openAPISpec", default=None)

    version: Optional[str] = None
