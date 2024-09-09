
import logging
import logging.config

import msgspec

logger = logging.getLogger(__name__)

RESPONSE_MAPPING = None

with open("src/response_mapping.yml", "rb") as f:
    RESPONSE_MAPPING = msgspec.yaml.decode(f.read())

with open ("src/output.json", "w") as f:
    f.write(f"{RESPONSE_MAPPING}")

if __name__ == "__main__":
    print(RESPONSE_MAPPING)