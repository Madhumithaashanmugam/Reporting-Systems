class ScoringService:

    SCORE_MAP = {
        "PASS": 100,
        "REVIEW": 60,
        "BLOCK": 0
    }

    @staticmethod
    def get_score(final_status: str) -> int:
        return ScoringService.SCORE_MAP.get(final_status, 0)