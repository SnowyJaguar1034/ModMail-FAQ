
import logging
import logging.config

import msgspec

### Iniial Setup ###

logger: logging.Logger = logging.getLogger(__name__)

SUPPORT_RESPONSE_MAPPING: list[dict] = None

"""
RESPONSE_MAPPING: list[dict[str, int]] = [ {
        "trigger message id": 00000000,
        "channel id": 00000000,
        "author id": 00000000,
        "answering message": 00000000,
    }
]
"""

RESPONSE_MAPPING: list[dict[str, int]] = [ { } ]
    
### Read the YAML file ###
with open("src/support_responses_mapping.yml", "rb") as f:
    SUPPORT_RESPONSE_MAPPING = msgspec.yaml.decode(f.read())

with open("src/output.txt", "w") as f:
    f.write(str(SUPPORT_RESPONSE_MAPPING))

### Update the dictionary ###
responses_len = len(SUPPORT_RESPONSE_MAPPING)



### Main Function ###
if __name__ == "__main__":
    print(SUPPORT_RESPONSE_MAPPING)