from topics import aspects, how_to_commands, initial, premium, trouleshooting

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
for article in initial.articles:
    mainoptions_mapping[article.id] = article.label

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {
    1.0: trouleshooting,
    2.0: aspects,
    3.0: premium,
    4.0: how_to_commands,
}
