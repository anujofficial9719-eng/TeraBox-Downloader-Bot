# ================== TELEGRAM API CONFIG ==================

# Get these from https://my.telegram.org/apps
API_ID = 32295602
API_HASH = "406a1c848574cd54189041aa7e507984"

# Bot token from @BotFather
BOT_TOKEN = "8399022576:AAFe3QcCEso6rnyboCzpvSigC0DjY4jX_Iw"


# ================== REDIS DATABASE CONFIG ==================

# Redis Host / Port / Password
HOST = "127.0.0.1"
PORT = 6379
PASSWORD = None   # Set to None if Redis has no password


# ================== BOT SETTINGS ==================

# Private storage chat where files are uploaded
# Use your private channel / chat ID (must be integer)
PRIVATE_CHAT_ID = -1003613454955


# Admin user IDs (MUST be integers)
# Add multiple IDs inside list
ADMINS = [
    8256962358,   # Example: Your Telegram ID
    # 123456789,
]


# ================== OPTIONAL FLAGS ==================

# If you still want to support single ADMIN broadcast logs etc.
# (Used in old redeem handler — safe to keep)
ADMIN_ID = 8256962358

TERABOX_API_BASE = "https://api.ntm.com/api/terabox"
TERABOX_API_TOKEN = "NTMPASS"

TERABOX_API_TEMPLATE = (
    f"{TERABOX_API_BASE}?key={TERABOX_API_TOKEN}&url={{url}}"
)
