from fastapi import FastAPI
from auth.google_oauth import router as google_auth_router

app = FastAPI()

app.include_router(google_auth_router)

