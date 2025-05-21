import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "22216834"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "c50044544e93eb670fbe5ad8d952fe7f")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7081893529").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
