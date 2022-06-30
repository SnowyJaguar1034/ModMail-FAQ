import json

import yaml
from discord import SelectOption

data_loaded = None
options = []
sub_options = []
parents = []
child = []
grandchild = []


def shortener(text: str, length: int = 100, dots: bool = True) -> str:
    if len(text) > length:
        if dots == True:
            output = text[: length - 3] + "..."
        else:
            output = text[:length]
    else:
        output = text
    return output


def checkKey(dict: dict, key: str) -> bool:
    return dict.get(key) != None


with open("topics.yaml", "r") as stream:
    print("Loading data...")
    data_loaded = yaml.safe_load(stream)

print(checkKey(dict=data_loaded[0], key="test"))

for entry in data_loaded:
    parents.append(entry["label"])
    label = shortener(text=entry["label"])
    option = SelectOption(label=label)
    if checkKey(dict=entry, key="description") == True:
        description = shortener(text=entry["description"])
        child.append(description)
        option.description = description
    if checkKey(dict=entry, key="emoji") == True:
        option.emoji = entry["emoji"]
    options.append(f"{option} \n")
    if entry["type"] == "CATEGORY":
        for article in entry["Articles"]:
            label = shortener(text=article["label"])
            sub_option = SelectOption(label=label)
            if (
                checkKey(dict=entry, key="description") == True
                and article["description"] is not None
            ):
                description = shortener(text=article["description"])
                grandchild.append(description)
                sub_option.description = description
            if (
                checkKey(dict=entry, key="emoji") == True
                and article["emoji"] is not None
            ):
                sub_option.emoji = article["emoji"]
            sub_options.append(sub_option)

print(f"Parents: {parents}")
print(f"Child: {child}\n")
# print(f"Grandchild: {grandchild}\n\n")
print(f"Options: {options}\n")
for option in options:
    print(f"Option: {option}\n")
print(f"Sub Options: {sub_options}\n")
for sub_option in sub_options:
    print(f"Sub Option: {sub_option}\n")

with open("output.json", "w") as file:
    print("Saving data...")
    json.dump(data_loaded, file, indent=3)

with open("output.txt", "w") as file:
    print("Saving outputs...")
    foo = ""
    for option in options:
        foo += f"Option: {option}\n"
    woo = ""
    for sub_option in sub_options:
        woo += f"Sub Option: {sub_option}\n"
    file.write(
        f"""
Parents: {parents}\n
Children: {child}\n
Grandchild: {grandchild}\n
Options: {options}\n
{foo}
Sub Options: {sub_options}\n
{woo}
    """
    )
