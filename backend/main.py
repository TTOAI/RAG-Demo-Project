from fastapi import FastAPI
from app.routers import ingest

app = FastAPI()

app.include_router(ingest.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
