from datetime import date
from typing import Optional


class ValidationService:

    @staticmethod
    def validate_dates(event_date: date, submission_date: date):
        today = date.today()

        # submission_date must be >= event_date
        if submission_date < event_date:
            raise ValueError("Submission_Date cannot be earlier than Event_Date")

        # dates must not be in the future
        if event_date > today:
            raise ValueError("Event_Date cannot be in the future")

        if submission_date > today:
            raise ValueError("Submission_Date cannot be in the future")

    @staticmethod
    def validate_reason(delay_reason: Optional[str]):

        if delay_reason is not None and not isinstance(delay_reason, str):
            raise ValueError("Delay_Reason must be a string")

    @staticmethod
    def is_reason_missing(delay_reason: Optional[str]) -> bool:

        if delay_reason is None:
            return True

        if delay_reason.strip() == "":
            return True

        return False