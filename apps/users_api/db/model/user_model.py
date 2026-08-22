from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from shared_core.db.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict

class User(Base):
    __tablename__ = "USERS"

    user_id = Column("user_id", Integer, primary_key=True, index=True)
    first_name = Column("first_name", String(45))
    last_name = Column("last_name", String(45))
    mobile_number = Column("mobile_number", String(45), unique=True)
    gender= Column("gender", Boolean)
    is_active = Column("is_active", Boolean)
