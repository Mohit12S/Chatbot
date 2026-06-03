"""
Hugging Face API integration service using OpenAI client
"""
from openai import OpenAI
import logging
from config.settings import settings

logger = logging.getLogger(__name__)


class HuggingFaceService:
    """Service for interacting with Hugging Face using OpenAI compatible API"""
    
    def __init__(self):
        """Initialize the Hugging Face service with OpenAI client"""
        self.api_key = settings.HF_TOKEN
        self.model = settings.HUGGINGFACE_MODEL
        self.system_prompt = settings.SYSTEM_PROMPT
        
        if not self.api_key:
            raise ValueError("HF_TOKEN not set in environment variables")
        
        # Initialize OpenAI client with Hugging Face router
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=self.api_key,
        )
    
    def generate_response(self, user_message: str) -> str:
        """
        Generate AI response using Hugging Face with OpenAI API
        
        Args:
            user_message: The user's input message
            
        Returns:
            The AI-generated response
            
        Raises:
            Exception: If API call fails
        """
        try:
            logger.info(f"Calling model: {self.model}")
            
            # Use OpenAI client to call Hugging Face
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                temperature=0.7,
                max_tokens=2560,
            )
            
            # Extract response text
            answer = response.choices[0].message.content.strip()
            print(answer , "************")
            
            logger.info("Successfully generated response from Hugging Face API")
            return answer[:1000]  # Limit response length
            
        except Exception as e:
            logger.error(f"Error calling Hugging Face API: {str(e)}")
            raise Exception(f"AI service error: {str(e)}")
