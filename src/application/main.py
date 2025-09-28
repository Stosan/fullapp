import os, uvicorn
from fastapi import FastAPI, status, Depends
from fastapi.security import HTTPBasic
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config.appconfig import env_config

# Get application settings from the settings module
from src.config.settings import get_settings
settings = get_settings()

description = "API for FullApp"
# Define a context manager for the application lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server up and running")
    yield
    print("server down")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=description,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    lifespan=lifespan
)

# Define allowed origins for CORS
origins = [
    "*",
]

# Instantiate basicAuth
security = HTTPBasic()

# Add middleware to allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Define a health check endpoint
@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return "pong"


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return "healthy"


if __name__ == "__main__":
    # Retrieve environment variables for host, port, and timeout
    timeout_keep_alive = int(os.getenv("TIMEOUT", 6000))

    # Run the application with the specified host, port, and timeout
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(env_config.port),
        timeout_keep_alive=timeout_keep_alive,
    )
