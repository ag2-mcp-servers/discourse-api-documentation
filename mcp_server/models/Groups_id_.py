# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:33:14+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Extras(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    visible_group_names: List


class Group(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    allow_membership_requests: bool
    allow_unknown_sender_topic_replies: bool
    associated_group_ids: Optional[List] = None
    automatic: bool
    automatic_membership_email_domains: Optional[str] = None
    bio_cooked: Optional[str] = None
    bio_excerpt: Optional[str] = None
    bio_raw: Optional[str] = None
    can_admin_group: bool
    can_edit_group: Optional[bool] = None
    can_see_members: bool
    default_notification_level: int
    email_from_alias: Optional[str] = None
    email_password: Optional[str] = None
    email_username: Optional[str] = None
    flair_bg_color: Optional[str] = None
    flair_color: Optional[str] = None
    flair_url: Optional[str] = None
    full_name: Optional[str] = None
    grant_trust_level: Optional[str] = None
    has_messages: bool
    id: int
    imap_enabled: Optional[bool] = None
    imap_last_error: Optional[str] = None
    imap_mailbox_name: str
    imap_mailboxes: List
    imap_new_emails: Optional[str] = None
    imap_old_emails: Optional[str] = None
    imap_port: Optional[str] = None
    imap_server: Optional[str] = None
    imap_ssl: Optional[str] = None
    imap_updated_at: Optional[str] = None
    imap_updated_by: Optional[Dict[str, Any]] = None
    incoming_email: Optional[str] = None
    is_group_owner_display: bool
    is_group_user: bool
    members_visibility_level: int
    membership_request_template: Optional[str] = None
    mentionable: bool
    mentionable_level: int
    message_count: int
    messageable: bool
    messageable_level: int
    muted_category_ids: List
    muted_tags: Optional[List] = None
    name: str
    primary_group: bool
    public_admission: bool
    public_exit: bool
    publish_read_state: bool
    regular_category_ids: List
    regular_tags: Optional[List] = None
    smtp_enabled: Optional[bool] = None
    smtp_port: Optional[str] = None
    smtp_server: Optional[str] = None
    smtp_ssl: Optional[str] = None
    smtp_updated_at: Optional[str] = None
    smtp_updated_by: Optional[Dict[str, Any]] = None
    title: Optional[str] = None
    tracking_category_ids: List
    tracking_tags: Optional[List] = None
    user_count: int
    visibility_level: int
    watching_category_ids: List
    watching_first_post_category_ids: List
    watching_first_post_tags: Optional[List] = None
    watching_tags: Optional[List] = None


class JsonGetResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    extras: Extras
    group: Group


class GroupModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    automatic_membership_email_domains: Optional[str] = Field(
        None, description='pipe|separated'
    )
    bio_raw: Optional[str] = Field(None, description='About Group')
    default_notification_level: Optional[int] = None
    flair_bg_color: Optional[str] = None
    flair_icon: Optional[str] = None
    flair_upload_id: Optional[int] = None
    full_name: Optional[str] = None
    muted_category_ids: Optional[List[int]] = None
    name: str
    owner_usernames: Optional[str] = Field(None, description='comma,separated')
    primary_group: Optional[bool] = None
    public_admission: Optional[bool] = None
    public_exit: Optional[bool] = None
    regular_category_ids: Optional[List[int]] = None
    tracking_category_ids: Optional[List[int]] = None
    usernames: Optional[str] = Field(None, description='comma,separated')
    visibility_level: Optional[int] = None
    watching_category_ids: Optional[List[int]] = None
    watching_first_post_category_ids: Optional[List[int]] = None


class JsonPutRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    group: GroupModel


class JsonPutResponse(BaseModel):
    success: Optional[str] = Field(None, examples=['OK'])
