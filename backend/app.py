from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from backend.store import get_targets
from backend.processor import start_processing

app = FastAPI(title="CyberRAdar")


@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.on_event("startup")
def startup():
    start_processing()

@app.get("/targets")
def targets():
    return get_targets()