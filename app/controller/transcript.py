from flask import Blueprint, request
from extension import app
from app.helper.selenium_helper import *

from app.services.selenium_services import capture_captions

api = Blueprint('captions_transcipt', 'captions_transcipt')


@api.route('/', methods=['GET'])
def meet_transcript():
    app.logger.info(f"selenium driver getting started.")
    return capture_captions()