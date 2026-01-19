# DEPLOYMENT GUIDE - Render.com

## Quick Start (5 minutes)

### Step 1: Prepare Your Repository
✅ Already done! Your repo is ready with:
- `Procfile` - Tells Render how to run your app
- `render.yaml` - Automatic configuration
- `requirements.txt` - All dependencies including gunicorn
- `runtime.txt` - Python 3.11.7

### Step 2: Push to GitHub
```bash
git push origin main
```

### Step 3: Go to Render.com
1. Visit https://dashboard.render.com
2. Sign up or log in (free account)
3. Click **"New +"** button (top right)
4. Select **"Web Service"**

### Step 4: Connect GitHub Repository
1. Click **"Connect Repository"**
2. Select your GitHub account
3. Search for "apiscan"
4. Click **"Connect"**

### Step 5: Configure Service Settings
- **Name**: `apiscan` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt` (auto-filled)
- **Start Command**: `gunicorn app:app` (auto-filled)
- **Instance Type**: Choose plan (Free available)

### Step 6: Set Environment Variables
Before deploying, click **"Environment"** tab and add:

```
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
SECRET_KEY=(generate random string, e.g., abc123xyz789)
FLASK_ENV=production
```

**For SECRET_KEY**, generate one using Python:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 7: Add Google Credentials File
**CRITICAL**: Don't commit credentials.json to GitHub!

Option A - Using Render Files (Recommended):
1. In Render dashboard, scroll to **"Files"**
2. Click **"Add File"**
3. Path: `credentials.json`
4. Paste entire contents of your `credentials.json`
5. Save

Option B - Environment Variable:
1. If file is small, encode it in base64:
   ```bash
   cat credentials.json | base64
   ```
2. Add as env var `GOOGLE_CREDENTIALS_B64`
3. Modify app.py to decode it

### Step 8: Deploy
1. Click the blue **"Deploy"** button
2. Watch the build logs (takes 2-5 minutes)
3. Wait for "Your service is live" message

### Step 9: Access Your App
- Your URL will be: `https://apiscan-xxxxx.onrender.com`
- Visit it in your browser
- Test the functionality!

---

## Detailed Troubleshooting

### Build Fails: ModuleNotFoundError
- Check requirements.txt has all dependencies
- Verify no typos in package names
- Current dependencies:
  ```
  Flask
  Pillow
  setuptools<81
  fpdf2
  google-cloud-vision
  gunicorn
  python-dotenv
  ```

### Build Fails: credentials.json not found
- Use **Files** section in Render (Step 7, Option A)
- OR encode and use environment variable
- Don't forget to set `GOOGLE_APPLICATION_CREDENTIALS` env var

### Service Crashes After Deploy
1. Check Logs tab in Render dashboard
2. Look for Python errors
3. Common issues:
   - Missing environment variables
   - Invalid credentials.json format
   - Port not binding correctly

### Face Detection Returns Empty
- Verify credentials.json is valid (test locally first)
- Check Google Cloud Console has Vision API enabled
- Confirm service account has proper permissions
- Test with `python -c "from google.cloud import vision; print('OK')"`

### Uploaded Files Disappear
- Render free tier has ephemeral storage
- Implement database or persistent storage
- Or upgrade to Render Disk (paid)

---

## Production Checklist

Before going live:

- [ ] Test locally: `python app.py`
- [ ] Push to GitHub: `git push origin main`
- [ ] Set all environment variables in Render
- [ ] Upload credentials.json via Files
- [ ] Test face detection is working
- [ ] Check SSL certificate (automatic)
- [ ] Monitor logs for errors

---

## After Deployment

### View Logs
Dashboard → Service → Logs tab

### Restart Service
Dashboard → Service → "Restart latest deployment"

### Update Code
1. Make changes locally
2. `git push origin main`
3. Render auto-redeploys (check Settings → Auto-deploy)

### Scale Up
- Switch to paid plan for better performance
- Add more resources if needed
- Upgrade storage for persistent data

---

## Quick Render Dashboard URLs

- Dashboard: https://dashboard.render.com
- Your Service: https://dashboard.render.com/services
- Docs: https://render.com/docs

---

## Need Help?

1. Check Render Logs: Dashboard → Your Service → Logs
2. Review README.md troubleshooting section
3. Check Google Cloud Console for API issues
4. Test locally first before deploying changes

---

**You're all set! 🚀 Your app should be live in 5-10 minutes.**
