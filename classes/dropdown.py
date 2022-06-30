import yaml
from discord import Embed, Interaction, SelectOption
from discord.ui import Select, View

data_loaded = None
options = []
sub_options = []
chosen_sub_options = []
parents = []
child = []
grandchild = []


def shortener(text: str, length: int = 100, dots: bool = True) -> str:
    if text == None:
        return ""
    elif len(text) > length:
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

# Defines a custom Select containing colour options that the user can choose. The callback function of this class is called when the user changes their choice
class AlphaDropdown(Select):
    def __init__(self):
        for entry in data_loaded:
            parents.append(entry["label"])
            option = SelectOption(label=shortener(text=entry["label"]))
            option.value = str(entry["id"])
            if checkKey(dict=entry, key="description") == True:
                child.append(entry["description"])
                option.description = shortener(text=entry["description"])
            if checkKey(dict=entry, key="emoji") == True:
                option.emoji = entry["emoji"]
            options.append(option)
            if entry["type"] == "CATEGORY":
                for article in entry["Articles"]:
                    label = shortener(text=article["label"])
                    sub_option = SelectOption(label=label)
                    if checkKey(dict=entry, key="description") == True:
                        description = shortener(text=article["description"])
                        grandchild.append(description)
                        sub_option.description = description
                    if checkKey(dict=entry, key="emoji") == True:
                        sub_option.emoji = article["emoji"]
                    sub_options.append(sub_option)

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Select a topic...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        temp = self.values[0].split(".")
        for entry in data_loaded:
            if entry["type"] == "CATEGORY" and str(entry["id"]).split(".")[0] == str(
                self.values[0].split(".")[0]
            ):
                # print(entry.keys())
                chosen_sub_options.append(entry["Articles"])

        print(chosen_sub_options)

        await interaction.response.send_message(
            f"You have selected {self.values[0]}", view=BetaDropdownView()
        )

        # newdict = {
        #     "type": "CATEGORY",
        #     "label": "How To setup certain aspects of ModMail",
        #     "id": 2.0,
        #     "Articles": [
        #         {
        #             "type": "ARTICLE",
        #             "label": "Should I give Modmail administrator?",
        #             "id": 2.1,
        #         },
        #     ],
        # }
        # temp = newdict["Articles"]
        # print(temp)
        # for that_dict in temp:
        #     print("Hello World")
        #     if that_dict["id"] == "2.1":
        #         print(f"found it! {that_dict['label']}")


class BetaDropdown(Select):
    def __init__(self):
        for entry in chosen_sub_options[0]:
            parents.append(entry["label"])
            sub_option = SelectOption(label=shortener(text=entry["label"]))
            sub_option.value = str(entry["id"])
            if checkKey(dict=entry, key="description") == True:
                child.append(entry["description"])
                sub_option.description = shortener(text=entry["description"])
            if checkKey(dict=entry, key="emoji") == True:
                sub_option.emoji = entry["emoji"]
            sub_options.append(sub_option)

        print(sub_options)

        super().__init__(
            placeholder="Select a topic...",
            min_values=1,
            max_values=1,
            options=sub_options,
        )

    async def callback(self, interaction: Interaction):

        await interaction.response.send_message(f"You have selected {self.values[0]}")


class AlphaDropdownView(View):
    def __init__(self):
        super().__init__()
        self.add_item(AlphaDropdown())


class BetaDropdownView(View):
    def __init__(self):
        super().__init__()
        self.add_item(BetaDropdown())
