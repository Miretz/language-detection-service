from langdetect import detect_langs
from langid.langid import LanguageIdentifier, model

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)


class LanguageDetection:

    @staticmethod
    def get_langdetect_result(text):
        langdetect_translations = detect_langs(text)
        langdetect_result = {}
        for lang in langdetect_translations:
            langdetect_result[lang.lang] = lang.prob
        return langdetect_result

    @staticmethod
    def get_langid_result(text):
        langid_translation = identifier.classify(text)
        langid_result = {str(langid_translation[0]): langid_translation[1]}
        return langid_result

    @staticmethod
    def detect_language(text):
        langdetect_results = LanguageDetection.get_langdetect_result(text)
        langid_results = LanguageDetection.get_langid_result(text)

        ld_id = max(langdetect_results, key=langdetect_results.get)
        lg_id = max(langid_results, key=langid_results.get)
        overall_language = ld_id if langdetect_results[ld_id] > langid_results[lg_id] else lg_id

        langs_detected = list(
            set(list(langdetect_results.keys()) + list(langid_results.keys())))

        result = {
            "text": text,
            "length": len(text),
            "langdetect": langdetect_results,
            "langid": langid_results,
            "overallLanguage": overall_language,
            "languagesDetected": langs_detected
        }

        return result
