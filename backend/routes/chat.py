"""
Chat API routes
"""
from fastapi import APIRouter, HTTPException
from models.schemas import ChatRequest, ChatResponse
from services.huggingface_service import HuggingFaceService
from services.firebase_service import FirebaseService
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["chat"])

# Initialize services
try:
    hf_service = HuggingFaceService()
    firebase_service = FirebaseService()
except Exception as e:
    logger.error(f"Error initializing services: {str(e)}")
    hf_service = None
    firebase_service = None


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint
    
    Receives a user message, generates an AI response using Hugging Face,
    saves the conversation to Firebase, and returns the response.
    
    Args:
        request: ChatRequest containing the user's message
        
    Returns:
        ChatResponse containing the AI's answer
    """
    try:
        # Validate services are initialized
        if not hf_service or not firebase_service:
            raise HTTPException(
                status_code=500,
                detail="Service initialization failed. Check environment variables."
            )
        
        user_message = request.message.strip()
        
        if not user_message:
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )
        
        logger.info(f"Processing message: {user_message[:100]}...")
        
        # Generate AI response
        ai_response = hf_service.generate_response(user_message)
        
        # Save to Firebase
        firebase_service.save_chat(user_message, ai_response)
        
        logger.info("Message processed successfully")
        
        return ChatResponse(answer=ai_response)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing message: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "huggingface": hf_service is not None,
            "firebase": firebase_service is not None,
        }
    }
