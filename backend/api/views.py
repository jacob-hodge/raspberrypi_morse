from flask import Blueprint, request
from flask_cors import CORS
main = Blueprint('main', __name__)
CORS(main)
@main.route('/api/run_led', methods=['POST'])
def run_led():
    from .led_helper import text_to_morse, morse_to_flashes
    message_data = request.get_json()
    message_upper = message_data.upper()
    morse_message = text_to_morse(message_upper)
    morse_to_flashes(morse_message)
    return 'DONE', 201
