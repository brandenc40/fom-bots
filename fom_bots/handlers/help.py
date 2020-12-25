from groupme_bot import Context

COMMANDS = {
    'NSFW Image': '\\nsfw',
    'COD Time': '\\codtime',
    'FIFA Time': '\\fifatime',
    'PGA Time': '\\pgatime',
    'Mention All': '\\all',
    'Horn Surprise': '\\horn',
    'Gagme': '\\jordan',
    'Waah Shayne': '\\shayne',
    'Random Bible Verse': '\\bible',
    'Urban Dictionary': '\\urban <word>',
    'GIF Search': '\\gif <word>',
    'Pornhub Search': '\\porn <word>'
}


def show_help(ctx: Context):
    out = ""
    for key, value in COMMANDS.items():
        out += "{}: {}\n".format(key, value)
    ctx.bot.post_message(out)
