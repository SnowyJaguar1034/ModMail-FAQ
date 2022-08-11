from logging import Filter


class CustomFilter(Filter):

    COLOR = {
        "DEBUG": "BLUE",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "ORANGE",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True
