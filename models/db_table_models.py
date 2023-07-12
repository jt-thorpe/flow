"""A class that contains the table definitions for the database."""

import uuid

from sqlalchemy import (UUID, VARCHAR, Boolean, Column, Date, ForeignKey,
                        Integer, MetaData, Table, text)
from sqlalchemy.dialects.postgresql import UUID

"""The metadata object"""
metadata_obj = MetaData()

"""Database table models"""
user_table = Table(
    "username",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    # could be just email as unique... could reduce complexity
    Column("email", VARCHAR(255), nullable=False, unique=True)
)

password_table = Table(
    "password",
    metadata_obj,
    Column("user_id", UUID(as_uuid=True), ForeignKey(
        "username.id"), nullable=False),
    Column("password", VARCHAR(255), nullable=False)
)

transaction_table = Table(
    "transaction",
    metadata_obj,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", UUID(as_uuid=True),
           ForeignKey("username.id"), primary_key=True, default=uuid.uuid4),
    Column("amount", Integer, nullable=False),
    Column("description", VARCHAR(100)),
    Column("date", Date, server_default=text('NOW()'), nullable=False),
    Column("is_income", Boolean, nullable=False)  # True income, False expense
)
