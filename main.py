from fastapi import FastAPI
from pydantic import BaseModel
from model import screen_resume

app = FastAPI(title="Resume Screener API")

class ScreenRequest(BaseModel):
    job_description: str
    resume: str

@app.post("/screen")
def screen(request: ScreenRequest):
    return screen_resume(request.job_description, request.resume)