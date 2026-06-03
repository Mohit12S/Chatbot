# Frontend Setup Instructions

## Prerequisites

- Node.js 18+ (download from https://nodejs.org)
- npm (comes with Node.js)

## Step 1: Install Dependencies

```bash
# Navigate to frontend directory
cd frontend

# Install all npm packages
npm install
```

This installs:
- **React**: UI library
- **Vite**: Build tool
- **Tailwind CSS**: Utility-first CSS framework

## Step 2: Configure Environment

The frontend is pre-configured for local development. Check `.env`:

```bash
cat .env
```

Should contain:
```env
VITE_API_URL=http://localhost:8000
```

Change this if your backend runs on a different URL.

## Step 3: Start Development Server

```bash
npm run dev
```

Output:
```
VITE v5.0.0  ready in 234 ms

➜  Local:   http://localhost:5173/
➜  press h to show help
```

Open http://localhost:5173 in your browser.

## Step 4: Test the Application

1. **Type a message** in the input box
2. **Press Enter** or click **Send button**
3. You should see:
   - Your message appear on the right (blue)
   - A loading indicator in the send button
   - AI response appear on the left (gray)
   - Your message saved to Firebase

## File Structure

```
frontend/
├── src/
│   ├── main.jsx              # React entry point
│   ├── App.jsx               # Main component
│   ├── index.css             # Global styles
│   ├── components/
│   │   ├── Message.jsx       # Single message
│   │   ├── MessageList.jsx   # All messages
│   │   └── MessageInput.jsx  # Input form
│   └── services/
│       └── chatService.js    # API communication
├── index.html                # HTML template
├── package.json              # npm config
├── vite.config.js            # Build config
├── tailwind.config.js        # Tailwind config
├── postcss.config.js         # PostCSS config
├── .env                      # Environment variables
└── .gitignore                # Git ignore
```

## File Descriptions

### `src/main.jsx`
Entry point. Renders React app into DOM.

### `src/App.jsx`
Main application component. Manages state and message flow.

### `src/components/Message.jsx`
Single chat message component. Styles differently for user/bot/error.

### `src/components/MessageList.jsx`
Container for all messages with auto-scroll.

### `src/components/MessageInput.jsx`
Input form with Send button. Handles Enter key submission.

### `src/services/chatService.js`
API client. Sends messages to backend and handles errors.

### `index.html`
HTML template. Single entry point for React app.

## Available Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run ESLint (if configured)
npm run lint
```

## Key Features

### 1. Auto-scroll
Messages auto-scroll to latest when new message arrives.

### 2. Loading State
Send button shows loading spinner and is disabled while waiting.

### 3. Error Handling
Errors display in red message bubble with error details.

### 4. Responsive Design
Mobile and desktop friendly using Tailwind CSS.

### 5. Enter Key Support
Press Enter to send message (or Shift+Enter for multiline).

## Components Overview

### App.jsx
- Manages overall state (messages, loading, error)
- Calls ChatService to send messages
- Handles API responses
- Auto-scrolls to new messages

### MessageList.jsx
- Displays all messages
- Maps messages to Message components

### Message.jsx
- Displays single message
- Different colors for user (blue), bot (gray), error (red)
- Shows timestamp

### MessageInput.jsx
- Text input field
- Send button with loading state
- Enter key support
- Pre-send message validation

### chatService.js
- `sendMessage(text)`: Sends message to backend
- `checkHealth()`: Verifies backend is running
- Handles network errors
- Uses VITE_API_URL from environment

## Styling with Tailwind CSS

The app uses utility-first Tailwind CSS classes:

```jsx
// Example
<div className="flex items-center gap-4 p-6 bg-white rounded-lg shadow">
  <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
    Click me
  </button>
</div>
```

Tailwind configuration in `tailwind.config.js`.

## Troubleshooting

### "npm: command not found"
- Install Node.js from https://nodejs.org
- Restart terminal

### Port 5173 already in use
```bash
# Use different port
npm run dev -- --port 5174
```

### "Cannot find module" error
```bash
# Delete node_modules and reinstall
rm -r node_modules
npm install
```

### Frontend can't reach backend
- Ensure backend is running: `http://localhost:8000`
- Check `VITE_API_URL` in `.env`
- Check browser console for CORS errors
- Verify backend `FRONTEND_URL` includes your frontend URL

### Messages not appearing
- Check browser console for JavaScript errors
- Verify API response in Network tab
- Check backend logs for errors

## Building for Production

```bash
# Create optimized build
npm run build

# Output: frontend/dist/
```

Deploy `dist/` folder to:
- Vercel (easiest, auto-detects Vite)
- Netlify
- GitHub Pages
- Any static host

### Vercel Deployment

1. Push code to GitHub
2. Go to vercel.com
3. Import repository
4. Add environment variable: `VITE_API_URL=your-backend-url`
5. Deploy

## Performance Tips

1. **Code Splitting**: Vite automatically code-splits components
2. **Production Build**: Always use `npm run build` for deployment
3. **Minification**: Vite minifies CSS and JavaScript
4. **Image Optimization**: Optimize images before adding

## Development Tips

### Debug Messages
Add console.logs in App.jsx:
```jsx
console.log('Message sent:', messageText);
console.log('Response:', response);
```

### Network Inspector
1. Open DevTools (F12)
2. Go to Network tab
3. Send message
4. See API request/response

### React DevTools Browser Extension
1. Install React DevTools extension
2. Inspect component state and props
3. Track re-renders

## Environment Variables

### VITE_API_URL
Backend API endpoint. 
- Local: `http://localhost:8000`
- Production: `https://api.example.com`

Accessed in code via:
```js
import.meta.env.VITE_API_URL
```

## Security Notes

- Never expose API keys in frontend (all keys in .env are safe)
- Values prefixed with `VITE_` are bundled into app, so don't use for secrets
- Backend handles all sensitive operations (API calls, database)

## Next Steps

1. Ensure backend is running
2. Test chat functionality
3. Try different messages
4. Check Firebase console for saved data
5. Deploy when ready

## Useful Resources

- React: https://react.dev
- Vite: https://vitejs.dev
- Tailwind CSS: https://tailwindcss.com
- MDN Web Docs: https://developer.mozilla.org

---

Need help? Check the main README.md for troubleshooting.
