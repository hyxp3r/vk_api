import os
from dotenv import load_dotenv

load_dotenv(".env")

class Connection():

    v = "5.131"

    def __init__(self, method:str) -> None:
        self.api_key = os.environ.get("api")
        self.url = f"https://api.vk.com/method/{method}"