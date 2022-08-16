from flask import Flask
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

app = Flask(__name__)

load_dotenv()

# get all variable from .env

MAIL_ID = os.getenv('MAIL_ID')
PASSWORD = os.getenv('PASSWORD')
MEET_LINK = os.getenv('MEET_LINK')
