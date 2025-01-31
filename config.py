import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24026315"))
API_HASH = os.environ.get("API_HASH", "4143de8d51d2248a4fac78055e8a2a88")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8118181574:AAEv-H-IQk0YcCkwwMzjJMjTZdXcnLdger0")
ADMIN = int(os.environ.get("ADMIN", "5432660436"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "SystemErrorBD")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002145882943"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dushkuloreta464:AHxA9BtFWQQKtN9b@cluster0.dhcje.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
