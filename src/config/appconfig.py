from dotenv import load_dotenv
load_dotenv(override=True)
import os


class EnvConfig:
    def __init__(self):
        self.port = os.getenv("PORT", 8000)


env_config = EnvConfig()