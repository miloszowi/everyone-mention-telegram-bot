import re

# These are MarkdownV2 python-telegram-bot specific
opted_in = re.escape('You have opted-in for everyone-mentions.')
opted_in_failed = re.escape('You already opted-in for everyone-mentions.')
opted_off = re.escape('You have opted-off for everyone-mentions.')
opted_off_failed = re.escape('You need to opt-in first before processing this command.')
mention_failed = re.escape('There are no users to mention.')
no_groups = re.escape('There are no groups for this chat.')