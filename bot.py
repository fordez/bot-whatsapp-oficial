from fastapi import FastAPI
from post.webhook import api

bot = FastAPI()

bot.include_router(api)