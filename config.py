# ================== TELEGRAM API CONFIG ==================

# Get these from https://my.telegram.org/apps
API_ID = 34724970
API_HASH = "f240eae7c60e8e30c17203ab0e052f7e"

# Bot token from @BotFather
BOT_TOKEN = "8741784728:AAFLpwz7UZvEUumoxgO2I7ii8Lo-9ZSpa1o"


# ================== REDIS DATABASE CONFIG ==================

# Redis Host / Port / Password
HOST = "redis-11676.crce217.ap-south-1-1.ec2.cloud.redislabs.com"
PORT = 11676
PASSWORD = "yzEpbZzB41i4dPIXo4CSR9uZrbnqslIc"
USERNAME = "default"

# ================== BOT SETTINGS ==================

# Private storage chat where files are uploaded
# Use your private channel / chat ID (must be integer)
PRIVATE_CHAT_ID = -1003515041061


# Admin user IDs (MUST be integers)
# Add multiple IDs inside list
ADMINS = [
    7892805795,   # Example: Your Telegram ID
    # 123456789,
]


# ================== OPTIONAL FLAGS ==================

# If you still want to support single ADMIN broadcast logs etc.
# (Used in old redeem handler — safe to keep)
ADMIN_ID = 7892805795

TERABOX_API_BASE = "https://api.ntm.com/api/terabox"
TERABOX_API_TOKEN = "NTMPASS"

TERABOX_API_TEMPLATE = (
    f"{TERABOX_API_BASE}?key={TERABOX_API_TOKEN}&url={{url}}"
)
