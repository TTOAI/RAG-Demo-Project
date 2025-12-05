from fastapi import FastAPI
from app.routers import ingest
from app.routers import test_embed

app = FastAPI()

app.include_router(ingest.router)
app.include_router(test_embed.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
