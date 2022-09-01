from sqlalchemy import BigInteger, Integer, Column, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Moderator(Base):
    id = Column(Integer, primary_key=True, index=True)
    vk_id = Column(BigInteger, index=True)
    steamid = Column(BigInteger, index=True)
    is_superuser = Column(Boolean, default=False)
    # checks = relationship("Checks")  # TODO: добавить
