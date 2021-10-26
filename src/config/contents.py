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

<b>Description</b>:
I <b>do not</b> have access to your messages! 
I am here to help you with multiple user mentions.

<b>Usage</b>:
Users that joined the group by <code>/join</code> command, can be mentioned after calling <code>/everyone</code> command.

<b>Commands</b>:
<pre>/join {group-name}</pre>
Joins (or creates if group did not exist before) group.

<pre>/leave {group-name}</pre>
Leaves (or deletes if no other users are left) the group

<pre>/everyone {group-name}</pre>
Mentions everyone that joined the group.

<pre>/groups</pre>
Show all created groups in this chat.

<pre>/start</pre>
Show start & help text

<b>Please note</b>
<code>{group-name}</code> is not required, <code>default</code> if not given.

If your chat does have multiple bots <b>I might not receive your command</b> according to <a href="https://core.telegram.org/bots/faq#what-messages-will-my-bot-get">policy of bots with privacy mode enabled</a> - use <code>Inline Mode</code> to avoid this.
"""
