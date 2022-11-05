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
STRING_SESSION = getenv("STRING_SESSION", "BQA7lKyFqkRtqewX0_h8k2VstwXbBvf4UTruztVG0rPI83icsu2hL2E_hRsdVWP8kr1xvwZepWpNQOj2NbzCKYjb6Ndkri_7rk7DR7U5-q98bl7wlxAmwA06IHCqD1Uy9eTwaXKSC5FjLe24l4VliEFwP18Zi3uzZsJ7yUtUlgimksalGf3sY2nA8jFXXI9ayAFf84FQ7Xrjvm0JEAHvAcWcL4YSwvilcYSt2UAmtFyMer49K80T7pFS5Cg44kf8deu9b4zXUAVxlH22bKwb5cRW-68cazuHAFFHLwjdbUif-IVm0IlmJpmdzimnaW0HPuO4wuELWEFPQriobfRz6BDAAAAAAU71wR0A")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Itz_Raj01")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "MusicSupportGroupbot")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "V3N0M_0P")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5619695901").split()))
aiohttpsession = aiohttp.ClientSession()
