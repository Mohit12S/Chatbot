"""
Firebase Firestore integration service
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import logging
from datetime import datetime
from config.settings import settings

logger = logging.getLogger(__name__)


class FirebaseService:
    """Service for interacting with Firebase Firestore"""
    
    def __init__(self):
        """Initialize Firebase connection"""
        try:
            # Check if Firebase is already initialized
            if firebase_admin._apps:
                self.db = firestore.client()
            else:
                # Create credentials from environment variables
                cred_dict = {
                    "type": "service_account",
                    "project_id": settings.FIREBASE_PROJECT_ID,
                    "private_key_id": settings.FIREBASE_PRIVATE_KEY_ID,
                    "private_key": settings.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
                    "client_email": settings.FIREBASE_CLIENT_EMAIL,
                    "client_id": settings.FIREBASE_CLIENT_ID,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                }
                
                cred = credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred)
                self.db = firestore.client()
            
            logger.info("Firebase initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Firebase: {str(e)}")
            raise Exception(f"Firebase initialization error: {str(e)}")
    
    def save_chat(self, question: str, answer: str) -> dict:
        """
        Save a chat message to Firestore
        
        Args:
            question: The user's question
            answer: The AI's answer
            
        Returns:
            Dictionary with the saved data and document ID
            
        Raises:
            Exception: If save operation fails
        """
        try:
            timestamp = datetime.utcnow().isoformat()
            
            chat_data = {
                "question": question,
                "answer": answer,
                "timestamp": timestamp,
            }
            
            # Add to chats collection
            doc_ref = self.db.collection("chats").add(chat_data)
            
            logger.info(f"Chat saved successfully to Firestore")
            
            return {
                "id": doc_ref[1].id,
                "timestamp": timestamp,
                "question": question,
                "answer": answer,
            }
        except Exception as e:
            logger.error(f"Error saving chat to Firestore: {str(e)}")
            raise Exception(f"Error saving chat: {str(e)}")
    
    def get_recent_chats(self, limit: int = 10) -> list:
        """
        Get recent chat messages from Firestore
        
        Args:
            limit: Maximum number of chats to retrieve
            
        Returns:
            List of chat documents
        """
        try:
            docs = (
                self.db.collection("chats")
                .order_by("timestamp", direction=firestore.Query.DESCENDING)
                .limit(limit)
                .stream()
            )
            
            chats = []
            for doc in docs:
                data = doc.to_dict()
                data["id"] = doc.id
                chats.append(data)
            
            logger.info(f"Retrieved {len(chats)} recent chats from Firestore")
            return chats
        except Exception as e:
            logger.error(f"Error retrieving chats from Firestore: {str(e)}")
            raise Exception(f"Error retrieving chats: {str(e)}")
