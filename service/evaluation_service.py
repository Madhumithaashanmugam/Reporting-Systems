from datetime import date
from service.validation_service import ValidationService
from service.scoring_service import ScoringService


class EvaluationService:

    @staticmethod
    def calculate_delay_days(event_date: date, submission_date: date) -> int:
        return (submission_date - event_date).days

    @staticmethod
    def evaluate(event_date: date, delay_reason: str):

        submission_date = date.today()

        # Validations (will raise HTTPException automatically)
        ValidationService.validate_dates(event_date, submission_date)
        ValidationService.validate_reason(delay_reason)

        delay_days = EvaluationService.calculate_delay_days(
            event_date,
            submission_date
        )

        reason_missing = ValidationService.is_reason_missing(delay_reason)

        # Business rules
        if delay_days <= 2:
            status = "PASS"
        else:
            status = "BLOCK" if reason_missing else "REVIEW"

        reason_flag = "No" if reason_missing else "Yes"

        score = ScoringService.get_score(status)

        return {
            "submission_date": submission_date,
            "final_status": status,   # ✅ FIXED KEY
            "delay_days": delay_days,
            "reason_flag": reason_flag,
            "score": score
        }