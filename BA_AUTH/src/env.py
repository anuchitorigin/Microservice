from pydantic import BaseSettings

class Settings(BaseSettings):
  MYSQL_HOST: str
  MYSQL_PORT: str
  MYSQL_USER: str
  MYSQL_ROOT_PASSWORD: str
  MYSQL_DATABASE: str
  OAUTH2_SECRET_KEY: str
  OAUTH2_ALGORITHM: str
  # OAUTH2_ACCESS_TOKEN_EXPIRE_MINUTES: int
  class Config:
    env_file = ".env"

settings = Settings()
