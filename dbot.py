from imports import *
print(discord.__version__)
intents = discord.Intents().all()

"""
#DONE#Auto roles
role features
auto post yt videos
Music?
Review documentation for functions and ideas
"""#guild.members

#Documentation: https://discordpy.readthedocs.io/en/latest/

#establishes client for bot
client = commands.Bot(command_prefix = './', intents = intents)


"""
EVENTS
"""

#create first event, readies the bot for use
@client.event
async def on_ready():
    update_status.start()
    print("Bot ready to go")

#notifies console of member leaving
@client.event
async def on_member_join(member):
    guild = client.get_guild(528767443653623818)
    channel = client.get_channel(722970243252879420)
    role = guild.get_role(719421779600343110)
    await channel.send(f"Wow, {member} just joined the Pardi!")
    await member.add_roles(role)
    await channel.send(f"{member} is now a {role}")

#notifies console of member leaving
@client.event
async def on_member_remove(member):
    print(f"{member} couldn't Pardi hard enough.")

"""
AUTO ROLES
"""
# ASSIGN
@client.event
async def on_raw_reaction_add(payload):
    topics = [['Minecraft', 793106223469035550, "guessilldie", " is now a Minecrafter!"],
    ['Terraria', 793106820536467487, "terraria", " is now a 2-D Minecrafter ;)"],
    ['Halo', 793107335475232798, "mastertea", " is now able to finish the fight"],
    ['Phasmophobia', 793107580343812166, "ghosty", " is ghostbuster 2.0!"],
    ['Descenders', 793107709615538197, "borisbike", " is a 2-wheeled madlad!"],
    ['Programming', 793107751882457088, "VRPog", " is a code academy graduate maybe..."],
    ['Nerd', 793107957935505429, "amongusstonks", " is big wrinkly bren"],
    ['Youtuber', 793108477391274005, "youtube", " is gonna be famous one day :)"],
    ['Streamer', 793108522006741022, "twitch", " is a little POG Champ"]]
    message_id = payload.message_id
    channel = client.get_channel(722970243252879420)

    for topic in topics:
        if message_id == topic[1]:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
            if (payload.emoji.name == topic[2]):
                role = discord.utils.get(guild.roles, name=topic[0])
                member = guild.get_member(payload.user_id)
                await member.add_roles(role)
                member_at = '<@' + str(member.id) + '>'
                await channel.send(f"{member_at}" + topic[3])

# UNASSIGN
@client.event
async def on_raw_reaction_remove(payload):
    topics = [['Minecraft', 793106223469035550, "guessilldie", " is no longer a Minecrafter!"],
    ['Terraria', 793106820536467487, "terraria", " is no longer a 2-D Minecrafter ;)"],
    ['Halo', 793107335475232798, "mastertea", " is no longer able to finish the fight"],
    ['Phasmophobia', 793107580343812166, "ghosty", " is too afraid to ghost hunt"],
    ['Descenders', 793107709615538197, "borisbike", " crashed his bike and got injured"],
    ['Programming', 793107751882457088, "VRPog", " dropped out"],
    ['Nerd', 793107957935505429, "amongusstonks", " smooooth brain"],
    ['Youtuber', 793108477391274005, "youtube", " sadly gave up :("],
    ['Streamer', 793108522006741022, "twitch", " isn't my little POG Champ"]]
    message_id = payload.message_id
    channel = client.get_channel(722970243252879420)

    for topic in topics:
        if message_id == topic[1]:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
            if (payload.emoji.name == topic[2]):
                role = discord.utils.get(guild.roles, name=topic[0])
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)
                member_at = '<@' + str(member.id) + '>'
                await channel.send(f"{member_at}" + topic[3])

"""
COMMANDS
"""

#.ping
#replies with poing and the latency
@client.command()
async def ping(ctx):
    lag = round(client.latency * 1000)
    await ctx.send(f'pong! {lag}ms')

#.8ball / .eightball
#replies with magic 8 ball reply
@client.command(aliases=['8ball', 'eightball'])
#asterisk allows multiple arguments to go into 'question'
async def _8ball(ctx, *,question):
    responses = ['yes', 'no', 'maybe so']
    response = random.choice(responses)
    await ctx.send(f'Question: {question}\n\
    Answer: {response}')
    # ERROR CHECKING

#.clear
#clears given number of messages in used channel
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

#.kick
#kicks user
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *,reason = None):

    await member.kick(reason=reason)
    if (reason == None):
        print(f"{member.mention} was kicked for some reason...")
        await ctx.send(f"{member.mention} was kicked for some reason...")
    else:
        print(f"{member.mention} was kicked for the following reason:\n{reason}")
        await ctx.send(f"{member.mention} was kicked for the following reason:\n{reason}")
    

#.ban
#bans user
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *,reason = None):

    await member.ban(reason=reason)
    if (reason == None):
        print(f"{member.mention} was banned for some reason...")
    else:
        print(f"{member.mention} was banned for the following reason:\n{reason}")


@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    #returns tuple with name and reason for ban
    banned_users = await ctx.guild.bans()
    try:
        name, tag = member.split('#')
    except ValueError:
        await ctx.send("Please enter user's name and tag in the form of\n'user#1234'")

    for banned in banned_users:
        user = banned.user

        if ((user.name, user.discriminator) == (name, tag)):
            await ctx.guild.unban(user)
            await ctx.guild.send(f'unbanned {user.name}#{user.discriminator}')
            return

@client.command(aliases=['2077', 'whatgetsamanarrestedin2077'])
async def _2077(ctx, member):
    await ctx.send(f"{member} Getting cock")
    await ctx.send(file=discord.File('2077.gif'))

@client.command
async def addrole(ctx, member, role):
    channel = client.get_channel(722970243252879420)
    guild = discord.utils.find(lambda g : g.id == discord.guild_id, client.guilds)
    role = discord.utils.get(guild.roles, name=role)
    member = guild.get_member(discord.user_id)
    await member.add_roles(role)
    member_at = '<@' + str(member.id) + '>'
    await channel.send(f"{member_at} was granted the role, {role}")
    return

@client.command
async def removerole(ctx, member, role):
    channel = client.get_channel(722970243252879420)
    guild = discord.utils.find(lambda g : g.id == discord.guild_id, client.guilds)
    role = discord.utils.get(guild.roles, name=role)
    member = guild.get_member(discord.user_id)
    await member.remove_roles(role)
    member_at = '<@' + str(member.id) + '>'
    await channel.send(f"{member_at} lost the role, {role}")
    return
    
"""
TASKS
"""

statuses = cycle(["Vibing in Development", "Dev Vibe 2: Electric Boogalo"])
@tasks.loop(seconds = 30)
async def update_status():
    await client.change_presence(activity = discord.Game(next(statuses)))


"""
ERROR CHECKING
"""

@client.event
async def on_command_error(ctx, error):
    print(error)
    
    # MissingRequiredArgument
    if isinstance(error, MissingRequiredArgument) and "required argument that is missing." in str(error):
        await ctx.send("Hey dilweed you're missing an argument")
        return

    # MissingPermissions
    if isinstance(error, MissingPermissions) and " permission(s) to run this command." in str(error):
        await ctx.send("You don't have permission to use that command. Maybe don't suck?")
        return

    # CommandNotFound
    if isinstance(error, CommandNotFound) and " is not found" in str(error):
        await ctx.send("You typed a command that doesn't exist, which makes sense because you can't even READ")
        return

    # MemberNotFound
    if isinstance(error, MemberNotFound):
        await ctx.send("That person doesn't even exist bro wtf")
        return
    

#run bot from token, DO NOT SHARE TOKEN
client.run(token)