# app/services/login.py

import os
import requests
from fastapi import HTTPException

def get_login_token():
    login_url = os.getenv("API_URL_LOGIN")
    username = os.getenv("USER_NAME")
    password = os.getenv("USER_PASSWORD")

    if not all([login_url, username, password]):
        raise HTTPException(status_code=500, detail="🔒 Missing login environment variables")

    login_payload = {
        "username": username,
        "password": password
    }

    print("🔑 Logging in with username:", username)
    response = requests.post(login_url, json=login_payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Login failed: " + response.text)

    token = response.json().get("token")
    print("🔑 Token received:", token)
    if not token:
        raise HTTPException(status_code=500, detail="No token received")

    return token
