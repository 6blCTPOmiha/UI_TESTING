import os


class Config:
    SHORT_TIMEOUT = 5
    TIMEOUT = 15
    LONG_TIMEOUT = 60
    BROWSER = os.getenv("BROWSER", "chrome")
    REMOTE = os.getenv("REMOTE", "false").lower() == "true"
    GRID_URL = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")
