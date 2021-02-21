import os

from dotenv import load_dotenv
from pyats import log
import logging

load_dotenv()

host = os.getenv("HOST")
email = os.getenv("CUSTOMER_EMAIL")
customer_password = os.getenv("CUSTOMER_PASSWORD")
browser = os.getenv("BROWSER")
protocol = os.getenv("PROTOCOL")
log_level = os.getenv("LOG_LEVEL")

# Log settings
logger = logging.getLogger()
logger.setLevel(log_level)
handler = log.TaskLogHandler(logfile="oct/tests/log/temp.log", mode="w")
log.managed_handlers["tasklog"] = handler
log.managed_handlers.tasklog.setLevel(log_level)
logger.addHandler(handler)
log_managed = {"logger": logger, "handler": log.managed_handlers.tasklog}

