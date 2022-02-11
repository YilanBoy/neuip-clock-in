import requests

from src.config import get_config

# 取得設定檔的參數
config = get_config()

def send_message(message: str):

    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json',
    }

    requests.post(
        config['JANDI']['api_url'],
        json={'body': message},
        headers=headers
    )
