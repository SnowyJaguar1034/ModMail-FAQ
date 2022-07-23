import json
from logging import getLogger
from re import L

from topics import (
    data,  # aspects, data, how_to_commands, homepage, premium, trouleshooting
)

log = getLogger(__name__)

log.critical("Loading mappings...")
# log.warning(f"Homepage data: {data['homepage']}")
# log.warning(f"Homepage data: {data['homepage'].options}")
# log.warning(f"Links data: {data['links']}")
# for key in data.keys():
#     if key == "homepage":
#         continue
#     if key == "links":
#         continue
#     log.warning(f"{key}: {data[key].options}")

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in data["homepage"].options:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
for key in data.keys():
    if key == "homepage":
        continue
    if key == "links":
        continue
    if key == "rules":
        continue
    # log.warning(f"{key}: {data[key].options}")
    # write the above log msg contnet to the suboption_mapping dictionary
    for suboption in data[key].options:
        suboption_mapping[suboption.id] = data[key].options
    # suboption_mapping[data[key].options] = data[key].options
    log.warning(f" suboption_mapping: {suboption_mapping}")
    # for suboption in data[key].options:
    # log.warning(f"{suboption.id}: {suboption.label}")
    # suboption_mapping[int(suboption.id)] = suboption
    # suboption_mapping[int(key["id"])] = key["label"]
# suboptions = [trouleshooting, premium, how_to_commands, aspects]
# for suboption in suboptions:
#     for article in suboption.options:
#         if article.id not in suboption_mapping.keys():
#             suboption_mapping[int(article.id)] = suboption

# combined_mapping = {**mainoptions_mapping, **suboption_mapping}
# log.critical(f"combined_mapping: {combined_mapping}")

# homepage_mapping = {}
# # make a dict of all entrys of data["homepage"]
# for entry in data["homepage"].options:
#     homepage_mapping[entry.id] = entry["label"]

# links_mapping = {}
# for topic in data["links"]:
#     links_mapping[topic.label] = topic["url"]

# sub_mapping = {}
# for key, value in data.items():
#     if key == "homepage":
#         continue
#     if key == "links":
#         continue
#     for topic in value:
#         sub_mapping[topic["id"]] = topic["label"]

# log.critical(f"homepage_mapping: {homepage_mapping}")
# log.critical(f"links_mapping: {links_mapping}")
# log.critical(f"sub_mapping: {sub_mapping}")
