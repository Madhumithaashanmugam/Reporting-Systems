from fastapi import FastAPI
from router.evaluation_api import router as evaluation_router

app = FastAPI(
    title="Validation Workflow Engine",
    version="1.0"
)

app.include_router(evaluation_router)