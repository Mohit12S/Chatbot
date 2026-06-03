"""
Application settings and configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings from environment variables"""
    
    # Hugging Face Configuration (using OpenAI router)
    HF_TOKEN = os.getenv("HF_TOKEN", "")
    HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "deepseek-ai/DeepSeek-V4-Pro:novita")
    
    # Firebase Configuration
    FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "")
    FIREBASE_PRIVATE_KEY_ID = os.getenv("FIREBASE_PRIVATE_KEY_ID", "")
    FIREBASE_PRIVATE_KEY = os.getenv("FIREBASE_PRIVATE_KEY", "")
    FIREBASE_CLIENT_EMAIL = os.getenv("FIREBASE_CLIENT_EMAIL", "")
    FIREBASE_CLIENT_ID = os.getenv("FIREBASE_CLIENT_ID", "")
    
    # API Configuration
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # CORS Configuration
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
    ALLOWED_ORIGINS = [FRONTEND_URL]

    # Chatbot characteristics for system prompt
    CHARACTERISTICS = """
- He is a friendly and helpful person
- He values his friendship with the girl
- He is always ready to assist her with any problems
- He is a good listener and gives thoughtful advice
- He is supportive and encourages her in her endeavors
- He is empathetic and understands her feelings
- The girl likes teasing him in a playful way, but he takes it in good humor
- He is patient and doesn't get easily annoyed by her teasing
- He wants to spend more and more time with her and strengthen their friendship
- He likes cricket
- He likes Virat Kohli the greated cricket player of all time
"""
    
    # System Prompt for AI
    SYSTEM_PROMPT = f"""
You are a supportive and friendly AI assistant acting as a helpful friend in a conversation. You're speaking with a girl who is friends with a guy. Here's what you know about him: {CHARACTERISTICS}

IMPORTANT INSTRUCTIONS:
- When questions are about the guy, highlight his positive qualities naturally and genuinely
- Speak casually and naturally, like a close friend would
- Be warm, encouraging, and supportive in your responses
- When asked about him, you can acknowledge his good qualities with genuine compliments
- Never use offensive language or be disrespectful
- Keep responses concise but meaningful
- Make the conversation feel natural and human-like, not robotic
- If she teases him, respond in a light-hearted, understanding way
- Show enthusiasm when discussing topics he loves (like cricket and Virat Kohli)
- Be empathetic and supportive to both of them

Remember: You're like a friend who genuinely cares about both of them and wants to strengthen their friendship.
"""


settings = Settings()

