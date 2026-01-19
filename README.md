# apiscan - Face Recognition & Photo Management

A Flask-based web application for event photo management with Google Vision API face recognition capabilities.

## Features

- 📷 Face detection and matching using Google Vision API
- 🎯 Selfie match functionality to find photos of attendees
- 📸 Event-based photo organization
- 💾 Photo selection and batch download
- 🎨 Responsive web interface
- ⚡ Quick access navigation

## Prerequisites

- Python 3.11+
- Google Cloud Project with Vision API enabled
- Service account credentials (credentials.json)

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd apiscan
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your GOOGLE_APPLICATION_CREDENTIALS path
   ```

5. **Run locally**
   ```bash
   python app.py
   ```

   Visit http://localhost:5000

## Deployment to Render

### Option 1: Manual Deployment (Recommended)

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Go to [render.com](https://render.com)**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `main` branch

3. **Configure Service**
   - **Name**: apiscan
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Choose your plan (Free tier available)

4. **Add Environment Variables**
   - Click "Environment" tab
   - Add these variables:
     - `GOOGLE_APPLICATION_CREDENTIALS`: `credentials.json`
     - `SECRET_KEY`: Generate a random string
     - `FLASK_ENV`: `production`

5. **Upload Google Credentials**
   - In Render dashboard, go to your service
   - Add `credentials.json` as a file in the Files section
   - Or add it as a secret environment variable

6. **Deploy**
   - Click "Deploy"
   - Wait for build to complete (2-5 minutes)

### Option 2: Deploy via Render Dashboard (One-Click)

1. **Prepare your repo** (already done)
2. **Visit Render Dashboard**
3. **Click "New" → "Web Service"**
4. **Select your GitHub repo**
5. **Let Render auto-detect** (render.yaml will be used)
6. **Set environment variables** as noted above
7. **Deploy**

## Environment Variables Required

```
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
SECRET_KEY=your_secret_key_here
FLASK_ENV=production
```

## File Structure

```
apiscan/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── render.yaml           # Render service definition
├── credentials.json      # Google service account (not in git)
├── .env                  # Local env vars (not in git)
├── templates/            # HTML templates
├── static/               # CSS, JavaScript
├── database/             # Face database
├── events/               # Event data
└── uploads/              # Temporary uploads
```

## Important Notes

⚠️ **Security**
- Never commit `credentials.json` to GitHub
- Use Render's Files section or secure secrets for credentials
- Keep `SECRET_KEY` private

⚠️ **Storage**
- Render free tier provides ephemeral storage
- Use Render Disk or external storage for persistent data
- Consider upgrading to paid plan for production

## Troubleshooting

**Issue: Build fails**
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Check build logs in Render dashboard

**Issue: Face detection not working**
- Verify credentials.json is properly configured
- Check Google Cloud Vision API is enabled
- Review API quotas in Google Cloud Console

**Issue: Files disappearing after deploy**
- Render free tier has ephemeral storage
- Implement persistent storage or upgrade plan

## Support

For issues or questions, check the logs:
- Render Dashboard → Your Service → Logs tab
- Review Google Cloud Console for API issues
