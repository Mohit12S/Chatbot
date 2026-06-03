# AI Chatbot Application - Complete MVP

A production-ready, single-page chatbot application built with React + Vite (frontend), FastAPI (backend), and Hugging Face AI.

## Features

- 💬 Real-time chat interface
- 🤖 AI responses powered by Hugging Face
- 💾 Conversation history saved to Firebase
- 📱 Responsive design (mobile & desktop)
- ⚡ Fast performance with Vite
- 🔒 Environment variable configuration
- 📊 Error handling and loading states
- 🚀 Ready for deployment

## Tech Stack

- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: FastAPI, Python
- **Database**: Firebase Firestore
- **AI**: Hugging Face Inference API
- **Deployment**: Vercel (frontend), Render/Railway/Fly.io (backend)

## Project Structure

```
chatbot_project/
├── backend/
│   ├── app.py                          # FastAPI main application
│   ├── requirements.txt                # Python dependencies
│   ├── .env.example                    # Example environment variables
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py                 # Configuration management
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py                  # Pydantic models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── chat.py                     # Chat endpoints
│   └── services/
│       ├── __init__.py
│       ├── huggingface_service.py      # Hugging Face integration
│       └── firebase_service.py         # Firebase integration
├── frontend/
│   ├── src/
│   │   ├── main.jsx                    # React entry point
│   │   ├── App.jsx                     # Main App component
│   │   ├── index.css                   # Global styles
│   │   ├── components/
│   │   │   ├── Message.jsx             # Single message component
│   │   │   ├── MessageList.jsx         # Messages container
│   │   │   └── MessageInput.jsx        # Input form component
│   │   └── services/
│   │       └── chatService.js          # API communication
│   ├── index.html                      # HTML template
│   ├── package.json                    # npm dependencies
│   ├── vite.config.js                  # Vite configuration
│   ├── tailwind.config.js              # Tailwind configuration
│   ├── postcss.config.js               # PostCSS configuration
│   ├── .env                            # Local environment variables
│   ├── .env.example                    # Example environment variables
│   └── .gitignore                      # Git ignore file
└── README.md                           # This file
```

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.8+ (for backend)
- Hugging Face API key (free from https://huggingface.co)
- Firebase project (free tier available)

## Local Development Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables file
cp .env.example .env

# Edit .env with your credentials
# Add your Hugging Face API key, Firebase credentials
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Environment is already configured in .env for local development
```

### 3. Running Locally

**Terminal 1 - Backend:**
```bash
cd backend

# Activate virtual environment (Windows)
venv\Scripts\activate

# Run the FastAPI server
python app.py

# Server runs at http://localhost:8000
# API docs available at http://localhost:8000/docs
```

**Terminal 2 - Frontend:**
```bash
cd frontend

# Start development server
npm run dev

# Open http://localhost:5173 in your browser
```

## Environment Variables

### Backend (.env)

```env
# Hugging Face API Configuration
HUGGINGFACE_API_KEY=your_api_key_here
HUGGINGFACE_MODEL=meta-llama/Llama-2-7b-chat-hf

# Firebase Configuration
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY_ID=your_key_id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=xxxxx@appspot.gserviceaccount.com
FIREBASE_CLIENT_ID=your_client_id

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# CORS
FRONTEND_URL=http://localhost:5173
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000
```

## Getting API Keys & Credentials

### Hugging Face API Key

1. Visit https://huggingface.co/join
2. Create an account
3. Go to Settings → Access Tokens
4. Create a new token with "read" permission
5. Copy the token and add to backend `.env`

### Firebase Setup

1. Go to https://console.firebase.google.com
2. Create a new project
3. Enable Firestore Database (Start in test mode)
4. Go to Project Settings → Service Accounts
5. Click "Generate new private key"
6. Copy the credentials to backend `.env`:
   - `FIREBASE_PROJECT_ID`: "project_id" from JSON
   - `FIREBASE_PRIVATE_KEY_ID`: "private_key_id" from JSON
   - `FIREBASE_PRIVATE_KEY`: "private_key" from JSON (replace \n with actual newlines)
   - `FIREBASE_CLIENT_EMAIL`: "client_email" from JSON
   - `FIREBASE_CLIENT_ID`: "client_id" from JSON

7. In Firestore, create a collection named "chats"

## API Documentation

### Health Check
```http
GET /api/health
```

Response:
```json
{
  "status": "healthy",
  "services": {
    "huggingface": true,
    "firebase": true
  }
}
```

### Send Message
```http
POST /api/chat
Content-Type: application/json

{
  "message": "What is the weather today?"
}
```

Response:
```json
{
  "answer": "I don't have access to real-time weather data, but you can check weather.com or your local weather service for current conditions."
}
```

## Deployment

### Deploy Frontend to Vercel

1. Push frontend code to GitHub
2. Visit https://vercel.com
3. Click "Add New..." → "Project"
4. Select your repository
5. Configure:
   - Framework: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`
6. Add environment variable:
   - `VITE_API_URL`: Your backend API URL
7. Deploy

### Deploy Backend to Render

1. Push backend code to GitHub
2. Visit https://render.com
3. Click "New +" → "Web Service"
4. Select your repository
5. Configure:
   - Name: `chatbot-api`
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python -m uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Add environment variables from your `.env`
7. Deploy

### Deploy Backend to Railway

1. Push backend code to GitHub
2. Visit https://railway.app
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Select your repository
6. Add environment variables from your `.env`
7. Service will auto-deploy

### Deploy Backend to Fly.io

1. Install Fly CLI: https://fly.io/docs/getting-started/installing-flyctl/
2. Run: `flyctl auth login`
3. In backend directory: `flyctl launch`
4. Add environment variables to `fly.toml`
5. Deploy: `flyctl deploy`

## Build for Production

### Frontend
```bash
cd frontend
npm run build

# Output in frontend/dist/
```

### Backend
```bash
cd backend

# Create requirements.txt (already done)
# No build needed - copy files and set environment variables
```

## Testing

### Test Backend API
```bash
# Using curl
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'

# Using Python
python -c "
import requests
response = requests.post('http://localhost:8000/api/chat', 
  json={'message': 'Hello!'})
print(response.json())
"
```

### Test Frontend
- Open http://localhost:5173
- Type a message and click Send
- Message should appear in chat
- AI response should appear after a few seconds

## Production Checklist

- [ ] Set `DEBUG=False` in backend
- [ ] Use strong random secret keys if needed
- [ ] Enable HTTPS on all services
- [ ] Update `FRONTEND_URL` on backend for production
- [ ] Update `VITE_API_URL` on frontend for production
- [ ] Test all API endpoints
- [ ] Monitor error logs
- [ ] Set up database backups (Firebase automatic)
- [ ] Monitor API rate limits (Hugging Face free tier: 30k requests/month)

## Troubleshooting

### CORS Errors
- Check `FRONTEND_URL` in backend matches your frontend URL
- Ensure backend is running before frontend makes requests

### Firebase Errors
- Verify all credentials are correct
- Check "chats" collection exists in Firestore
- Ensure Firebase is in read/write mode

### Hugging Face Errors
- Verify API key is valid
- Check API rate limits haven't been exceeded
- Try a different model if current one is slow

### API Not Responding
- Check backend is running: `curl http://localhost:8000/`
- Check `/api/health` endpoint
- Look at backend logs for errors

## Performance Tips

1. Use free tier Hugging Face models for faster responses
2. Add caching for similar queries
3. Implement request debouncing on frontend
4. Monitor Firebase read/write costs
5. Use CDN for frontend assets (Vercel does this automatically)

## Security Considerations

- Never commit `.env` files to git
- Rotate API keys regularly
- Use HTTPS in production
- Implement rate limiting for production
- Add authentication if needed
- Validate all user inputs (already done with Pydantic)

## License

MIT License - Feel free to use this for personal and commercial projects

## Support & Resources

- FastAPI Docs: https://fastapi.tiangolo.com
- React Docs: https://react.dev
- Tailwind CSS: https://tailwindcss.com
- Firebase Docs: https://firebase.google.com/docs
- Hugging Face: https://huggingface.co/docs

## Next Steps & Enhancements

- Add user authentification
- Store user sessions
- Add chat history features
- Implement bot typing indicator
- Add emoji reactions
- Store user preferences
- Add multiple language support
- Upload files and images

---

Happy coding! 🚀
