# Google Vision API Setup Guide

## ⚠️ Current Issue
The app cannot find valid Google Vision API credentials, which is needed for:
- Face detection
- Selfie matching
- Photo analysis

## 🔧 Setup Steps

### Step 1: Get Google Cloud Credentials

1. **Go to** [Google Cloud Console](https://console.cloud.google.com)
2. **Create a new project** or select existing one
3. **Enable Vision API**:
   - Search for "Vision API"
   - Click "Enable"

### Step 2: Create Service Account

1. **Go to** IAM & Admin → Service Accounts
2. **Click** "Create Service Account"
3. **Fill in**:
   - Service account name: `apiscan`
   - Description: "Face detection for apiscan"
4. **Click** "Create and Continue"
5. **Grant roles**:
   - Select role: `Viewer` (minimal permissions needed)
6. **Click** "Continue" then "Done"

### Step 3: Generate JSON Key

1. **Click** the service account you just created
2. **Go to** "Keys" tab
3. **Click** "Add Key" → "Create new key"
4. **Select** "JSON"
5. **Click** "Create"
6. **A JSON file will download** - this is your `credentials.json`

### Step 4: Setup Locally

1. **Copy the downloaded JSON file**:
   ```bash
   cp ~/Downloads/credentials.json /workspaces/apiscan/
   ```

2. **OR set environment variable**:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
   ```

3. **Update `.env`**:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=credentials.json
   ```

4. **Test it**:
   ```bash
   cd /workspaces/apiscan
   python -c "from google.cloud import vision; client = vision.ImageAnnotatorClient.from_service_account_file('credentials.json'); print('✅ API configured successfully!')"
   ```

### Step 5: For Render Deployment

**Option A: Using Render Files (Recommended)**

1. Go to Render Dashboard → Your Service
2. Scroll to **"Files"** section
3. Click **"Add File"**
4. **Path**: `credentials.json`
5. **Content**: Paste entire contents of your JSON key file
6. Save

**Option B: Using Environment Variable**

1. Encode the JSON to base64:
   ```bash
   cat credentials.json | base64
   ```

2. In Render Dashboard, add environment variable:
   - **Key**: `GOOGLE_CREDENTIALS_B64`
   - **Value**: (paste the base64 string)

3. Modify `app.py` to decode it:
   ```python
   import base64
   import json
   
   creds_b64 = os.environ.get("GOOGLE_CREDENTIALS_B64")
   if creds_b64:
       creds_json = base64.b64decode(creds_b64).decode('utf-8')
       # Write to temp file and use it
   ```

## ✅ Verification

### Check if API is working:

```bash
python app.py
# Then visit http://localhost:5000
# Try uploading a photo to test face detection
```

### Check credentials file exists:

```bash
ls -la credentials.json
```

### Test Google Cloud Connection:

```bash
python -c "
from google.cloud import vision
client = vision.ImageAnnotatorClient.from_service_account_file('credentials.json')
print('✅ Vision API is configured!')
print(f'Project: {client.project_id}')
"
```

## 🆘 Troubleshooting

### Error: "Vision API is not configured"
- ✅ Check `credentials.json` exists
- ✅ Verify file has valid JSON format
- ✅ Ensure Vision API is enabled in Google Cloud
- ✅ Check service account has proper permissions

### Error: "credentials.json not found"
- ✅ Download the key file again
- ✅ Place it in `/workspaces/apiscan/credentials.json`
- ✅ Or set `GOOGLE_APPLICATION_CREDENTIALS` env var

### Error: "Permission denied"
- ✅ Service account needs "Viewer" role minimum
- ✅ Go to Google Cloud IAM and verify permissions
- ✅ May need to grant "Cloud Vision Service Agent" role

### Error: "Project quota exceeded"
- ✅ Free tier has limited requests
- ✅ Check billing in Google Cloud Console
- ✅ Enable billing or upgrade

## 💡 Notes

- ⚠️ **NEVER commit `credentials.json` to GitHub** (security risk)
- ✅ It's already in `.gitignore`
- ✅ Safe to add to Render via Files section
- ✅ Free tier allows ~1000 requests/month

## Next Steps

1. Download your `credentials.json` from Google Cloud
2. Place in project folder
3. Test locally
4. Push to GitHub (credentials.json is ignored)
5. Deploy to Render with credentials via Files section

---

**Need help?** Check the app logs for detailed error messages:
```bash
tail -f /tmp/flask.log
```
