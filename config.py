import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27018175"))
API_HASH = getenv("API_HASH", "9726271ce98f126cebea0d4758edc88d")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6823089678:AAGg4ObgffxnA9ysxW2PXxVYrZRi3fiOOQo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://chomuchot:marin@akuma.6zp9apt.mongodb.net/?retryWrites=true&w=majority&appName=Akuma" )

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1001985818611))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5161733380"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/about-tosu/tosu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_tosuu")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nothing_bots_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGcQ78ApHRQydE8wCvcIEQW6EkzHZ89T39MablonNII0yXqczniWbaXslG3Zla1DOAZK9PZVg7x5HPRguHseZV5qmPJGD2edXgHrNkP8xcNyBBjvdnaDx4F3kkEZlfK7BE9tBXmHBkoP4wrYaYwfKG6qgqWD2LOzBXGh4XoJGhqvz2M3D_g5strtW2_P66v5OUCMlEqim7d-9FAtW57VKbYMmS-zTd7vqJvfJlaJ2tlJKJ4RP2yiFIYKdeaODzZekcrq97-Q9Vl_nVlfhun3Xo5nQVsyrOF8ntYMrMBpl2um8TYY4m4nkA9HyjgaV0yY7a0FDcxr-DCXzvVxKX3ke4qdQy0iAAAAAHT4YAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
STATS_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/cf9b17c2d78e1f58ff297.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
