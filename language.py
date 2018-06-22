from datetime import datetime
from language_detection import detect_language
import six

from flask import ( 
    request,  
    jsonify, 
    abort
)

MAX_TEXT_LENGTH = 1000000

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def detect(input):
    
    if not input:
        abort(400, description="Missing JSON request body")
    
    text = input['text'].strip()

    if isinstance(text, six.string_types) is False:
        abort(400, description="Required text parameter is missing")
    
    if len(text) == 0:
        abort(400, description="Required text parameter is empty")
    
    if len(text) > MAX_TEXT_LENGTH:
        abort(400, description="Text property size too big")
    
    return detect_language(text)
