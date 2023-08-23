"""A class that contains the table definitions for the database."""

import uuid

from sqlalchemy import (UUID, VARCHAR, Column, Date, ForeignKey,
                        Integer, MetaData, Table, text)
from sqlalchemy.dialects.postgresql import UUID

"""The metadata object"""
metadata_obj = MetaData()

# Some constants
USERNAME_ID = "username.id"

"""Database table models"""
user_table = Table(
    "username",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("email", VARCHAR(255), nullable=False, unique=True)
)

password_table = Table(
    "password",
    metadata_obj,
    Column("user_id", UUID(as_uuid=True), ForeignKey(
        USERNAME_ID), nullable=False),
    Column("password", VARCHAR(255), nullable=False)
)

income_table = Table(
    "income",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True),
           ForeignKey(USERNAME_ID), primary_key=True, default=uuid.uuid4),
    Column("amount", Integer, nullable=False),
    Column("date", Date, server_default=text('NOW()'), nullable=False),
    Column("description", VARCHAR(100)),
)

expense_table = Table(
    "expense",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True),
           ForeignKey(USERNAME_ID), primary_key=True, default=uuid.uuid4),
    Column("amount", Integer, nullable=False),
    Column("date", Date, server_default=text('NOW()'), nullable=False),
    Column("description", VARCHAR(100)),
)
