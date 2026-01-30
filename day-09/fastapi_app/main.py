# Application Entry Point
from app.api import app
from routers import metrics, aws, logs 
import uvicorn

if __name__ == "__main__":
    # ASGI Web Server
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

    
app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
app.include_router(logs.router) 