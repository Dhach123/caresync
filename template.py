import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

folders = [
    "care-sync",
    "care-sync/backend",
    "care-sync/frontend"
]

files = {
    "care-sync/backend/app.py": "# Flask app entry point\n",
    "care-sync/backend/models.py": "# SQLAlchemy models go here\n",
    "care-sync/backend/ai_model.py": "# AI model prediction logic\n",
    "care-sync/backend/reminders.py": "# Email/SMS reminder logic\n",
    "care-sync/backend/calendar_api.py": "# Google Calendar sync logic\n",
    "care-sync/backend/config.py": "# Configuration settings\n",
    "care-sync/backend/requirements.txt": "flask\nflask_sqlalchemy\nflask_cors\nscikit-learn\npandas\njoblib\n",
    "care-sync/frontend/index.html": "<!DOCTYPE html>\n<html>\n<head><title>CareSync</title></head>\n<body>\n<h1>Welcome to CareSync</h1>\n</body>\n</html>\n",
    "care-sync/README.md": "# CareSync - Healthcare Appointment Optimizer\n\nFree AI-powered scheduling system using Flask + AI + Google Calendar\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    logging.info(f"Created folder: {folder}")

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)
    logging.info(f"Created file: {file_path}")

logging.info("✅ CareSync project structure created successfully!")
