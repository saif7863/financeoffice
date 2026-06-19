# GAC Finance Dashboard

## Run locally in PyCharm

1. Open this folder in PyCharm
2. Open terminal inside PyCharm and run:
   pip install -r requirements.txt
3. Run the app:
   python app.py
4. Open browser and go to:
   http://localhost:5000

## Deploy on Render

1. Push this folder to a GitHub repository

2. Go to https://render.com and sign up / log in

3. Click "New" → "Web Service"

4. Connect your GitHub repo

5. Fill in these settings:
   - Name: gac-finance
   - Environment: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app

6. Click "Create Web Service"

7. Render will give you a live URL like:
   https://gac-finance.onrender.com

That's it. Share that URL with your team.

## Important note

Right now data is stored in the browser only.
Each person who opens the app starts fresh.
This is fine for testing for one week.
When you hand over to ERP team, they will add a proper database.
