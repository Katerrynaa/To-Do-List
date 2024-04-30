from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass
class Config:
    DATABASE_URL: str


def read_config():
    load_dotenv()
    return Config(DATABASE_URL=os.environ.get("DATABASE_URL"))


@dataclass
class ConfigToken:
    SECRET_KEY: str 
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

def read_config_token():
    load_dotenv()
    return ConfigToken(SECRET_KEY=os.environ.get("SECRET_KEY"), ALGORITHM=os.environ.get("ALGORITHM"), 
                       ACCESS_TOKEN_EXPIRE_MINUTES=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")),
                       REFRESH_TOKEN_EXPIRE_MINUTES=int(os.environ("REFRESH_TOKEN_EXPIRE_MINUTES")))