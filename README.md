# Priyadarshini Portfolio Web Application

A full portfolio website built with Python Flask, SQLite, and a responsive HTML/CSS/JavaScript frontend.


## Project Structure

- `app.py` - Flask application entry point
- `controllers/` - Flask routes and controller logic
- `models/` - Database models and helpers
- `templates/` - HTML templates for each page
- `frontend/css/` - Stylesheets
- `frontend/js/` - JavaScript for navigation and contact form
- `frontend/images/` - Profile image and static assets

## Pages

- Home
- About
- Skills
- Projects
- Certifications
- Achievements
- Contact

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - Windows: `venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Contact Form

The contact page submits data using Fetch API to `/api/contact` and stores messages in SQLite (`contacts.db`).

## Notes

- Replace `frontend/images/profile.jpg` with your real profile picture.
- The app is configured with Flask static folder support for the `frontend` folder.

## Deploy to Render

1. Push this project to GitHub.
2. In Render, create a new Web Service and connect the GitHub repository.
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Render will automatically detect the included `render.yaml` configuration.
5. After deployment, open the Render URL to view your portfolio.
