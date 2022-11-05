import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11019153"))
API_HASH = getenv("API_HASH", "71e4c97877f8452bd741d0b9f05bc810")
BOT_TOKEN = getenv("BOT_TOKEN", "5737170801:AAG4cSETRUvaO6LSC_T82AI_0WbmzjOM-YU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
OWNER_USERNAME = getenv("OWNER_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
