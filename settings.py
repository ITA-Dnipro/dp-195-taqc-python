from dotenv import load_dotenv

load_dotenv()
import os

host = os.getenv("HOST")
email = os.getenv("CUSTOMER_EMAIL")
customer_password = os.getenv("CUSTOMER_PASSWORD")
