import datetime
from enum import IntEnum
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, select, DateTime
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base


class AdminAudit(BaseModel):
    id: int
    action: str
    created_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)


class BanActionAudit(BaseModel):
    id: int
    ban_id: int
    action: str
    created_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)


class Ban(BaseModel):
    id: int
    target_discord_id: int
    target_user_name: str
    target_user_display_name: str
    author_discord_id: int
    author_discord_name: str
    reason: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    expires_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)


class Banpool(BaseModel):
    id: int
    name: str
    description: str
    model_config = ConfigDict(from_attributes=True)
    bans: list[Ban]

class BanpoolSubscriptionLevel(IntEnum):
    ALERT = 1
    BAN = 2

class BanpoolSubscription(BaseModel):
    id: int
    banpool_id: int
    created_at: datetime.datetime
    author_discord_id: int
    author_discord_name: str
    guild_id: int
    guild_name: str
    model_config = ConfigDict(from_attributes=True)


class GuildNotificationChannel(BaseModel):
    id: int
    guild_id: int
    channel_id: int
    model_config = ConfigDict(from_attributes=True)


class GuildNotificationRole(BaseModel):
    id: int
    guild_id: int
    role_id: int
    model_config = ConfigDict(from_attributes=True)
