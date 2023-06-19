import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29705318"))
API_HASH = getenv("API_HASH", "3e2781d669267ba9165147f70110cc4e")

BOT_TOKEN = getenv("BOT_TOKEN", "6282745391:AAEyyEJe6oQ_kEwhWfkpl7ejMfCc7YjZWu8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://choco:music@cluster0.45sanbt.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847797595"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Radha Robot [Pvt]")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6039423699").split("5776889746")))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Radhaxd/radha-music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RadhaX2Support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/RadhaXUpdate")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", "True")

STRING1 = getenv("STRING_SESSION", "BQCFdugLggzz848DBv1Y865vBplj1yHhPjBO-IDICnmtLx932qGsO5HDBYyantH2i4soneUnrEBLQVKYlAObNeLOsTwOmcrJnJpYQuxQ4tRc_u6JtxdieEUlwisj_AVtS77US-PrPMjvfWpwELxMYKcX2VFYGoTSCGgSlrOUWm-t6Pqz_JbtNaHGLIN060bERsg9HQ5HnXCXm2V4JrDcPQqE36FNTd3pzTGb6vTEJELzxbY1HV7yevIxlpc98luEpjq3OBDAdA7pAK1Fg3Cj_oyeLlrgecX0q_yPCYJh4L1JirEd_Aih57Y1hf8wvo0xsQ_zBT8wGzP65XKhT2xlikpEAAAAAWdEJFwA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/3afc2232682be723f72f3.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/3afc2232682be723f72f3.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/e9b0cdf96388dbd1293f3.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/30928368d3dc8992e7484.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/30928368d3dc8992e7484.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/92790c54da91bc6ab1b8d.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/92790c54da91bc6ab1b8d.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/e51cc586250e6a1878d9b.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/43fbd4623e5d59291ff43.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
