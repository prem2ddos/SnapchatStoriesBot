import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "25109257"))
    API_HASH = os.environ.get("API_HASH", "ca6e12ee79189ad6a5d01e6f3a2f9b31")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7800823134:AAEyNMRxufF-cEhamAD2jBo3mt7jfp8TTRo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "snakesnapbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 7820924114))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
