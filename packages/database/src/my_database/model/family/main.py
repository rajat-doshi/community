from sqlalchemy import Column,  Boolean, JSON, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, mapped_column
from my_database.db import Base

class Family(Base):
    """
    Family model
    """
    __tablename__ = "FAMILY"

    family_id : Mapped[int] = mapped_column('family_id',primary_key=True, index=True);
    family_members_list = Column("family_members_list", JSON);
    is_active = Column("is_active", Boolean);

    self_user_id: Mapped[int] = mapped_column(ForeignKey("USERS.user_id", ondelete="CASCADE"));
    last_family_head_id: Mapped[int] = mapped_column(ForeignKey("USERS.user_id", ondelete="CASCADE"));
    family_head_id: Mapped[int] = mapped_column(ForeignKey("USERS.user_id", ondelete="CASCADE"));