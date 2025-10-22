from ..settings import settings

def commission_rate(category: str, region: str = "GLOBAL") -> float:
    base = {"Moda":0.08,"Turizm":0.10,"Aksesuar":0.07,"Yemek":0.05,"Çiçek":0.08,"Otel":0.09,"Teknoloji":0.06,"Bilet":0.07}
    rate = base.get(category, settings.COMMISSION_DEFAULT)
    if region=="EU": rate -= 0.01
    if region=="ASIA": rate += 0.02
    return max(settings.COMMISSION_CAP_MIN, min(rate, settings.COMMISSION_CAP_MAX))

def apply_findalleasy_price(price: float, category: str, region: str = "GLOBAL") -> float:
    return round(price * (1 - commission_rate(category, region)), 2)

def fetch_trendyol(query: str):
    return [{"title":"Trendyol Ürün","price":399.0,"seller":"Trendyol","link":"#"}]

def fetch_ciceksepeti(query: str):
    return [{"title":"Çiçek Buket","price":129.0,"seller":"ÇiçekSepeti","link":"#"}]

def fetch_amazon(query: str):
    return [{"title":"Amazon Product","price":489.0,"seller":"Amazon","link":"#"}]

def fetch_booking(query: str):
    return [{"title":"Butik Otel","price":880.0,"seller":"Booking","link":"#"}]

PROVIDERS = {"trendyol":fetch_trendyol,"ciceksepeti":fetch_ciceksepeti,"amazon":fetch_amazon,"booking":fetch_booking}

def aggregate(query: str, category: str, region: str = "GLOBAL"):
    results = []
    for name, fn in PROVIDERS.items():
        try:
            for item in fn(query):
                item = dict(item)
                item["source"] = name
                item["findalleasy_price"] = apply_findalleasy_price(item["price"], category, region)
                results.append(item)
        except Exception:
            continue
    results.sort(key=lambda x: x.get("findalleasy_price", 1e9))
    return results
