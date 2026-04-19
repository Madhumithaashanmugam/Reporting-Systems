from fastapi import APIRouter
from schemas.evaluation_record import (
    EvaluateRecordRequest,
    EvaluationResponse,
    ErrorResponse
)
from service.evaluation_service import EvaluationService

router = APIRouter()


@router.post(
    "/evaluate-record",
    response_model=EvaluationResponse,
    responses={422: {"model": ErrorResponse}}   # ✅ use 422
)
def evaluate_record_api(payload: EvaluateRecordRequest):

    result = EvaluationService.evaluate(
        payload.event_date,
        payload.delay_reason
    )

    return {
        "submission_date": result["submission_date"],
        "final_status": result["final_status"],  # ✅ FIXED KEY
        "delay_days": result["delay_days"],
        "reason_flag": result["reason_flag"],
        "score": result["score"]
    }