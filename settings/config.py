from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_username: str = ""
    database_password: str = ""
    database_address: str = ""
    database_port: str = ""
    database: str = ""
    authorization_key: str = ""
    algorithm: str = ""
    access_token_time: int = 30

    class Config:
        env_file = "settings/.env"


settings = Settings()
