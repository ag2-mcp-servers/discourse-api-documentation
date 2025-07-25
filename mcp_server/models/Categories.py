# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:33:14+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Category(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    can_edit: bool
    color: str
    default_list_filter: str
    default_top_period: str
    default_view: Optional[str] = None
    description: Optional[str] = None
    description_excerpt: Optional[str] = None
    description_text: Optional[str] = None
    has_children: bool
    id: int
    is_uncategorized: Optional[bool] = None
    minimum_required_tags: int
    name: str
    navigate_to_first_post_after_read: bool
    notification_level: int
    num_featured_topics: int
    permission: int
    position: int
    post_count: int
    read_restricted: bool
    show_subcategory_list: bool
    slug: str
    sort_ascending: Optional[str] = None
    sort_order: Optional[str] = None
    subcategory_ids: List
    subcategory_list: Optional[List[Any]] = None
    subcategory_list_style: str
    text_color: str
    topic_count: int
    topic_template: Optional[str] = None
    topic_url: Optional[str] = None
    topics_all_time: int
    topics_day: int
    topics_month: int
    topics_week: int
    topics_year: int
    uploaded_background: Optional[str] = None
    uploaded_logo: Optional[str] = None
    uploaded_logo_dark: Optional[str] = None


class CategoryList(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    can_create_category: bool
    can_create_topic: bool
    categories: List[Category]


class JsonGetResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    category_list: CategoryList


class Permissions(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    everyone: Optional[int] = Field(None, examples=[1])
    staff: Optional[int] = None


class JsonPostRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    allow_badges: Optional[bool] = None
    color: Optional[str] = Field(None, examples=['49d9e9'])
    form_template_ids: Optional[List] = None
    name: str
    parent_category_id: Optional[int] = None
    permissions: Optional[Permissions] = None
    search_priority: Optional[int] = None
    slug: Optional[str] = None
    text_color: Optional[str] = Field(None, examples=['f0fcfd'])
    topic_featured_links_allowed: Optional[bool] = None


class GroupPermission(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    group_name: str
    permission_type: int


class RequiredTagGroup(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    min_count: int
    name: str


class CategoryModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    all_topics_wiki: bool
    allow_badges: bool
    allow_global_tags: Optional[bool] = None
    allow_unlimited_owner_edits_on_first_post: bool
    allowed_tag_groups: Optional[List] = None
    allowed_tags: Optional[List] = None
    auto_close_based_on_last_post: bool
    auto_close_hours: Optional[str] = None
    available_groups: List
    can_delete: bool
    can_edit: bool
    color: str
    custom_fields: Dict[str, Any]
    default_list_filter: str
    default_slow_mode_seconds: Optional[str] = None
    default_top_period: str
    default_view: Optional[str] = None
    description: Optional[str] = None
    description_excerpt: Optional[str] = None
    description_text: Optional[str] = None
    email_in: Optional[str] = None
    email_in_allow_strangers: bool
    form_template_ids: Optional[List] = None
    group_permissions: List[GroupPermission]
    has_children: Optional[str] = None
    id: int
    mailinglist_mirror: bool
    minimum_required_tags: int
    name: str
    navigate_to_first_post_after_read: bool
    notification_level: int
    num_featured_topics: int
    permission: Optional[int] = None
    position: int
    post_count: int
    read_only_banner: Optional[str] = None
    read_restricted: bool
    required_tag_groups: List[RequiredTagGroup]
    search_priority: int
    show_subcategory_list: bool
    slug: str
    sort_ascending: Optional[str] = None
    sort_order: Optional[str] = None
    subcategory_list_style: str
    text_color: str
    topic_count: int
    topic_featured_link_allowed: bool
    topic_template: Optional[str] = None
    topic_url: Optional[str] = None
    uploaded_background: Optional[str] = None
    uploaded_logo: Optional[str] = None
    uploaded_logo_dark: Optional[str] = None


class JsonPostResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    category: CategoryModel
