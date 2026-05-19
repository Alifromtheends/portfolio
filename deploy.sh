#!/bin/bash
set -e

echo "═══════════════════════════════════════"
echo "  FREELANCE PORTFOLIO DEPLOYMENT"
echo "═══════════════════════════════════════"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "[1/5] Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial portfolio launch"
else
    echo "[1/5] Git already initialized"
fi

# GitHub Pages deployment
echo ""
echo "[2/5] Setting up GitHub Pages deployment..."
echo ""
echo "Options:"
echo "  1) GitHub Pages (free, fast)"
echo "  2) Netlify Drop (drag & drop)"
echo "  3) Cloudflare Pages (free, fast global CDN)"
echo ""
read -p "Choose deployment method (1/2/3): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "GitHub Pages Setup:"
    echo "  1. Create a new repo on GitHub (e.g., 'portfolio')"
    echo "  2. Run these commands:"
    echo ""
    echo "     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo "     git branch -M main"
    echo "     git push -u origin main"
    echo ""
    echo "  3. Go to repo Settings > Pages"
    echo "  4. Set source to 'Deploy from branch' > 'main' > '/ (root)'"
    echo "  5. Your site will be live at: https://YOUR_USERNAME.github.io/YOUR_REPO/"
    echo ""
    echo "To use a custom domain:"
    echo "  1. Add a file named 'CNAME' with your domain (e.g., 'you.com')"
    echo "  2. In your DNS provider, add a CNAME record pointing to YOUR_USERNAME.github.io"
    echo ""
    
    read -p "Do you want me to create the CNAME file now? (y/n): " cname_choice
    if [ "$cname_choice" = "y" ]; then
        read -p "Enter your custom domain (or press Enter to skip): " domain
        if [ ! -z "$domain" ]; then
            echo "$domain" > CNAME
            echo "CNAME file created with: $domain"
        fi
    fi

elif [ "$choice" = "2" ]; then
    echo ""
    echo "Netlify Drop Setup:"
    echo "  1. Go to https://app.netlify.com/drop"
    echo "  2. Drag and drop this entire 'freelance-launch' folder"
    echo "  3. Your site is live instantly with a .netlify.app URL"
    echo "  4. Go to Site Settings > Domain to add a custom domain"
    echo ""

elif [ "$choice" = "3" ]; then
    echo ""
    echo "Cloudflare Pages Setup:"
    echo "  1. Go to https://dash.cloudflare.com > Pages"
    echo "  2. Connect your GitHub repo OR use Direct Upload"
    echo "  3. If Direct Upload: zip this folder, upload it"
    echo "  4. Your site is live with a .pages.dev URL"
    echo "  5. Add custom domain in Pages dashboard (free)"
    echo ""
fi

echo ""
echo "[3/5] Verifying index.html..."
if [ -f "index.html" ]; then
    echo "  ✓ index.html found"
else
    echo "  ✗ index.html not found! Aborting."
    exit 1
fi

echo ""
echo "[4/5] Checking for placeholder email..."
if grep -q "your-email@example.com" index.html; then
    echo "  ⚠ WARNING: You still have 'your-email@example.com' in index.html"
    echo "  Open index.html and replace it with your real email before deploying."
else
    echo "  ✓ Email looks updated"
fi

echo ""
echo "[5/5] Ready to deploy!"
echo ""
echo "═══════════════════════════════════════"
echo "  NEXT STEPS"
echo "═══════════════════════════════════════"
echo ""
echo "  1. Replace your email in index.html"
echo "  2. Update social links in index.html (GitHub, Twitter, LinkedIn)"
echo "  3. Add a real photo or keep it text-only (clean either way)"
echo "  4. Deploy using the method chosen above"
echo "  5. Update service-listings.md and outreach-kit.md with your real URL"
echo "  6. Start sending cold emails and posting on Twitter/LinkedIn"
echo ""
echo "Estimated time to first client: 3-7 days with consistent outreach."
echo ""
