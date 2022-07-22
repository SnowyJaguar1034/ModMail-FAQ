import json
from logging import getLogger
from re import L

from topics import aspects, data, how_to_commands, initial, premium, trouleshooting

log = getLogger(__name__)

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in initial.options:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
suboptions = [trouleshooting, premium, how_to_commands, aspects]
for suboption in suboptions:
    for article in suboption.options:
        if article.id not in suboption_mapping.keys():
            suboption_mapping[int(article.id)] = suboption

combined_mapping = {**mainoptions_mapping, **suboption_mapping}
log.critical(f"combined_mapping: {combined_mapping}")

initial_mapping = {}
# make a dict of all entrys of data["initial"]
for entry in data["initial"].options:
    initial_mapping[entry.id] = entry["label"]

links_mapping = {}
for topic in data["links"]:
    links_mapping[topic.label] = topic["url"]

sub_mapping = {}
for key, value in data.items():
    if key == "initial":
        continue
    if key == "links":
        continue
    for topic in value:
        sub_mapping[topic["id"]] = topic["label"]

log.critical(f"initial_mapping: {initial_mapping}")
log.critical(f"links_mapping: {links_mapping}")
log.critical(f"sub_mapping: {sub_mapping}")
