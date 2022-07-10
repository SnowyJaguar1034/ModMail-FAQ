from topics import aspects, how_to_commands, initial, premium, trouleshooting

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in initial.articles:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
suboptions = [trouleshooting, premium, how_to_commands, aspects]
for suboption in suboptions:
    for article in suboption.options:
        if article.id not in suboption_mapping.keys():
            suboption_mapping[int(article.id)] = suboption


# for article in trouleshooting.options:
#     if article.id not in suboption_mapping.keys():
#         suboption_mapping[int(article.id)] = trouleshooting
# for article in aspects.options:
#     if article.id not in suboption_mapping.keys():
#         suboption_mapping[int(article.id)] = aspects
# for article in how_to_commands.options:
#     if article.id not in suboption_mapping.keys():
#         suboption_mapping[int(article.id)] = how_to_commands
# for article in premium.options:
#     if article.id not in suboption_mapping.keys():
#         suboption_mapping[int(article.id)] = premium

# suboption_mapping = {
#     1.0: trouleshooting,
#     2.0: aspects,
#     3.0: premium,
#     4.0: how_to_commands,
# }
