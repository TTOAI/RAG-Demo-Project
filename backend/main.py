from fastapi import FastAPI

app = FastAPI()

app.include_router(ingest.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
