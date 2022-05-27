from fastapi import FastAPI
from src.post.webhook import api

bot = FastAPI()

bot.include_router(api)