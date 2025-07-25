# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:33:14+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Metadata(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    sha1_checksum: Optional[str] = Field(
        None,
        alias='sha1-checksum',
        description='The SHA1 checksum of the upload binary blob. Optionally\nbe provided and serves as an additional security check when\nlater processing the file in complete-external-upload endpoint.',
    )


class Type(Enum):
    avatar = 'avatar'
    profile_background = 'profile_background'
    card_background = 'card_background'
    custom_emoji = 'custom_emoji'
    composer = 'composer'


class JsonPostRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    file_name: str = Field(..., examples=['IMG_2021.jpeg'])
    file_size: int = Field(
        ..., description='File size should be represented in bytes.', examples=[4096]
    )
    metadata: Optional[Metadata] = None
    type: Type


class JsonPostResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    key: Optional[str] = Field(
        None,
        description='The path of the temporary file on the external storage\nservice.',
        examples=['temp/site/uploads/default/12345/67890.jpg'],
    )
    unique_identifier: Optional[str] = Field(
        None,
        description='A unique string that identifies the external upload.\nThis must be stored and then sent in the /complete-external-upload\nendpoint to complete the direct upload.',
        examples=['66e86218-80d9-4bda-b4d5-2b6def968705'],
    )
    url: Optional[str] = Field(
        None,
        description='A presigned PUT URL which must be used to upload\nthe file binary blob to.',
        examples=[
            'https://file-uploads.s3.us-west-2.amazonaws.com/temp/site/uploads/default/123/456.jpg?x-amz-acl=private&x-amz-meta-sha1-checksum=sha1&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AAAAus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211221T011246Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=12345678'
        ],
    )
