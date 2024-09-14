from fastapi import FastAPI
from config import logger, Config
from routes import main
import uvicorn


app = FastAPI(
    title="Real Time Template",
    description="Template for real time pipeline using different tools",
    version="1.0"
)

config = Config()

app.add_route(main.route)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host = config.get_api_config()["HOST"],
        port=config.get_api_config()["PORT"],
        reload=True
    )