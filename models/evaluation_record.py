from sqlalchemy import Column, String, Integer, Date, TIMESTAMP
from sqlalchemy.sql import func
import uuid
from config.db.session import Base


class EvaluationRecord(Base):
    __tablename__ = "evaluation_records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)

    event_date = Column(Date, nullable=False)
    submission_date = Column(Date, nullable=False)

    delay_reason = Column(String, nullable=True)

    final_status = Column(String, nullable=False)
    delay_days = Column(Integer, nullable=False)
    reason_flag = Column(String, nullable=False)
    score = Column(Integer, nullable=False)

    created_ts = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_ts = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )