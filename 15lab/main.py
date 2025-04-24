from fastapi import FastAPI, Query
from pydantic import BaseModel
import wikipedia

app = FastAPI()

# Схема ответа
class WikiResponse(BaseModel):
    title: str
    summary: str

# Схема запроса для POST
class WikiRequest(BaseModel):
    query: str
    lang: str = "en"

# Роут с path-параметром
@app.get("/search/{term}", response_model=WikiResponse)
def search_term(term: str):
    wikipedia.set_lang("en")
    summary = wikipedia.summary(term, sentences=2)
    return WikiResponse(title=term, summary=summary)

# Роут с query-параметром
@app.get("/search", response_model=WikiResponse)
def search_query(term: str = Query(...), lang: str = Query("en")):
    wikipedia.set_lang(lang)
    summary = wikipedia.summary(term, sentences=2)
    return WikiResponse(title=term, summary=summary)

# POST-запрос с телом
@app.post("/search", response_model=WikiResponse)
def search_post(request: WikiRequest):
    wikipedia.set_lang(request.lang)
    summary = wikipedia.summary(request.query, sentences=2)
    return WikiResponse(title=request.query, summary=summary)
