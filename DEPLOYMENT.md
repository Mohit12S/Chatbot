# Deployment Guide

Complete instructions for deploying the chatbot application to production.

## Overview

- **Frontend**: Deploy to Vercel (free, fast, auto-scales)
- **Backend**: Deploy to Render, Railway, or Fly.io
- **Database**: Firebase Firestore (auto-deployed, serverless)

Choose one option for backend deployment based on your preference.

## Pre-deployment Checklist

- [ ] Code committed to GitHub
- [ ] Backend `.env` configured with all variables
- [ ] Frontend `VITE_API_URL` set correctly
- [ ] Environment variables stored securely
- [ ] Tested locally on desktop and mobile
- [ ] Firestore "chats" collection created
- [ ] Firebase credentials secured
- [ ] API keys are fresh and valid

## Frontend Deployment: Vercel

### Step 1: Prepare GitHub Repository

```bash
# Navigate to frontend directory
cd frontend

# Create/verify .gitignore
echo "node_modules/" >> .gitignore
echo ".env" >> .gitignore
echo "dist/" >> .gitignore

# Commit files
git add .
git commit -m "Initial commit"
git push
```

### Step 2: Deploy on Vercel

1. Visit https://vercel.com
2. Click **"Sign Up"** (free account)
3. Choose **"Continue with GitHub"**
4. Authorize Vercel
5. Click **"Add New..."** → **"Project"**
6. Select your repository
7. Import settings appear:
   - **Framework**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - Root Directory: `./frontend` (if monorepo)
8. Click **"Environment Variables"**
9. Add:
   - Name: `VITE_API_URL`
   - Value: `https://your-backend-url.com` (update after deploying backend)
10. Click **Deploy**

### Step 3: Access Your Site

After deployment:
- Your site is live at: `https://your-project.vercel.app`
- Vercel assigns a domain automatically
- Updates auto-deploy when you push to GitHub

### Updating Frontend

```bash
# Make changes
git add .
git commit -m "Update message"
git push

# Vercel automatically redeploys
```

## Backend Deployment: Render (Recommended for Beginners)

### Step 1: Prepare Backend

```bash
cd backend

# Create runtime.txt for Python version
echo "python-3.11.4" > runtime.txt

# Commit
git add .
git commit -m "Prepare for Render deployment"
git push
```

### Step 2: Deploy on Render

1. Visit https://render.com
2. Click **"Sign Up"** (free account)
3. Choose **"GitHub"** or **"Google"**
4. Authorize Render
5. Click **"New +"** → **"Web Service"**
6. Select your repository
7. Configure:
   - **Name**: `chatbot-api` (or your name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python -m uvicorn app:app --host 0.0.0.0 --port $PORT`
8. Click **"Advanced"**
9. Add environment variables from your `.env`:
   - `HUGGINGFACE_API_KEY`
   - `HUGGINGFACE_MODEL`
   - `FIREBASE_PROJECT_ID`
   - `FIREBASE_PRIVATE_KEY_ID`
   - `FIREBASE_PRIVATE_KEY`
   - `FIREBASE_CLIENT_EMAIL`
   - `FIREBASE_CLIENT_ID`
   - `DEBUG=False`
   - `FRONTEND_URL=https://your-frontend.vercel.app`
10. Click **"Create Web Service"**

### Step 3: Monitor Deployment

- Deployment takes 2-5 minutes
- Check logs for errors
- Your API is live at: `https://chatbot-api.onrender.com`

### Update Backend URL

1. Go to Vercel for your frontend
2. Settings → Environment Variables
3. Update `VITE_API_URL`: `https://chatbot-api.onrender.com`
4. Redeploy frontend

## Backend Deployment: Railway

### Step 1: Deploy on Railway

1. Visit https://railway.app
2. Sign up with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Select your repository
6. Select `backend` folder if monorepo
7. Wait for auto-detection
8. Click **"Deploy"**

### Step 2: Configure Environment Variables

1. In Railway dashboard, go to your project
2. Click **"Variables"**
3. Add all variables from `.env`:
   - Copy entire `.env` content
   - Paste into Variables (Railway parses .env format)

### Step 3: Get API URL

1. In Railway, click on your service
2. Copy the **Public URL**
3. Update Vercel environment variable `VITE_API_URL`

## Backend Deployment: Fly.io

### Step 1: Install Fly CLI

**Windows:**
```bash
choco install flyctl
```

**macOS:**
```bash
brew install flyctl
```

**Linux:**
```bash
curl -L https://fly.io/install.sh | sh
```

### Step 2: Deploy

```bash
cd backend

# Login to Fly
flyctl auth login

# Launch app
flyctl launch

# Choose app name: chatbot-api
# Choose region closest to you
# Select Python
# Click "Create and Deploy"
```

### Step 3: Set Environment Variables

```bash
# Open Fly dashboard to add secrets
flyctl secrets set HUGGINGFACE_API_KEY=your_key
flyctl secrets set HUGGINGFACE_MODEL=meta-llama/Llama-2-7b-chat-hf
flyctl secrets set FIREBASE_PROJECT_ID=your_id
# ... set all other variables
```

Or use Fly Dashboard:
1. Go to https://fly.io/dashboard
2. Select your app
3. Settings → Secrets
4. Add all variables

### Step 4: Deploy

```bash
flyctl deploy
```

Your API is live at: `https://chatbot-api.fly.dev`

## Production Configuration

### Backend: app.py

Change these settings from `config/settings.py`:

```python
DEBUG = False  # Disable debug mode
```

Or set in `.env`:
```env
DEBUG=False
```

### Backend: CORS Settings

Update `FRONTEND_URL` to match production frontend:

```env
# In backend .env
FRONTEND_URL=https://your-frontend-url.vercel.app
```

### Frontend: API URL

Vercel environment variable:
```
VITE_API_URL=https://your-backend-api.com
```

## Monitoring & Maintenance

### Monitor Backend Logs

**Render:**
- Dashboard → Logs tab
- Real-time streaming logs

**Railway:**
- Dashboard → Logs
- Searchable logs with filters

**Fly:**
```bash
flyctl logs
```

### Monitor API Health

```bash
# Test API
curl https://your-backend-api.com/api/health

# Should return:
# {"status": "healthy", "services": {"huggingface": true, "firebase": true}}
```

### Monitor Frontend Performance

Vercel Analytics:
1. Vercel Dashboard → Project
2. Analytics tab
3. View Web Vitals

### Monitor Database

Firebase Console:
1. Firestore Database
2. Stats tab
3. View reads/writes/storage

### Check Error Rates

Each platform has error tracking:
- **Render/Fly**: Native error logs
- **Vercel**: Deployment logs
- **Firebase**: Firestore monitoring

## Updating Production

### Update Backend

```bash
# Make changes to backend code
cd backend
# ... code changes ...
git add .
git commit -m "Update backend"
git push

# Auto-deploy on your platform:
# - Render: Auto-deploys on push
# - Railway: Auto-deploys on push
# - Fly: Manual with `flyctl deploy`
```

### Update Frontend

```bash
# Make changes to frontend code
cd frontend
# ... code changes ...
git add .
git commit -m "Update frontend"
git push

# Vercel auto-deploys on push
```

## Cost Estimates (Free Tier)

| Service | Free Tier | Estimated Cost |
|---------|-----------|-----------------|
| Vercel | 100 GB bandwidth/month | $0 |
| Render | 750 hours/month | $0 (within limits) |
| Railway | $5 monthly credit | $0-20 |
| Fly | 3 shared-cpu-1x 256MB VMs | $0-2 |
| Firebase | 50k reads/day, 1GB storage | $0 (pay-as-you-go after) |

## Performance Optimization

### Frontend
- Vite automatically optimizes build
- Vercel CDN caches assets globally
- Gzip compression built-in

### Backend
- Use lightweight Hugging Face models for faster responses
- Add response caching if needed
- Monitor API rate limits

### Database
- Firestore indexes optimize queries
- Consider archiving old messages

## Security in Production

1. **Never commit `.env` files**
   - Add to `.gitignore`
   - Use platform's secret management

2. **Use HTTPS everywhere**
   - Vercel: Automatic
   - Render/Railway/Fly: Automatic

3. **Monitor API usage**
   - Set up billing alerts
   - Track Hugging Face API calls

4. **Firestore Security Rules**
   - Switch from test mode to production rules
   - Example rules provided in FIREBASE_SETUP.md

5. **Rate Limiting**
   - Consider adding rate limits if public
   - Protect against abuse

## Troubleshooting Deployment

### Frontend not connecting to backend
- Check `VITE_API_URL` is set correctly
- Verify backend is running: `curl backend-url/api/health`
- Check CORS on backend

### Backend failing to start
- Verify all environment variables set
- Check `requirements.txt` has all dependencies
- Review deployment logs for errors

### Firebase authentication failed
- Verify all credentials in environment variables
- Check private key has real newlines (not `\n`)
- Ensure Firestore is created

### Hugging Face timeouts
- Model might be overloaded
- Try smaller model
- Increase timeout if needed

## Next Steps

1. Deploy frontend to Vercel
2. Deploy backend to Render/Railway/Fly
3. Update environment URLs
4. Test on production URL
5. Monitor first 24 hours
6. Set up uptime monitoring
7. Plan backups if needed

## Useful Commands

```bash
# Check deployment status
vercel status          # Vercel
flyctl status          # Fly
# Railway/Render: use dashboard

# View logs
vercel logs            # Vercel
flyctl logs            # Fly

# Rollback deployment
vercel rollback        # Vercel
flyctl releases        # Fly to see history
```

## Resources

- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **Fly.io Docs**: https://fly.io/docs
- **Firebase Deployment**: https://firebase.google.com/docs/functions/manage-functions

---

Deployed? Send me feedback at your-email@example.com 🚀
