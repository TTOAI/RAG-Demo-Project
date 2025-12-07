from fastapi import FastAPI
from app.routers import ingest, test_embed, search

app = FastAPI()

app.include_router(ingest.router)
app.include_router(test_embed.router)
app.include_router(search.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
