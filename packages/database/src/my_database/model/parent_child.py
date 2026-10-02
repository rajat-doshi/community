from sqlalchemy import Column, Boolean, ForeignKey, Integer
from my_database.db import Base
from my_database.model.member import Members


class ParentChild(Base):
    """
    Parent Child model
    """

    __tablename__ = "PARENT_CHILD"
    parent_child_id = Column("parent_child_id", Integer, primary_key=True, index=True)
    father_id = Column("father_id", Integer, ForeignKey(Members.member_id), nullable=False)
    mother_id = Column("mother_id", Integer, ForeignKey(Members.member_id), nullable=False)
    child_id = Column("child_id", Integer, ForeignKey(Members.member_id), nullable=False)
    is_active = Column("is_active", Boolean, default=True)
