import reflex as rx
from datetime import datetime, timezone
from sqlmodel import Field

import sqlalchemy

def get_utc_now() -> datetime:
  return datetime.now(timezone.utc)

class ContactEntryModel(rx.Model, table=True):
  first_name: str
  last_name: str
  email: str
  message: str
  created_at: datetime = Field(
    default_factory=get_utc_now,
    sa_type=sqlalchemy.DateTime(timezone=True),
    sa_column_kwargs={
      'server_default': sqlalchemy.func.now()
    },
    nullable=False
  )
