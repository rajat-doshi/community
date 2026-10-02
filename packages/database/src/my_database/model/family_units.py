from sqlalchemy import Boolean, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from my_database.db import Base


class FamilyUnits(Base):
    """
    Family Units model
    """

    __tablename__ = "FAMILY_UNITS"
    family_unit_id: Mapped[int] = mapped_column("family_unit_id", primary_key=True, index=True)
    family_name: Mapped[str] = mapped_column("family_name", String(45))
    is_active: Mapped[bool] = mapped_column("is_active", Boolean, default=True)
