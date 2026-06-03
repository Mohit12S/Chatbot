# Firebase Setup Guide

Complete step-by-step guide to set up Firebase Firestore for the chatbot.

## Prerequisites

- Google account
- Access to https://console.firebase.google.com

## Step 1: Create Firebase Project

1. Visit https://console.firebase.google.com
2. Click **"Add project"** (or **"Create project"**)
3. Enter project name: `chatbot` (or your preferred name)
4. Click **Continue**
5. Disable Google Analytics (you can enable later)
6. Click **Create project**
7. Wait for project to initialize (1-2 minutes)

## Step 2: Create Firestore Database

1. In Firebase Console, click on your project
2. Left sidebar → **Firestore Database**
3. Click **"Create database"**
4. Select **Start in test mode** (for development)
   - ⚠️ **Important**: Test mode allows read/write without authentication
   - For production, switch to production mode with security rules
5. Select region closest to you (or keep default)
6. Click **"Enable"**

Wait for database to initialize (this takes a minute).

## Step 3: Create "chats" Collection

1. In Firestore, click **"Start collection"**
2. Collection ID: `chats`
3. Click **"Next"**
4. Click **"Auto ID"** to auto-generate first document
5. Add these fields:
   - Field: `question` | Type: `String` | Value: `Sample question?`
   - Field: `answer` | Type: `String` | Value: `Sample answer`
   - Field: `timestamp` | Type: `String` | Value: `2024-01-15T10:30:00`
6. Click **Save**

Now you have a "chats" collection ready!

## Step 4: Get Service Account Credentials

### Option A: Using Firebase Console (Recommended)

1. Go to **Project Settings** (gear icon, top-left)
2. Click **"Service Accounts"** tab
3. Select **Python** in language dropdown
4. Click **"Generate new private key"**
5. Save the JSON file
6. Open the JSON file and copy these values:

```json
{
  "project_id": "YOUR_PROJECT_ID",
  "private_key_id": "YOUR_PRIVATE_KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xxxxx@YOUR_PROJECT_ID.iam.gserviceaccount.com",
  "client_id": "YOUR_CLIENT_ID"
}
```

## Step 5: Configure Backend

1. In `backend/.env`, add these values:

```env
FIREBASE_PROJECT_ID=your_project_id_from_json
FIREBASE_PRIVATE_KEY_ID=your_private_key_id_from_json
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIB...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@your_project_id.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=your_client_id_from_json
```

### Important: Handling the Private Key

The private key in JSON has escape sequences (`\n`). You need actual newlines:

**Method 1: Manual replacement**
- Copy the `private_key` value
- Replace `\n` with actual newlines in .env

**Method 2: Python script**
```python
import json

with open('your-downloaded-file.json') as f:
    data = json.load(f)
    print(data['private_key'])
```

Copy the output and paste into `.env`

## Step 6: Verify Connection

### Test Backend Connection

```bash
cd backend

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run health check
python -c "
from services.firebase_service import FirebaseService
try:
    firebase = FirebaseService()
    print('✓ Firebase connected successfully!')
except Exception as e:
    print(f'✗ Error: {e}')
"
```

### Send Test Message

```bash
# Start backend
python app.py

# In another terminal, send test message:
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello world!"}'
```

Check Firebase Console → Firestore → Look for new document in "chats" collection!

## Step 7: Security Rules (Production)

For production, switch from test mode to production rules:

1. In Firestore, click **"Rules"** tab
2. Replace with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow read to everyone
    match /chats/{document=**} {
      allow read: if true;
      allow write: if false;
    }
  }
}
```

This allows everyone to read but only backend writes (via service account).

Or restrict by domain:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /chats/{document=**} {
      // Only allow requests from your backend
      allow read: if true;
      allow create: if request.auth.uid == "YOUR_SERVICE_ACCOUNT_ID";
    }
  }
}
```

## Monitoring & Usage

### View Database Statistics

1. **Firestore Console** → Database view
2. See number of documents, storage used
3. Click on "chats" to view all conversations

### Monitor Costs

1. **Firebase Console** → **Settings** → **Billing**
2. View current usage
3. Free tier includes:
   - 50,000 reads/day
   - 20,000 writes/day
   - 1 GB storage

### View Real-time Updates

1. In Firestore Console, open "chats" collection
2. Send messages from the chatbot
3. See new documents appear in real-time

## Backup & Recovery

### Backup Data

Firebase provides:
- Auto-backup to Google Cloud Storage
- Export/import via Firebase Console

To manually export:
1. **Firestore** → Click menu (**⋮**)
2. **"Export collection"**
3. Choose destination (Google Cloud Storage bucket)

### Delete Test Data

To delete all documents:
1. **Firestore** → Select all documents
2. Click **Delete**

⚠️ Be careful in production!

## Troubleshooting

### "Permission denied" Error
- Check Firestore is in **test mode**
- Verify credentials in `.env` are correct
- Check "chats" collection exists

### "Resource not found" Error
- Create "chats" collection manually
- Verify collection spelling (lowercase)

### "Authentication failed" Error
- Verify all Firebase credentials
- Download new private key from Firebase Console
- Restart backend after updating .env

### No Documents Appearing in Firestore
- Check backend logs for errors
- Verify backend health: `curl http://localhost:8000/api/health`
- Manually test save with curl (see Step 6)

### Firebase Module Not Found
```bash
# In backend directory:
pip install firebase-admin
```

## Best Practices

1. **Never commit private key to git**
   - Add `backend/.env` to `.gitignore`
   - Use `.env.example` as template

2. **Use service account for backend**
   - Backend handles Firestore writes
   - Frontend doesn't directly access database

3. **Monitor costs**
   - Use filtering to reduce reads
   - Archive old conversations
   - Set up billing alerts

4. **Security rules in production**
   - Don't use test mode in production
   - Restrict access appropriately
   - Regularly review rules

## Common Queries in Firestore

### View Recent Messages
```javascript
db.collection("chats")
  .orderBy("timestamp", "desc")
  .limit(10)
  .get()
```

### Search by Question
```javascript
db.collection("chats")
  .where("question", ">=", "search term")
  .where("question", "<", "search term" + "\uf8ff")
```

## Next Steps

1. ✅ Create Firebase project
2. ✅ Set up Firestore database
3. ✅ Create "chats" collection
4. ✅ Get service account credentials
5. ✅ Configure backend .env
6. ✅ Test connection
7. Deploy application

## Resources

- Firebase Docs: https://firebase.google.com/docs/firestore
- Firestore Python SDK: https://firebase.google.com/docs/firestore/quickstart
- Firestore Best Practices: https://firebase.google.com/docs/firestore/best-practices
- Security Rules: https://firebase.google.com/docs/firestore/security/start

---

Questions? Check Firebase Support: https://firebase.google.com/support
