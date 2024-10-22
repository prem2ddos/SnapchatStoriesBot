import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "22151179"))
    API_HASH = os.environ.get("API_HASH", "d0796594c68e193879899b56220a7502")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7803927725:AAFTMz9ddegKN3UfUkNfY4UVbM5Gs6CZn2I")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SMHACKERS_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5137596693))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
