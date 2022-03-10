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

<b>Usage</b>:
Users that joined the group by <code>/join</code> command, 
can be mentioned after typing one of those in your message: 
<code>@all</code>, <code>@channel</code>, <code>@chat</code>, <code>@everyone</code>, <code>@group</code> or <code>@here</code>.

If you did create a group named <code>gaming</code>, simply use <code>@gaming</code> to call users from that group.

You can also use <code>/everyone</code> command.

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
"""
