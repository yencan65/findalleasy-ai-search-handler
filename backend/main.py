from fastapi import FastAPI, UploadFile, File, Form, Query
from fastapi.responses import JSONResponse
from .settings import settings
from .ai.handler import preview_from_voice, preview_from_image, finalize_query
from .api.search_api import aggregate

app = FastAPI(title=settings.APP_NAME)

@app.get("/healthz")
def healthz():
    return {"ok": True, "app": settings.APP_NAME}

@app.post("/voice")
async def voice_to_preview(transcript: str = Form(...), ui_lang: str = Form("en")):
    preview = preview_from_voice(transcript, ui_lang)
    return JSONResponse(preview)

@app.post("/vision")
async def vision_to_preview(file: UploadFile = File(...), ui_lang: str = Form("en")):
    image_bytes = await file.read()
    preview = preview_from_image(image_bytes, ui_lang)
    return JSONResponse(preview)

@app.get("/search")
async def search(q: str = Query(..., min_length=1), category: str = Query("Genel"), region: str = Query("GLOBAL")):
    data = aggregate(q, category, region)
    return JSONResponse({"query": q, "category": category, "region": region, "results": data})
