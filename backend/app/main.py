import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< Updated upstream
from sqlalchemy.exc import OperationalError
from app.models.base import BaseModel
from app.db.session import engine
from app.models import user

from app.api.v1.auth import router as auth_router
from app.api.schedule_routes import router as schedule_router
from app.api.task_routes import router as task_router
=======

from app.api.v1 import auth
>>>>>>> Stashed changes

# Create FastAPI app instance
app = FastAPI(
    title="AI Task Manager Backend",
    description="Backend API for AI Task Manager application",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< Updated upstream
# Include Routers
app.include_router(auth_router)
app.include_router(schedule_router)
app.include_router(task_router)
=======
app.include_router(auth.router, prefix="/api/v1")
>>>>>>> Stashed changes

@app.get("/")
async def root():
    return {"message": "AI Task Manager Backend is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is healthy"}

@app.on_event("startup")
async def create_tables():
    max_attempts = 10
    for attempt in range(1, max_attempts + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(BaseModel.metadata.create_all)
            return
        except OperationalError:
            if attempt == max_attempts:
                raise
            await asyncio.sleep(2)

if __name__ == "__main__":
    import uvicorn
<<<<<<< Updated upstream
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
=======
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
>>>>>>> Stashed changes
