import os
from pathlib import Path

QR_DIRECTORY = Path("qr_codes")
SERVER_BASE_URL = "http://localhost:8000"
SERVER_DOWNLOAD_FOLDER = "qr_codes"
FILL_COLOR = "black"
BACK_COLOR = "white"
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "secret")
