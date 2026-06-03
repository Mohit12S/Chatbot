# Backend Setup Instructions

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Hugging Face API key
- Firebase project credentials

## Step 1: Create Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **python-dotenv**: Environment variable management
- **requests**: HTTP library
- **firebase-admin**: Firebase SDK
- **python-multipart**: Form data handling

## Step 3: Configure Environment Variables

```bash
# Copy example file
cp .env.example .env

# Edit .env with your credentials (use any text editor)
```

### Required Environment Variables

#### Hugging Face Setup

1. Visit https://huggingface.co/join and create account
2. Go to Settings → Access Tokens
3. Create new token with "read" permission
4. Add to `.env`:

```env
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxx
HUGGINGFACE_MODEL=meta-llama/Llama-2-7b-chat-hf
```

**Alternative models** (faster/lighter):
- `mistralai/Mistral-7B-Instruct-v0.1`
- `NousResearch/Nous-Hermes-2-Mistral-7B-DPO`
- `google/flan-t5-small` (fast, good for testing)

#### Firebase Setup

1. Go to https://console.firebase.google.com
2. Create new project
3. Enable Firestore Database
4. Go to Project Settings → Service Accounts
5. Click "Generate new private key"
6. Open downloaded JSON file and copy values:

```env
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY_ID=xxxxx
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIExxx...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-admin@your-project.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=123456789
```

**Important**: The `FIREBASE_PRIVATE_KEY` should have actual newlines. When copying from JSON:
- Replace `\n` with actual newlines, OR
- Use: `python -c "import json; print(json.load(open('key.json'))['private_key'])"`

7. In Firebase Console, create collection named "chats"

## Step 4: Run Backend

```bash
# Make sure venv is activated
python app.py

# Or use uvicorn directly
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Server runs at: http://localhost:8000

## Step 5: Test Backend

### Using curl
```bash
# Health check
curl http://localhost:8000/

# Test chat endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Hello!\"}"
```

### View API Documentation
Open: http://localhost:8000/docs (interactive API docs)

## Troubleshooting

### "ModuleNotFoundError: No module named 'fastapi'"
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

### "HUGGINGFACE_API_KEY not set"
- Check `.env` file has the key
- Verify key is valid on huggingface.co

### Firebase Connection Error
- Verify all Firebase credentials in `.env`
- Check Firebase project allows Firestore read/write
- Ensure "chats" collection exists

### "Connection refused" to API
- Check backend is running
- Verify port 8000 is not in use
- Try different port: `python app.py --port 8001`

## Project Structure

```
backend/
├── app.py                     # Main application entry point
├── requirements.txt           # Python dependencies
├── .env.example              # Example environment variables
├── .env                      # Your environment variables (don't commit!)
├── config/
│   ├── __init__.py
│   └── settings.py           # Load & manage settings
├── models/
│   ├── __init__.py
│   └── schemas.py            # Pydantic validation models
├── routes/
│   ├── __init__.py
│   └── chat.py               # Chat endpoint handlers
└── services/
    ├── __init__.py
    ├── huggingface_service.py# HF API integration
    └── firebase_service.py   # Firebase integration
```

## File Descriptions

### `app.py`
Main FastAPI application. Sets up CORS, routes, and error handling.

### `config/settings.py`
Loads environment variables and provides centralized configuration.

### `models/schemas.py`
Pydantic models for request/response validation.

### `services/huggingface_service.py`
Handles API calls to Hugging Face including prompt engineering.

### `services/firebase_service.py`
Handles saving and retrieving chat messages from Firestore.

### `routes/chat.py`
API endpoints: POST /api/chat and GET /api/health

## Key Endpoints

### POST /api/chat
Send a message and get AI response.

**Request:**
```json
{
  "message": "What is Python?"
}
```

**Response:**
```json
{
  "answer": "Python is a high-level programming language known for its simplicity and readability..."
}
```

### GET /api/health
Check if all services are running.

**Response:**
```json
{
  "status": "healthy",
  "services": {
    "huggingface": true,
    "firebase": true
  }
}
```

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| HUGGINGFACE_API_KEY | Your HF API token | hf_xxxx |
| HUGGINGFACE_MODEL | Model to use | meta-llama/Llama-2-7b-chat-hf |
| FIREBASE_PROJECT_ID | Firebase project ID | my-project-123 |
| FIREBASE_PRIVATE_KEY_ID | Private key ID | xxxxx |
| FIREBASE_PRIVATE_KEY | Private key (include newlines) | ----BEGIN... |
| FIREBASE_CLIENT_EMAIL | Service account email | xxxxx@appspot.gserviceaccount.com |
| FIREBASE_CLIENT_ID | Client ID | 123456789 |
| API_HOST | Server host | 0.0.0.0 |
| API_PORT | Server port | 8000 |
| DEBUG | Enable debug mode | True |
| FRONTEND_URL | Frontend URL for CORS | http://localhost:5173 |

## Production Deployment

See main README.md for deployment to:
- Render
- Railway
- Fly.io

## Next Steps

1. Start frontend development server
2. Test chat functionality
3. Check Firebase console for saved messages
4. Deploy when ready

---

For issues, check logs in the terminal where backend is running.
