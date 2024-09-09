import logging
import os

from dotenv import load_dotenv

loggger = logging.getLogger(__name__)
class Config:
    """ """
    def __init__(self):
        pass

    def __getattr__(self, attr):
        variable = os.getenv(attr)
        if variable == "":
            return None
        return variable

    def load(self):
        """ """
        load_dotenv(override=True)
        return self

Config().load()
config: Config = Config()
