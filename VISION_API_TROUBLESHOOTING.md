# Google Vision API - Troubleshooting & Configuration

## ✅ Current Status
Your Google Vision API **IS CONFIGURED AND WORKING** ✓

```
✅ credentials.json: PRESENT
✅ Project ID: scanner-484616
✅ Service Account: face-scanner@scanner-484616.iam.gserviceaccount.com
✅ Vision client: INITIALIZED
```

## 🔍 If You See "Google Vision API is not configured"

This error occurs when:
1. `credentials.json` is missing
2. `credentials.json` has invalid JSON
3. Service account permissions are insufficient
4. Environment variables are not set

### Quick Fix

**Run the configuration checker:**
```bash
python check_vision_api.py
```

This will show you exactly what's configured and what's missing.

## 🛠️ Common Issues & Solutions

### Issue 1: "Google Vision API is not configured" Error

**Cause**: `_get_vision_client()` returns `None`

**Solution**:
```bash
# 1. Verify credentials file exists
ls -la credentials.json

# 2. Verify it's valid JSON
python -m json.tool credentials.json

# 3. Test the connection
python check_vision_api.py

# 4. Check app can load it
python -c "from app import _get_vision_client; print(_get_vision_client())"
```

### Issue 2: "File not found" Error

**Cause**: `credentials.json` deleted or renamed

**Solution**:
1. Get a new credentials file from Google Cloud Console
2. Place it in the project root: `/workspaces/apiscan/credentials.json`
3. Ensure filename is exactly `credentials.json` (case-sensitive)

### Issue 3: Face Detection Not Working

**Cause**: API call failed

**Debugging Steps**:
```bash
# 1. Check API is enabled in Google Cloud
# Visit: https://console.cloud.google.com/apis/api/vision.googleapis.com

# 2. Check service account permissions
# Need: Viewer role or Vision API User role

# 3. Check quota and usage
# Visit: https://console.cloud.google.com/apis/api/vision.googleapis.com/quotas

# 4. Check request format
python -c "
from google.cloud import vision
from PIL import Image

client = _get_vision_client()
# Test with a simple image
"
```

### Issue 4: "Permission Denied" Error

**Cause**: Service account lacks necessary permissions

**Solution**:
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Go to IAM & Admin → IAM
3. Find your service account
4. Click Edit
5. Add these roles:
   - `Viewer` (minimal)
   - `Cloud Vision API User` (recommended)
6. Save

### Issue 5: Files Disappearing After Deploy

**Cause**: Render uses ephemeral storage (free tier)

**Solution**:
1. Upload credentials via Render **Files** section (recommended)
2. OR use environment variables with base64 encoding
3. OR upgrade to Render Disk (paid)

See `RENDER_DEPLOYMENT.md` for Render-specific setup.

## 🚀 Deployment Configuration

### For Render

**Option 1: Using Files Section (Recommended)**
1. In Render dashboard → Your Service
2. Scroll to **Files** section
3. Add file with path: `credentials.json`
4. Paste your JSON credentials content

**Option 2: Using Environment Variable**
```bash
# Encode credentials
cat credentials.json | base64

# Add to Render env vars
GOOGLE_CREDENTIALS_B64=<paste-base64-string>

# Update app.py to decode (see GOOGLE_VISION_SETUP.md)
```

### For Local Development

**Option 1: File in Project**
```bash
# Place credentials.json in project root
cp ~/Downloads/credentials.json .
```

**Option 2: Environment Variable**
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

**Option 3: In .env file**
```
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

## 📊 Verify Configuration

### Test Script Output
```bash
$ python check_vision_api.py

🔍 Checking Google Vision API Configuration...

✅ credentials.json found
  ✅ type: OK
  ✅ project_id: OK
  ✅ private_key: OK
  ✅ client_email: OK

📊 Service Account Details:
  Project ID: scanner-484616
  Email: face-scanner@scanner-484616.iam.gserviceaccount.com

🧪 Testing Google Vision API import...
✅ google-cloud-vision library imported successfully
✅ Vision API client created successfully

==================================================
✅ Google Vision API is properly configured!
==================================================
```

### Manual Test
```bash
python -c "
from google.cloud import vision
from app import _get_vision_client

client = _get_vision_client()
if client:
    print('✅ Vision API client created successfully')
    print(f'Project: scanner-484616')
else:
    print('❌ Failed to create Vision API client')
"
```

## 🔐 Security Notes

⚠️ **IMPORTANT**:
- ✅ `credentials.json` is in `.gitignore` (NOT tracked by git)
- ✅ NEVER commit credentials to GitHub
- ✅ Store credentials securely in production (Render Files or env vars)
- ✅ Rotate credentials periodically
- ✅ Check Google Cloud IAM audit logs for usage

## 📋 Checklist

Before considering setup complete:

- [ ] Run `python check_vision_api.py` and see ✅
- [ ] Test uploading a photo in the app
- [ ] Test face detection works
- [ ] Test selfie matching works
- [ ] For Render: Upload credentials via Files section
- [ ] For Render: Set all environment variables

## 🆘 Still Having Issues?

1. **Check the logs**:
   ```bash
   tail -f /tmp/app.log
   ```

2. **Run configuration checker**:
   ```bash
   python check_vision_api.py
   ```

3. **Review these files**:
   - `GOOGLE_VISION_SETUP.md` - Setup guide
   - `RENDER_DEPLOYMENT.md` - Render-specific setup
   - `README.md` - General documentation

4. **Check Google Cloud Console**:
   - Verify Vision API is enabled
   - Check service account permissions
   - Review quotas and usage

5. **Common fixes**:
   - Restart the app: `python app.py`
   - Reload environment: `source .env`
   - Re-download credentials from Google Cloud

---

**Configuration Status**: ✅ ACTIVE
**Last Checked**: January 19, 2026
