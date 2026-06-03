"""
FastAPI application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from config.settings import settings
from routes.chat import router as chat_router

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Chatbot API",
    description="A simple AI chatbot API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info(f"CORS configured for origins: {settings.ALLOWED_ORIGINS}")

# Include routes
app.include_router(chat_router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Chatbot API",
        "docs": "/docs",
        "health": "/api/health",
    }


@app.on_event("startup")
async def startup_event():
    """Startup event"""
    logger.info("Application starting up")
    logger.info(f"Using Hugging Face model: {settings.HUGGINGFACE_MODEL}")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    logger.info("Application shutting down")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
