from fastapi import APIRouter
from schemas.evaluation_record import (
    EvaluateRecordRequest,
    EvaluateRecordResponse,
    ValidationErrorResponse
)

from service.evaluation_service import EvaluationService
from service.scoring_service import ScoringService

router = APIRouter()


@router.post(
    "/evaluate-record",
    response_model=EvaluateRecordResponse,
    responses={400: {"model": ValidationErrorResponse}}
)
def evaluate_record_api(payload: EvaluateRecordRequest):

    try:

        result = EvaluationService.evaluate(
            payload.event_date,
            payload.submission_date,
            payload.delay_reason
        )

        return {
            "final_status": result["status"],
            "delay_days": result["delay_days"],
            "reason_flag": result["reason_flag"],
            "score": ScoringService.get_score(result["status"])
        }

    except ValueError as e:
        return {
            "error": "VALIDATION_ERROR",
            "message": str(e)
        }