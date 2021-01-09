from groupme_bot import Context, MentionsAttachment

from constants.gaming import FIFA_PROFILES, COD_PROFILES, PGA_PROFILES, QC_FOM
from utils.error_decorator import handle_exceptions


@handle_exceptions
def fifa_time(ctx: Context):
    text = 'Pecan Sandies.. Assemble!\n\n'
    user_ids = []
    loci = []
    for val in FIFA_PROFILES.values():
        user_ids.append(val['groupme_id'])
        loci.append([len(text), len(val['gamertag']) + 1])
        text += '@{} '.format(val['gamertag'])
    ctx.bot.post_message(text, [MentionsAttachment(loci=loci, user_ids=user_ids)])


@handle_exceptions
def cod_time(ctx: Context):
    text = 'COD TIME MOTHERFUCKERS\n\n'
    user_ids = []
    loci = []
    for val in COD_PROFILES.values():
        user_ids.append(val['groupme_id'])
        loci.append([len(text), len(val['gamertag']) + 1])
        text += '@{} '.format(val['gamertag'])
    ctx.bot.post_message(text, [MentionsAttachment(loci=loci, user_ids=user_ids)])


@handle_exceptions
def pga_time(ctx: Context):
    text = 'Let\'s hit the links boys\n\n'
    user_ids = []
    loci = []
    for val in PGA_PROFILES.values():
        user_ids.append(val['groupme_id'])
        loci.append([len(text), len(val['gamertag']) + 1])
        text += '@{} '.format(val['gamertag'])
    ctx.bot.post_message(text, [MentionsAttachment(loci=loci, user_ids=user_ids)])


@handle_exceptions
def qc_fom(ctx: Context):
    ids = []
    for val in QC_FOM.values():
        ids.append(val['groupme_id'])
    text = 'Hey QC fags...\n\n'
    user_ids = []
    loci = []
    group_info = ctx.bot.get_group(ctx.bot.group_id)
    for member in group_info['members']:
        if member['id'] in ids:
            user_ids.append(member['id'])
            loci.append([len(text), len(member['name']) + 1])
            text += '@{} '.format(member['name'])
    ctx.bot.post_message(text, [MentionsAttachment(loci=loci, user_ids=user_ids)])
