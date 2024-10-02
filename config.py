import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29759992")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "61f150cdca64b2916fa499d107393140") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7433506212:AAF64LDufB89QFuTJ6cCapz1xY05QMMgw-c") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Era_Bot_Support') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Raiden:aloksingh@raiden.mnvywai.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Raiden") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5787502520")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001922369042')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph//file/80a97e703fc3fdbcaefc5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "7080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
