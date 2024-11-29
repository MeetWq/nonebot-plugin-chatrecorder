from collections.abc import Iterable
from datetime import datetime
from typing import Literal

from nonebot.adapters import Message
from nonebot_plugin_uninfo import SceneType, Session
from sqlalchemy.sql import ColumnElement

from .model import MessageRecord

def filter_statement(
    *,
    session: Session | None = None,
    filter_self_id: bool = True,
    filter_adapter: bool = True,
    filter_scope: bool = True,
    filter_scene: bool = True,
    filter_user: bool = True,
    self_ids: Iterable[str] | None = None,
    adapters: Iterable[str] | None = None,
    scopes: Iterable[str] | None = None,
    scene_types: Iterable[int | SceneType] | None = None,
    scene_ids: Iterable[str] | None = None,
    user_ids: Iterable[str] | None = None,
    exclude_self_ids: Iterable[str] | None = None,
    exclude_adapters: Iterable[str] | None = None,
    exclude_scopes: Iterable[str] | None = None,
    exclude_scene_types: Iterable[str] | None = None,
    exclude_scene_ids: Iterable[str] | None = None,
    exclude_user_ids: Iterable[str] | None = None,
    time_start: datetime | None = None,
    time_stop: datetime | None = None,
    types: Iterable[Literal["message", "message_sent"]] | None = None,
) -> list[ColumnElement[bool]]: ...
async def get_message_records(
    *,
    session: Session | None = None,
    filter_self_id: bool = True,
    filter_adapter: bool = True,
    filter_scope: bool = True,
    filter_scene: bool = True,
    filter_user: bool = True,
    self_ids: Iterable[str] | None = None,
    adapters: Iterable[str] | None = None,
    scopes: Iterable[str] | None = None,
    scene_types: Iterable[int | SceneType] | None = None,
    scene_ids: Iterable[str] | None = None,
    user_ids: Iterable[str] | None = None,
    exclude_self_ids: Iterable[str] | None = None,
    exclude_adapters: Iterable[str] | None = None,
    exclude_scopes: Iterable[str] | None = None,
    exclude_scene_types: Iterable[str] | None = None,
    exclude_scene_ids: Iterable[str] | None = None,
    exclude_user_ids: Iterable[str] | None = None,
    time_start: datetime | None = None,
    time_stop: datetime | None = None,
    types: Iterable[Literal["message", "message_sent"]] | None = None,
) -> list[MessageRecord]: ...
async def get_messages(
    *,
    session: Session | None = None,
    filter_self_id: bool = True,
    filter_adapter: bool = True,
    filter_scope: bool = True,
    filter_scene: bool = True,
    filter_user: bool = True,
    self_ids: Iterable[str] | None = None,
    adapters: Iterable[str] | None = None,
    scopes: Iterable[str] | None = None,
    scene_types: Iterable[int | SceneType] | None = None,
    scene_ids: Iterable[str] | None = None,
    user_ids: Iterable[str] | None = None,
    exclude_self_ids: Iterable[str] | None = None,
    exclude_adapters: Iterable[str] | None = None,
    exclude_scopes: Iterable[str] | None = None,
    exclude_scene_types: Iterable[str] | None = None,
    exclude_scene_ids: Iterable[str] | None = None,
    exclude_user_ids: Iterable[str] | None = None,
    time_start: datetime | None = None,
    time_stop: datetime | None = None,
    types: Iterable[Literal["message", "message_sent"]] | None = None,
) -> list[Message]: ...
async def get_messages_plain_text(
    *,
    session: Session | None = None,
    filter_self_id: bool = True,
    filter_adapter: bool = True,
    filter_scope: bool = True,
    filter_scene: bool = True,
    filter_user: bool = True,
    self_ids: Iterable[str] | None = None,
    adapters: Iterable[str] | None = None,
    scopes: Iterable[str] | None = None,
    scene_types: Iterable[int | SceneType] | None = None,
    scene_ids: Iterable[str] | None = None,
    user_ids: Iterable[str] | None = None,
    exclude_self_ids: Iterable[str] | None = None,
    exclude_adapters: Iterable[str] | None = None,
    exclude_scopes: Iterable[str] | None = None,
    exclude_scene_types: Iterable[str] | None = None,
    exclude_scene_ids: Iterable[str] | None = None,
    exclude_user_ids: Iterable[str] | None = None,
    time_start: datetime | None = None,
    time_stop: datetime | None = None,
    types: Iterable[Literal["message", "message_sent"]] | None = None,
) -> list[str]: ...
