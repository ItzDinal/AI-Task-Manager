import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
from app.models.base import BaseModel
from app.db.session import engine
from app.models import user

from app.api.v1.auth import router as auth_router

# Create FastAPI app instance
app = FastAPI(
    title="AI Task Manager Backend",
    description="Backend API for AI Task Manager application",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth_router)


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
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
