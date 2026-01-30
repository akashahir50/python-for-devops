from fastapi import APIRouter, HTTPException
from services.log_service import summarize_logs

router = APIRouter(prefix="/logs", tags=["logs"])

@router.get("/", status_code=200)
async def get_logs():  # Added 'async' for best practice
    """
    Analyze application logs and return summary statistics.
    """
    try:
        logs = summarize_logs()
        return logs
    except Exception as e:  # Specific exception handling
        raise HTTPException(
            status_code=500,
            detail=f"Log analysis failed: {str(e)}"
        )

@router.get("/health")
async def logs_health():
    """Health check for log service."""
    return {"status": "healthy", "service": "log-analyzer"}
