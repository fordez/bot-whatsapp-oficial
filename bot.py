from fastapi import FastAPI
from src.webhook import api

bot = FastAPI()

bot.include_router(api)