from imports import *
print(discord.__version__)
intents = discord.Intents().all()

"""
Auto roles
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

#AUTO ROLES
"""
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f"{member} is now a {role}")
"""

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