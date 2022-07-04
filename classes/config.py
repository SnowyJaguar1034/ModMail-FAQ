from logging import getLogger
from os import getenv

from dotenv import load_dotenv

log = getLogger(__name__)

class Config:
    def __init__(self):
        pass

    def __getattr__(self, attr):
        variable = getenv(attr)
        if variable == "":
            return None
        return variable

    def load(self):
        load_dotenv(override=True)
        return self