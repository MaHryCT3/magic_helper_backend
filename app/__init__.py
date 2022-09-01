import os

if os.getenv("POSTGRES_PASSWORD") is None:
    from dotenv import load_dotenv

    load_dotenv(".env.dev")


from app.main import *
