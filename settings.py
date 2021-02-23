import logging
from pyats import log

from dotenv import load_dotenv

load_dotenv()
import os

host = os.getenv("HOST")
email = os.getenv("CUSTOMER_EMAIL")
customer_password = os.getenv("CUSTOMER_PASSWORD")
browser = os.getenv("BROWSER")
protocol = os.getenv("PROTOCOL")
log_level = os.getenv("LOG_LEVEL")

# Log settings
logger = logging.getLogger()
logger.setLevel(log_level)


def log_error_message(cls_refer, test_name, failed_message="My custom error"):
    logger.error(
        "You can find screenshot of this error here: oct/tests/screenshot/%s.png",
        cls_refer.page.get_screenshot(test_name),
    )
    cls_refer.failed(failed_message)


def log_change_file_handler(file_name):
    log.managed_handlers["tasklog"] = logging.FileHandler(
        f"oct/tests/log/{file_name}.log", mode="w", delay=True
    )
    log.managed_handlers.tasklog.setLevel(log_level)
    logger.addHandler(log.managed_handlers.tasklog)
    return log.managed_handlers.tasklog
