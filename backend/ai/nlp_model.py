import re

COMMON_CORRECTIONS = {"ucak":"uçak","otelr":"otel","cicek":"çiçek","telefonu":"telefon"}
CATEGORY_KEYWORDS = {
    "Çiçek":["çiçek","flower","bouquet","gül","rose","orchid"],
    "Otel":["otel","tatil","rezervasyon","hotel"],
    "Bilet":["bilet","uçak","uçuş","train","tren","ticket"],
    "Moda":["giyim","elbise","moda","kıyafet","ayakkabı","fashion","shoe"],
    "Yemek":["restoran","yemek","cafe","food","restaurant","deliver"],
    "Teknoloji":["telefon","laptop","kulaklık","electronics","tekno","tech"]
}

def autocorrect(text: str) -> str:
    t = text
    for wrong,right in COMMON_CORRECTIONS.items():
        t = re.sub(rf"\b{re.escape(wrong)}\b", right, t, flags=re.IGNORECASE)
    return t

def detect_category(query: str) -> str:
    q = (query or "").lower()
    for cat, words in CATEGORY_KEYWORDS.items():
        if any(w in q for w in words): return cat
    return "Genel"

def intent_pack(query: str):
    fixed = autocorrect(query or "")
    cat = detect_category(fixed)
    return {"query": fixed.strip(), "category": cat}
