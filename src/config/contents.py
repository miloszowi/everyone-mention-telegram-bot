# markdownv2 python-telegram-bot specific
joined = '{} joined group `{}`'
not_joined = '{} is already in group `{}`'
left = '{} left group `{}`'
not_left = '{} did not join group `{}` before'
mention_failed = 'There are no users to mention'
no_groups = 'There are no groups for this chat'


# html python-telegram-bot specific
start_text = """
Hello!
@everyone_mention_bot here.
I am here to help you with multiple user mentions.

Using <code>Inline Mode</code> is recommended because <a href="https://core.telegram.org/bots/faq#what-messages-will-my-bot-get">policy of bots with privacy mode enabled</a> says that command trigger is sent (without mentioning the bot) only to the last mentioned bot. So if you do have multiple bots in current chat, I might not receive your command!

Available commands:
<b>Please note</b>
<code>{group-name}</code> is not required, <code>default</code> if not given.

<b>Join</b>
Joins (or creates if group did not exist before) group.
<pre>/join {group-name}</pre>

<b>Leave</b>
Leaves (or deletes if no other users are left) the group
<pre>/leave {group-name}</pre>

<b>Everyone</b>
Mentions everyone that joined the group.
<pre>/everyone {group-name}</pre>

<b>Groups</b>
Show all created groups in this chat.
<pre>/groups</pre>

<b>Start</b>
Show start & help text
<pre>/start</pre>

Reach out to <a href="https://t.me/miloszowi">Creator</a> in case of any issues/questions regarding my usage.
"""
