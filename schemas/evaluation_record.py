from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class EvaluateRecordRequest(BaseModel):
    event_date: date = Field(..., description="Date when the event occurred (YYYY-MM-DD)")
    submission_date: date = Field(..., description="Date when the record was submitted (YYYY-MM-DD)")
    delay_reason: Optional[str] = Field(None, description="Reason for delay if submission is late")


class EvaluateRecordResponse(BaseModel):
    final_status: str
    delay_days: int
    reason_flag: str
    score: int


class ValidationErrorResponse(BaseModel):
    error: str = "VALIDATION_ERROR"
    message: str