from langdetect import detect

def detect_language(text: str, fallback: str = "en") -> str:
    try:
        return detect(text) if text and text.strip() else fallback
    except Exception:
        return fallback

def translate(text: str, target_lang: str) -> str:
    return text

def normalize_query_to_lang(query: str, ui_lang: str) -> str:
    q_lang = detect_language(query)
    return translate(query, ui_lang) if q_lang != ui_lang else query
