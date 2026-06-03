"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str = Field(..., min_length=1, max_length=2000, description="User message")


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    answer: str = Field(..., description="AI generated response")


class ChatMessage(BaseModel):
    """Chat message model for database storage"""
    question: str
    answer: str
    timestamp: str
