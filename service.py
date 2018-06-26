from language_detection import LanguageDetection
import six
import os
from tika_parser import TikaParser
from werkzeug.utils import secure_filename
import traceback

from flask import (
    request,
    jsonify,
    abort,
    current_app
)

MAX_TEXT_LENGTH = 1000000
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'xlsx', 'xls', 'doc', 'docx', 'ppt', 'pptx'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate(text):
    if isinstance(text, six.string_types) is False:
        abort(400, description="Required text is not instance of string.")

    if len(text) == 0:
        abort(400, description="Required text is empty.")

    if len(text) > MAX_TEXT_LENGTH:
        abort(400, description="Text is too long.")


def detect(input):
    """Check for bad input and detect languages"""

    if not input:
        abort(400, description="Missing JSON request body.")

    text = input['text'].strip()
    validate(text)
    return LanguageDetection.detect_language(text)


def detect_from_file(uploadedFile):
    """Extract text from document using tika and detect languages"""

    if uploadedFile and allowed_file(uploadedFile.filename):

        filename = secure_filename(uploadedFile.filename)

        absolute_path = os.path.abspath(
            os.path.join(current_app.config['UPLOAD_DIR'], filename))

        uploadedFile.save(absolute_path)

        try:
            text = TikaParser.extract_text(absolute_path)
            validate(text)
            return LanguageDetection.detect_language(text)
        except:
            traceback.print_exc()
            abort(400, description="Failed to process the file")
        finally:
            if os.path.isfile(absolute_path):
                os.remove(absolute_path)
    else:
        abort(400, description="Uploaded file is missing")
