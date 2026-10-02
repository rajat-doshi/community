from sqlalchemy import Column, Integer, String, Boolean
from my_database.db import Base


class Members(Base):
    __tablename__ = "MEMBERS"

    member_id = Column("member_id", Integer, primary_key=True, index=True)
    first_name = Column("first_name", String(45))
    last_name = Column("last_name", String(45))
    mobile_number = Column("mobile_number", String(45), unique=True)
    gender = Column("gender", Boolean)
    is_active = Column("is_active", Boolean)
