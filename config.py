from os import environ

API_ID = int(environ.get("API_ID", "21257327"))
API_HASH = environ.get("API_HASH", "1235c1fe45ebc4968d9e23bc93440549")
BOT_TOKEN = environ.get("BOT_TOKEN", "7739130686:AAEJPcR_0EgFIByce5jbcaAQzCQPpCpz0o0")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002054999365"))
ADMINS = int(environ.get("ADMINS", "5192808332"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://figega1249:owYb9NfJAuBRFFFV@cluster0.wfrsxjp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
