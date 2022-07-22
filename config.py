## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuz7D77of0jiQPbEQzCInGHlCo9jyBzXHNbqsi6-_GS_W9N32NsNXFiu3oPZDpri9YkxXG03F1UPCpnPRuRzK30dta8VzC4VszT_KvIMcYbVT2VUauSFdMyXQiwgPIw6p97S0QJ-JQIwgJM3dC3uR6u-vAr-PStv52z80vhBnD1NbirMObu235AiqokyoyyNQaYqjhvv2M6ObLXaIEXj7Hc5RE17EuXg3z6RgpE17V-tw8VE8J_6oi-PKDuSHzP-82Q3EptIYaBMVlxqh0GL1x_7FHOF07wex83NgZ8j3JWdzEIw2EEP_0XY2bsB8RDLSg7asXc3QnNRcaeNvXsZg0aU=")
BOT_TOKEN = getenv("BOT_TOKEN", "5547452832:AAEfrr0nanUo-E8iR1q2oslF_mtjM9E1G2I")
BOT_NAME = getenv("BOT_NAME", "Music FrEeDoM")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "ხᖇ᥆ᥱძ ꪔ᥆᥉ᥴ᥆᭙")
OWNER_USERNAME = getenv("OWNER_USERNAME", "vvvvvve")
ALIVE_NAME = getenv("ALIVE_NAME", "ხᖇ᥆ᥱძ ꪔ᥆᥉ᥴ᥆᭙")
BOT_USERNAME = getenv("BOT_USERNAME", "Powssaofbot")
OWNER_ID = getenv("OWNER_ID", "2131150492")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "zzztz4")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LLLK_3")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LLLK_3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAMEl")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
