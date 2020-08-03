import os
from dotenv import load_dotenv
from pyzillow.pyzillow import ZillowWrapper


load_dotenv()

ZILLOW_API_KEY = os.getenv('ZILLOW_API_KEY')
