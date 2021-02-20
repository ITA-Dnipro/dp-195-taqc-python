from dotenv import load_dotenv

load_dotenv()
import os

host = os.getenv("HOST")
email = os.getenv("CUSTOMER_EMAIL")
customer_password = os.getenv("CUSTOMER_PASSWORD")
browser = os.getenv("BROWSER")
protocol = os.getenv("PROTOCOL")
log_level = os.getenv("LOG_LEVEL")
