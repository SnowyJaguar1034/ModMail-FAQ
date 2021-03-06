from topics import aspects, how_to_commands, initial, premium, rules, trouleshooting

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in initial.articles:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
suboptions = [trouleshooting, premium, how_to_commands, aspects, rules]
for suboption in suboptions:
    for article in suboption.options:
        if article.id not in suboption_mapping.keys():
            suboption_mapping[int(article.id)] = suboption
