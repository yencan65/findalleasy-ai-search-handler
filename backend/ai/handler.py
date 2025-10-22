from .nlp_model import intent_pack
from .vision_model import label_image
from .locale_adapter import normalize_query_to_lang

def preview_from_voice(transcript: str, ui_lang: str):
    normalized = normalize_query_to_lang(transcript, ui_lang)
    intent = intent_pack(normalized)
    return {"type":"voice","preview":intent["query"],"category":intent["category"]}

def preview_from_image(image_bytes: bytes, ui_lang: str):
    labels = label_image(image_bytes)
    q = " ".join(labels)
    normalized = normalize_query_to_lang(q, ui_lang)
    intent = intent_pack(normalized)
    return {"type":"image","labels":labels,"preview":intent["query"],"category":intent["category"]}

def finalize_query(approved_text: str, ui_lang: str):
    normalized = normalize_query_to_lang(approved_text, ui_lang)
    intent = intent_pack(normalized)
    return {"query":intent["query"],"category":intent["category"]}
