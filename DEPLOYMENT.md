# Deploying Security Header Checker to Vercel

This guide will walk you through deploying your Security Header Checker application to Vercel.

## Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Python Knowledge**: Basic understanding of Python web applications

## Step 1: Prepare Your Repository

Make sure your project structure looks like this:
```
cyber/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel configuration
├── api/
│   └── index.py       # Vercel serverless entry point
└── templates/
    └── index.html     # HTML template
```

## Step 2: Push to GitHub

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Vercel deployment"
   ```

2. **Create GitHub Repository**:
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name it (e.g., "security-header-checker")
   - Don't initialize with README (you already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

## Step 3: Deploy to Vercel

### Method 1: Using Vercel Dashboard (Recommended)

1. **Go to Vercel Dashboard**:
   - Visit [vercel.com/dashboard](https://vercel.com/dashboard)
   - Sign in with your GitHub account

2. **Import Project**:
   - Click "New Project"
   - Select "Import Git Repository"
   - Choose your GitHub repository
   - Click "Import"

3. **Configure Project**:
   - **Framework Preset**: Select "Other"
   - **Root Directory**: Leave as `./` (default)
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Deploy**:
   - Click "Deploy"
   - Wait for the build to complete (usually 2-3 minutes)

### Method 2: Using Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Link to existing project? → No
   - Project name → security-header-checker (or your preferred name)
   - Directory → ./ (current directory)

## Step 4: Verify Deployment

1. **Check Your URL**:
   - Vercel will provide you with a URL like: `https://your-project.vercel.app`
   - Your app should be accessible at this URL

2. **Test the Application**:
   - Open the URL in your browser
   - Try checking security headers for a website (e.g., `google.com`)
   - Verify that both HTTPS and security headers analysis work

## Step 5: Custom Domain (Optional)

1. **Add Custom Domain**:
   - Go to your project dashboard in Vercel
   - Click "Settings" → "Domains"
   - Add your custom domain
   - Follow DNS configuration instructions

## Troubleshooting

### Common Issues:

1. **Build Fails**:
   - Check that all dependencies are in `requirements.txt`
   - Ensure `vercel.json` is properly configured
   - Check Vercel build logs for specific errors

2. **App Not Loading**:
   - Verify the `api/index.py` file exists
   - Check that routes are properly configured in `vercel.json`
   - Ensure Flask app is properly exported

3. **Function Timeout**:
   - The `maxDuration` is set to 30 seconds in `vercel.json`
   - If requests are timing out, consider optimizing the code

### Debugging:

1. **Check Vercel Logs**:
   - Go to your project dashboard
   - Click "Functions" to see serverless function logs
   - Check "Deployments" for build logs

2. **Local Testing**:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## Environment Variables (if needed)

If you need to add environment variables:

1. Go to your Vercel project dashboard
2. Click "Settings" → "Environment Variables"
3. Add any required variables

## Performance Optimization

1. **Caching**: Consider adding caching headers for static assets
2. **CDN**: Vercel automatically provides global CDN
3. **Function Optimization**: Keep functions lightweight and fast

## Monitoring

1. **Analytics**: Vercel provides built-in analytics
2. **Logs**: Monitor function logs for errors
3. **Performance**: Track function execution times

## Cost Considerations

- **Vercel Hobby Plan**: Free tier includes:
  - 100GB bandwidth/month
  - 100GB storage
  - 100GB function execution time/month
  - Perfect for personal projects

- **Pro Plan**: $20/month for:
  - Unlimited bandwidth
  - Team collaboration
  - Advanced analytics

## Support

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Vercel Community**: [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

## Next Steps

After successful deployment:

1. **Share Your App**: Share the Vercel URL with others
2. **Monitor Usage**: Keep an eye on function calls and bandwidth
3. **Iterate**: Make improvements based on user feedback
4. **Scale**: Upgrade to Pro plan if needed

Your Security Header Checker is now live on Vercel! 🚀 