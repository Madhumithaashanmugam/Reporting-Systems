from datetime import date
from typing import Optional
from fastapi import HTTPException, status


class ValidationService:

    @staticmethod
    def validate_dates(event_date: date, submission_date: date):
        today = date.today()

        if submission_date < event_date:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "VALIDATION_ERROR",
                    "message": "Submission_Date cannot be earlier than Event_Date"
                }
            )

        if event_date > today:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "VALIDATION_ERROR",
                    "message": "Event_Date cannot be in the future"
                }
            )

        if submission_date > today:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "VALIDATION_ERROR",
                    "message": "Submission_Date cannot be in the future"
                }
            )

    @staticmethod
    def validate_reason(delay_reason: Optional[str]):
        if delay_reason is not None and not isinstance(delay_reason, str):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": "VALIDATION_ERROR",
                    "message": "Delay_Reason must be a string"
                }
            )

    @staticmethod
    def is_reason_missing(delay_reason: Optional[str]) -> bool:
        return delay_reason is None or delay_reason.strip() == ""