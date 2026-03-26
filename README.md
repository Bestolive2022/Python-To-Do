# Python To-Do App

A simple To-Do list web app built with Python and Flask.

## Features

- Add tasks to your list
- Delete tasks when done
- Clean, minimal UI

## Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the app:**
   ```bash
   python todo_flask.py
   ```

3. Open your browser and go to `http://localhost:81`

## Publishing / Deploying

### Option 1: Replit

1. Go to [replit.com](https://replit.com) and create a free account.
2. Click **+ Create Repl** → choose **Import from GitHub** and paste this repo's URL.
3. Replit will detect the Flask app automatically. Click **Run**.
4. To make it public, click **Publish** in the top bar and follow the prompts.

### Option 2: Render (Free Tier)

1. Push your code to a GitHub repository.
2. Go to [render.com](https://render.com) and sign up.
3. Click **New → Web Service** and connect your GitHub repo.
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn todo_flask:app`
5. Click **Deploy**.

### Option 3: Railway

1. Push your code to a GitHub repository.
2. Go to [railway.app](https://railway.app) and sign in with GitHub.
3. Click **New Project → Deploy from GitHub repo** and select your repo.
4. Railway will auto-detect Python. Set the start command to:
   ```
   gunicorn todo_flask:app
   ```
5. Your app will be live at the generated URL.

### Option 4: PythonAnywhere (Beginner-Friendly)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com).
2. Upload your files via the **Files** tab or clone from GitHub using a Bash console.
3. Go to the **Web** tab → **Add a new web app** → choose **Flask**.
4. Set the path to `todo_flask.py` and update the WSGI config file to point to your `app` object.
5. Click **Reload** to publish.

## Notes

- The app stores tasks **in memory only** — tasks are lost when the server restarts.
- For production use, consider adding a database (e.g., SQLite) to persist tasks.
