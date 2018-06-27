from tikapp import TikaApp
import os


class TikaParser:
    @staticmethod
    def extract_text(filename):
        jar_path = os.path.abspath(os.path.join("lib", "tika-app-1.18.jar"))
        tika_client = TikaApp(file_jar=jar_path)
        parsed = tika_client.extract_only_content(filename)
        return parsed
