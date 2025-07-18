# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:33:14+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Enabled(Enum):
    true = 'true'
    false = 'false'


class Status(Enum):
    closed = 'closed'
    pinned = 'pinned'
    pinned_globally = 'pinned_globally'
    archived = 'archived'
    visible = 'visible'


class JsonPutRequest(BaseModel):
    enabled: Enabled
    status: Status
    until: Optional[str] = Field(
        None,
        description='Only required for `pinned` and `pinned_globally`',
        examples=['2030-12-31'],
    )


class JsonPutResponse(BaseModel):
    success: Optional[str] = Field(None, examples=['OK'])
    topic_status_update: Optional[str] = None
