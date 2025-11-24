from fastapi import FastAPI
from pydantic import BaseModel
import os
from supabase import create_client, Client

# Database connection
SUPABASE_URL = os.environ.get("SUPABASE_URL") # railway
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") # railway
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_steps(supabase, step_date, steps):
        supabase.table("step").insert({
            "stepdate": step_date,
            "steps": steps
        }).execute()

app = FastAPI()

class StepsPayload(BaseModel):
    date: str
    steps: int

@app.post("/add_steps")
def receive_steps(payload: StepsPayload):
    add_steps(supabase, payload.date, payload.steps)
    return {"status": "ok", "message": "Steps recorded"}