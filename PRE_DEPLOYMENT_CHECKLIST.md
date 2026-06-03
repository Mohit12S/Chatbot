# Pre-Deployment Checklist

Use this checklist to verify everything is configured and working before deploying to production.

## ✅ Prerequisites

- [ ] Node.js 18+ installed (`node --version`)
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Git installed and configured (`git --version`)
- [ ] GitHub account (for version control)
- [ ] Hugging Face account (for API key)
- [ ] Google account (for Firebase)

## ✅ Environment Variables

### Backend (.env file)

- [ ] `HUGGINGFACE_API_KEY` - Valid HF API token
- [ ] `HUGGINGFACE_MODEL` - Valid model name
- [ ] `FIREBASE_PROJECT_ID` - Your Firebase project ID
- [ ] `FIREBASE_PRIVATE_KEY_ID` - From service account JSON
- [ ] `FIREBASE_PRIVATE_KEY` - From service account JSON (with proper newlines)
- [ ] `FIREBASE_CLIENT_EMAIL` - From service account JSON
- [ ] `FIREBASE_CLIENT_ID` - From service account JSON
- [ ] `API_HOST` - Set to 0.0.0.0
- [ ] `API_PORT` - Set to 8000
- [ ] `DEBUG` - Set to True (development) or False (production)
- [ ] `FRONTEND_URL` - Correct frontend URL for CORS

### Frontend (.env file)

- [ ] `VITE_API_URL` - Correct backend URL (http://localhost:8000 for dev)

## ✅ Backend Setup

- [ ] Virtual environment created (`venv/`)
- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Backend starts without errors (`python app.py`)
- [ ] API docs accessible (`http://localhost:8000/docs`)
- [ ] Health check returns success (`curl http://localhost:8000/api/health`)

### Backend Testing

- [ ] Send test message to `/api/chat`:
  ```bash
  curl -X POST http://localhost:8000/api/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello!"}'
  ```
- [ ] Response contains valid answer
- [ ] No errors in backend logs
- [ ] Message appears in Firebase Firestore

## ✅ Frontend Setup

- [ ] All npm dependencies installed (`npm install`)
- [ ] Development server starts (`npm run dev`)
- [ ] Frontend accessible at http://localhost:5173
- [ ] All React components render without errors
- [ ] No console errors in browser DevTools

### Frontend Testing

- [ ] Type message "Hello"
- [ ] Click Send button
- [ ] Loading indicator appears
- [ ] User message appears on right (blue)
- [ ] AI response appears on left (gray)
- [ ] No network errors in DevTools
- [ ] Responsive on mobile (DevTools mobile view)

## ✅ Firebase Setup

- [ ] Firebase project created at console.firebase.google.com
- [ ] Firestore database created
- [ ] "chats" collection exists
- [ ] Service account credentials downloaded
- [ ] Private key file saved securely
- [ ] All credentials entered in backend .env
- [ ] Firebase connection test passes (no errors on backend start)

### Firebase Testing

- [ ] Send message from chatbot
- [ ] Check Firestore console
- [ ] New document appears in "chats" collection
- [ ] Document has: question, answer, timestamp fields

## ✅ Integration Testing

- [ ] Both backend and frontend running
- [ ] Frontend connects to backend without CORS errors
- [ ] Full message flow works:
  1. User types message
  2. Frontend sends to backend
  3. Backend calls Hugging Face
  4. Backend saves to Firebase
  5. Frontend displays response
- [ ] Multiple messages work without issues
- [ ] Error handling works (test with invalid API key)

## ✅ Code Quality

- [ ] No console.errors in browser
- [ ] No Python exceptions in backend logs
- [ ] All .env files added to .gitignore
- [ ] No API keys committed to git
- [ ] Code is readable and commented
- [ ] No unused imports or variables

## ✅ Frontend Optimization

- [ ] Production build works: `npm run build`
- [ ] Build output in `dist/` folder
- [ ] Build size is reasonable (under 500KB)
- [ ] All assets load in production build
- [ ] No errors in preview: `npm run preview`

## ✅ Backend Optimization

- [ ] `DEBUG=False` in production
- [ ] All dependencies in requirements.txt
- [ ] No hardcoded values (all in .env)
- [ ] Logging is configured
- [ ] CORS properly set for production URL

## ✅ Security Checklist

- [ ] `.env` files in .gitignore
- [ ] `.env.example` has no real keys
- [ ] No API keys in committed code
- [ ] HTTPS forced in production (automatic on Vercel)
- [ ] Firebase credentials secure
- [ ] Database backups configured (Firebase automatic)
- [ ] Rate limiting considered for production

## ✅ Pre-Commit

Before pushing to GitHub:

```bash
# Backend
cd backend
git status  # Verify .env is NOT listed
rm -rf __pycache__ .pytest_cache venv
git add .

# Frontend
cd frontend
git status  # Verify .env and node_modules NOT listed
git add .
```

- [ ] No .env files in commit
- [ ] No node_modules folder
- [ ] No __pycache__ folder
- [ ] Only source code committed
- [ ] Meaningful commit message

## ✅ Deployment: Vercel (Frontend)

- [ ] Code pushed to GitHub
- [ ] Vercel connected to GitHub repository
- [ ] All build settings correct:
  - Framework: Vite
  - Build: `npm run build`
  - Output: `dist`
- [ ] Environment variable set: `VITE_API_URL`
- [ ] Deployment successful
- [ ] Frontend URL accessible and working
- [ ] Console has no errors in production

## ✅ Deployment: Render (Backend)

- [ ] Code pushed to GitHub
- [ ] Render connected to GitHub repository
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `python -m uvicorn app:app --host 0.0.0.0 --port $PORT`
- [ ] All environment variables configured in Render
- [ ] Deployment successful
- [ ] API accessible: `curl https://backend-url/api/health`
- [ ] API and frontend can communicate

## ✅ Post-Deployment

- [ ] Frontend and backend deployed and live
- [ ] Update frontend `VITE_API_URL` to production backend URL
- [ ] Redeploy frontend with new URL
- [ ] Full end-to-end test on production URL:
  1. Send message
  2. Receive response
  3. Check Firebase for saved chat
- [ ] Monitor logs for errors
- [ ] Set up uptime monitoring (optional)
- [ ] Plan backup strategy

## ✅ Documentation

- [ ] README.md is complete and accurate
- [ ] QUICKSTART.md is tested and working
- [ ] All setup guides are complete
- [ ] DEPLOYMENT.md covers your deployment method
- [ ] Comments in code explain complex sections
- [ ] API documentation auto-generated `/docs`

## ✅ Future Maintenance

- [ ] Set reminder to rotate API keys quarterly
- [ ] Monitor Firebase usage and costs
- [ ] Monitor Hugging Face API usage
- [ ] Check for dependency updates monthly
- [ ] Review security regularly
- [ ] Plan scaling if traffic increases

## 🚀 Ready to Deploy?

If all checkboxes are checked:

✅ **Frontend**: Deploy to Vercel (automatic on push)
✅ **Backend**: Deploy to Render (automatic on push)
✅ **Database**: Firebase Firestore (already in cloud)
✅ **AI**: Hugging Face (API already available)

## 📋 Deployment Steps Summary

1. Push frontend to GitHub
2. Push backend to GitHub
3. Connect frontend repo to Vercel
4. Connect backend repo to Render/Railway/Fly
5. Configure environment variables on each platform
6. Deploy

Total time: 15-30 minutes for first deployment

## 🆘 Troubleshooting

If something fails:

1. **Check local setup first** - Does it work locally?
2. **Review logs** - Platform logs show actual errors
3. **Verify environment variables** - All set correctly?
4. **Test API directly** - Use curl to test endpoints
5. **Check Firebase** - Is database accessible?
6. **Review documentation** - Check specific setup guide

## 📞 Support Resources

- QUICKSTART.md - Fast overview
- README.md - Full documentation
- BACKEND_SETUP.md - Backend issues
- FRONTEND_SETUP.md - Frontend issues
- FIREBASE_SETUP.md - Database issues
- DEPLOYMENT.md - Deployment issues
- Platform docs: Vercel, Render, Railway, Fly.io

## 📅 Progress Tracking

| Date | Status | Notes |
|------|--------|-------|
| | Pre-deployment | Running locally |
| | Deployed | Frontend live |
| | Deployed | Backend live |
| | Testing | All systems working |
| | Production | Ready for users |

---

**Congratulations!** 🎉 You have completed the pre-deployment checklist.

Your chatbot application is ready for production deployment!

Good luck! 🚀
