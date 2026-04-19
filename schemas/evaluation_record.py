from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


# ✅ Request Schema
class EvaluateRecordRequest(BaseModel):
    event_date: date = Field(..., description="Date when the event occurred")
    delay_reason: Optional[str] = Field(
        None,
        description="Reason for delay (optional)"
    )


# ✅ Success Response Schema
class EvaluationResponse(BaseModel):
    submission_date: date = Field(..., description="Auto-generated submission date")
    final_status: str = Field(..., description="Workflow decision (PASS / REVIEW / BLOCK)")
    delay_days: int = Field(..., description="Number of delayed days")
    reason_flag: str = Field(..., description="Indicates if reason was provided (Yes / No)")
    score: int = Field(..., description="Score based on workflow decision")


# ✅ Error Response Schema (Optional - for documentation purpose)
class ErrorResponse(BaseModel):
    error: str = Field(..., example="VALIDATION_ERROR")
    message: str = Field(..., example="Event_Date cannot be in the future")