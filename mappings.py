from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, getLogger

from discord import ActivityType

from topics import aspects, how_to_commands, initial, premium, trouleshooting

log = getLogger(__name__)

# Get the list of initial articles and map them id:label to display correct label title later
mainoptions_mapping = {}
try:
    for article in initial.options:
        mainoptions_mapping[article.id] = article.label
except Exception as e:
    log.error(f"Error mapping initial articles:\n{e.message}")

# Get the list of sub-questions to display, based on their selection
suboption_mapping = {}
suboptions = [trouleshooting, premium, how_to_commands, aspects]
try:
    for suboption in suboptions:
        for article in suboption.options:
            try:
                if article.id not in suboption_mapping.keys():
                    suboption_mapping[int(article.id)] = suboption
            except AttributeError as e:
                log.error(f"AttributeError: {article} - {e.message}")
except Exception as e:
    log.error(f"Error mapping suboptions: {e.message}")

log_levels = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARNING": WARNING,
    "ERROR": ERROR,
    "CRITICAL": CRITICAL,
}

activities = {
    "PLAYING": ActivityType.playing,
    "STREAMING": ActivityType.streaming,
    "LISTENING": ActivityType.listening,
    "WATCHING": ActivityType.watching,
    "COMPETING": ActivityType.competing,
}
