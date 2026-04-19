from datetime import date
from service.validation_service import ValidationService


class EvaluationService:

    @staticmethod
    def calculate_delay_days(event_date: date, submission_date: date) -> int:
        return (submission_date - event_date).days

    @staticmethod
    def evaluate(event_date: date, submission_date: date, delay_reason: str):

        # Run validation first
        ValidationService.validate_dates(event_date, submission_date)
        ValidationService.validate_reason(delay_reason)

        delay_days = EvaluationService.calculate_delay_days(event_date, submission_date)

        reason_missing = ValidationService.is_reason_missing(delay_reason)

        # Business rules
        if delay_days <= 2:
            status = "PASS"
        else:
            if reason_missing:
                status = "BLOCK"
            else:
                status = "REVIEW"

        reason_flag = "No" if reason_missing else "Yes"

        return {
            "status": status,
            "delay_days": delay_days,
            "reason_flag": reason_flag
        }