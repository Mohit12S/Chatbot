# Quick Start Guide

Get the chatbot running locally in 10 minutes!

## What You Need

- Node.js 18+ ([download](https://nodejs.org))
- Python 3.8+ ([download](https://www.python.org/downloads/))
- Hugging Face API key (free from [huggingface.co](https://huggingface.co))
- Firebase Project (free from [firebase.google.com](https://firebase.google.com))

## 1️⃣ Get Credentials (5 minutes)

### Hugging Face API Key
1. Go to https://huggingface.co/settings/tokens
2. Create new token with "read" access
3. Copy the token

### Firebase Credentials
1. Go to https://console.firebase.google.com
2. Create new project
3. Enable Firestore Database
4. Create "chats" collection
5. Get service account JSON:
   - Settings → Service Accounts
   - Generate new private key
   - Open JSON file and copy values

## 2️⃣ Configure Backend (3 minutes)

```bash
cd backend

# Create .env file
cp .env.example .env

# Edit .env with your credentials:
# - HUGGINGFACE_API_KEY=your_key
# - FIREBASE_* from your JSON file
```

## 3️⃣ Start Backend (2 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py

# Check: http://localhost:8000/docs
```

## 4️⃣ Start Frontend (2 minutes)

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev

# Opens: http://localhost:5173
```

## 5️⃣ Test It! (Less than 1 minute)

1. Type a message: "Hello!"
2. Click Send button
3. Wait for AI response
4. Check Firebase Console → Firestore → "chats" collection

**That's it!** 🎉

## What's Next?

- [Backend Setup](BACKEND_SETUP.md) - Detailed backend guide
- [Frontend Setup](FRONTEND_SETUP.md) - Detailed frontend guide
- [Firebase Setup](FIREBASE_SETUP.md) - Complete Firebase guide
- [Deployment](DEPLOYMENT.md) - Deploy to production
- [Main README](README.md) - Full documentation

## Troubleshooting

### "Backend not responding"
```bash
# Check if running:
curl http://localhost:8000/

# Verify environment variables in .env
```

### "Firebase error"
- Verify all credentials in backend/.env
- Check "chats" collection exists
- Check private key newlines (not escaped `\n`)

### "Frontend can't reach backend"
- Ensure backend is running
- Check frontend `.env` has `VITE_API_URL=http://localhost:8000`

### Still stuck?
1. Check full [README.md](README.md)
2. Review specific guide: [Backend](BACKEND_SETUP.md), [Frontend](FRONTEND_SETUP.md), or [Firebase](FIREBASE_SETUP.md)
3. Check logs in terminal where server is running

## Project Structure

```
chatbot_project/
├── backend/              # FastAPI Python backend
├── frontend/             # React Vite frontend
├── README.md             # Full documentation
├── BACKEND_SETUP.md      # Backend guide
├── FRONTEND_SETUP.md     # Frontend guide
├── FIREBASE_SETUP.md     # Firebase guide
├── DEPLOYMENT.md         # Deploy to production
└── QUICKSTART.md         # This file
```

## Key Files

| File | Purpose |
|------|---------|
| `backend/app.py` | Main backend server |
| `backend/requirements.txt` | Python dependencies |
| `backend/.env` | Backend configuration |
| `frontend/src/App.jsx` | Main React component |
| `frontend/src/services/chatService.js` | API communication |
| `frontend/package.json` | NPM dependencies |

## Important Notes

⚠️ **Never commit `.env` files!**
- Add to `.gitignore`
- Use `.env.example` as template

🔒 **API Keys are Secure**
- Backend handles all API calls
- Frontend never exposes keys
- Keys stay in environment variables

🚀 **Ready to Deploy?**
- See [DEPLOYMENT.md](DEPLOYMENT.md) for production setup

## Need Help?

Check the relevant guide:
- [Backend Setup Issues](BACKEND_SETUP.md#troubleshooting)
- [Frontend Setup Issues](FRONTEND_SETUP.md#troubleshooting)
- [Firebase Setup Issues](FIREBASE_SETUP.md#troubleshooting)
- [Deployment Issues](DEPLOYMENT.md#troubleshooting-deployment)

---

Happy coding! 🚀
