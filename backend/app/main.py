from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth

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

app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "AI Task Manager Backend is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
