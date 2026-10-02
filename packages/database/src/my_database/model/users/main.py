from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from my_database.db import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict


class User(Base):
    __tablename__ = "USERS"

    user_id = Column("user_id", Integer, primary_key=True, index=True)
    first_name = Column("first_name", String(45))
    last_name = Column("last_name", String(45))
    mobile_number = Column("mobile_number", String(45), unique=True)
    gender = Column("gender", Boolean)
    is_active = Column("is_active", Boolean)
    is_head = Column("is_head", Boolean)
    parent_id = Column(
        "parent_id",
        Integer,
        ForeignKey("USERS.user_id"),
        nullable=False,
    )

    parent = relationship("User", remote_side="User.user_id", back_populates="children")
    children = relationship("User", back_populates="parent")
