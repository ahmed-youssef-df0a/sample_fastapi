from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI : str
    SECRET_KEY : str
    ALGORITHM : str
    TOKEN_EXPIRE : int
    
    class Config:
        env_file = '.env'
 


settings = Settings()