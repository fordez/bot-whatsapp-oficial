from fastapi import FastAPI
from src.apirest import api

bot = FastAPI()

bot.include_router(api)