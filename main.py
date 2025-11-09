import uvicorn
from .server import app
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def main():
    uvicorn.run(app, port=8000, host="0.0.0.0")


main()
