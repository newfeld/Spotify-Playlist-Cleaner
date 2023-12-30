import os
import base64
import json
import requests

client_id = "499628a6ed3b4b8290b8f11d2585754e"
client_secret = "7415f2a5ce844009a61ea3dc7a412aa4"

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant-type": "client-credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer" + token}

token = get_token()

print(token)