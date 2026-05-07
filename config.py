import os

class Config(object):
    BOT_TOKEN = os.environ.get("8565895750:AAGn5GSgwv80MwvTamKp62-wrd6Cwhz2J2w")
    API_ID = int(os.environ.get("20831039"))
    API_HASH = os.environ.get("ea20b722f7af827db12fb85f4d55238c")
    AUTH_USER = os.environ.get('AUTH_USERS', '7597020624').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "PATEL POWER ™"#Here You Can Change with Your Name  or any custom name or title you prefer
