# In google_oauth.py
from fastapi import Request, APIRouter
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import os
import pathlib

router = APIRouter()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

BASE_DIR = pathlib.Path(__file__).parent.parent
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "client_secret.json")

# 🔐 TEMPORARY storage for credentials
user_credentials = {}

from fastapi import Request, APIRouter
from starlette.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
import os
import pickle

router = APIRouter()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flows = {}

@router.get("/login/google")
def login_with_google(request: Request):
    flow = Flow.from_client_secrets_file(
    "client_secret.json",
    scopes=["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile", "openid"],
    redirect_uri="http://127.0.0.1:8000/auth/callback"
)

    auth_url, state = flow.authorization_url()
    flows[state] = flow
    return RedirectResponse(auth_url)

@router.get("/auth/callback")
async def auth_callback(request: Request):
    state = request.query_params["state"]
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=[
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "openid"
        ],
        redirect_uri="http://127.0.0.1:8000/auth/callback"
    )
    flow.fetch_token(authorization_response=str(request.url))

    # ✅ Save the credentials in memory
    user_credentials["token"] = flow.credentials

    return {"message": "Login successful!"}

