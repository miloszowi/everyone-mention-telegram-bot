import re

# These are MarkdownV2 python-telegram-bot specific
opted_in = re.escape('You have opted-in for everyone-mentions.')
opted_in_failed = re.escape('You already opted-in for everyone-mentions.')
opted_off = re.escape('You have opted-off for everyone-mentions.')
opted_off_failed = re.escape('You need to opt-in first before processing this command.')
mention_failed = re.escape('There are no users to mention.')
no_groups = re.escape('There are no groups for this chat.')


start_text = re.escape("""
Hello there.
I am `@everyone_mention_bot`. 
I am here to help you with mass notifies.

Please take a look at available commands.
Parameter `<group-name>` is not required, if not given, I will assign you to `default` group.

To opt-in for everyone-mentions use:
`/in <group-name>`
for example: `/in gaming`

To opt-off for everyone mentions use:
`/out <group-name>`

To gather everyone attention use:
`/everyone <group-name>`

To see all available groups use:
`/groups`

To display all users that opted-in for everyone-mentions use:
`/silent <group-name>`

In case questions regarding my usage please reach out to @miloszowi
""")