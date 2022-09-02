from datetime import datetime, timedelta

from sqlalchemy import BigInteger, Integer, Column, ForeignKey, Text, DateTime

from app.db.base_class import Base


class Token(Base):
    id = Column(Integer, primary_key=True)
    vk_id = Column(BigInteger, ForeignKey("moderators.vk_id", ondelete="CASCADE"))
    bearer_token = Column(Text, nullable=False, unique=True)
    access_token = Column(Text, nullable=False, unique=True)
    expires = Column(
        DateTime,
        default=datetime.now() + timedelta(days=7),
    )
