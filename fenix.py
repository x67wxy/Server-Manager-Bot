import discord
import os
import sys
import psutil
import asyncio
import random
import urllib
import json
import requests
from time import strftime
import jishaku
from discord.utils import find
from discord.ext import commands, tasks
import time
import aiohttp
from discord_buttons_plugin import *
from discord_components import *
from discord_components import DiscordComponents, Button, Select, SelectOption
from discord_components import *
from typing import Union
from discord.gateway import DiscordWebSocket
import datetime
from discord.ext.commands import Greedy
from typing import Union

start_time = datetime.datetime.utcnow()


def guildowner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 808230072536006697 or ctx.message.author.id == 808230072536006697


async def get_prefix(client, message):
    if message.author.id in []:
        return ""
    else:
        return "."


token = "MTA0Mzc1NzE5MTMyMjE1NzExOA.GGWQsx.QyB8cs2kUGn-22UPJ42GCmzwxWr1pzJMULArjM"
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.AutoShardedBot(shard_count=1,
                                 command_prefix=("."),
                                 case_insensitive=True,
                                 intents=intents,
                                 help_command=None,
                                 activity=discord.Activity(
                                     type=discord.ActivityType.listening,
                                     name=f".help"),
                                 status=discord.Status.idle)
client.owner_ids = [808230072536006697]
buttons = ButtonsClient(client)
headers = {"Authorization": f"{token}"}
ddb = DiscordComponents(client)

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client.load_extension("jishaku")


@client.event
async def on_ready():
    print(f"Sucessfully logged in {client.user}")


def restart_client():
    os.execv(sys.executable, ['python'] + sys.argv)


@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send(f"{tick} Restarting..")
    restart_client()


######## ERROR ###########


@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    await ctx.send(
        embed=discord.Embed(color=0x2f3136,
                            title="",
                            timestamp=ctx.message.created_at,
                            description=f'<:error:992024170785427537> {error}')
    )


tick = "<:success:992024105975037992>"
cross = "<:error:992024170785427537>"
warn = "<:icons_warning:974700296011907122>"
arrow = "<:arrow:992046835201999013>"
reply = "<:rep:992046915170619414>"
dash = "<:term_dash:992047477433831456>"

################ EMBEDS ##################


@client.command(aliases=["h"])
async def help(ctx):
    embed = discord.Embed(
        title=f'',
        description=
        f'{dash} Want To See All Commands??\n{reply} Use `.cmds` To View All',
        color=0x2f3136)
    embed.set_footer(text=f"Requested by {ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    embed.set_thumbnail(url="")
    await ctx.send(embed=embed)


@client.command(aliases=["cmd"])
async def cmds(ctx):
    embed = discord.Embed(
        title=f'Commands Menu',
        description=
        f'**Moderation & Admin Cmds\n```ar | rr | lock | unlock | hide | unhide | purge | nick | ban | kick | lockall | unlockall | hideall | unhideall | roleall | purge | nuke```\n\nUtility Cmds\n```mc | av | banner | ping | say | truth | dare```\n\nRoles Cmds\n```To Many Cmds, Use .roles To View Those Cmds```\n\nExtra Cmds\n```about | dev```**',
        color=0x2f3136)
    embed.set_footer(text=f"Requested by {ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


@client.command(aliases=["c"])
async def codes(ctx):
    embed = discord.Embed(
        title=f'CodeX | Codes <:Flantic_oki_oki:1039471757922418729>',
        description=
        f'>>> **Dont Use These Codes In Your Main Accounts Or Your Any Bot Because If Anything Happens Then We Are Not Responsible And Its Your Mistake.\n\n[Apolex](https://replit.com/@Fenix1337/ApoleX#main.py)\n[Multipurpose Code](https://replit.com/@Fenix1337/Multipurpose-Bot-Code#main.py)\n[Zector](https://replit.com/@Fenix1337/Zector#main.py)\n[CodeZ](https://replit.com/@Fenix1337/CodeZ#main.py)\n[Axiom Bot](https://replit.com/@Fenix1337/Axiom#main.py)\n[AstroZ New](https://replit.com/@NotHerHacker/Astroz-Open-Source-Bot)\n[Discord Auth Bot](https://replit.com/@Fenix1337/Auth-bot#kalash.js)\n[Clan Manager Bot](https://replit.com/@Fenix1337/simpleclanbotbyspence#main.py)\n[Music Bot](https://replit.com/@Fenix1337/Music-Bot-for-Discord)\n\nNOTE: We Respect Discord [TOS](https://discord.com/terms) And [Guidelines](https://discord.com/guidelines)**',
        color=0x2f3136)
    embed.set_footer(
        text=f"CodeX By FenixPlayZ",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@client.command(aliases=["tool"])
async def tools(ctx):
    embed = discord.Embed(
        title=f'CodeX | Tools <:Flantic_oki_oki:1039471757922418729>',
        description=
        f'>>> **Dont Use These Tools In Your Main Accounts Or Your Any Bot Because If Anything Happens Then We Are Not Responsible And Its Your Mistake.\n\n[Multi-Tool](https://replit.com/@Fenix1337/Multitool-In-Go#.gitattributes)\n[AFK SelfBot](https://replit.com/@Fenix1337/AFK-SB#main.py)\n[Account Nuker](https://replit.com/@Fenix1337/Discord-account-nuker-1)\n[E-Mail Gen](https://replit.com/@Fenix1337/EMAIL-GEN#Main.py)\n[Server Cloner](https://replit.com/@Fenix1337/Working-Server-Cloner#main.py)\n[Auth Bot](https://replit.com/@Fenix1337/Auth-bot#kalash.js)\n[Vanity Sniper](https://github.com/RisinPlayZ/vanity-sniper)\n[Temp-Mail](https://github.com/RisinPlayZ/tempmail-python)\n[URL Grabber](https://github.com/exploitxd/URLGrabber)\n[Owl Spammer](https://github.com/exploitxd/owl-spammer)\n[J4J Bot](https://replit.com/@TecnoPlayZ3301/Discord-J4J-Bot)\n[Discord RPC](https://replit.com/@TecnoPlayZ3301/Custom-Discord-Rpc?v=1)\n[Token VC Joiner](https://replit.com/@TecnoPlayZ3301/Discord-Nukdollar-Bot)\n\nNOTE: We Respect Discord [TOS](https://discord.com/terms) And [Guidelines](https://discord.com/guidelines)**',
        color=0x2f3136)
    embed.set_footer(
        text=f"CodeX By FenixPlayZ",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@client.command(aliases=["ex"])
async def exodus(ctx):
    embed = discord.Embed(
        title=f'Exodus Address For Payemnts',
        description=
        f'> **_Fenix Exodus Addresses_**\n\n> **_ - BitCoin_**\n> **_bc1qckrdllym06h0eq73zvqxm403xn7a8kadxyrkmw_**\n\n> **_- LiteCoin_**\n> **_LXNnqvBtUd8eKs2VNucvCxqp8TQgBrbFbc_**\n\n> **_- Solana_**\n> **_8MaLdC9LC4AC3N55BzCMupd6niSpXRDNDWWTX4TEZFPX_**\n\n> **__- Long Press The Embed To Copy All Address__**',
        color=0x2f3136)
    embed.set_footer(
        text=f"Fenix Exodus Wallet Address",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@client.command(aliases=["cb"])
async def coinbase(ctx):
    embed = discord.Embed(
        title=f'CoinBase Address & Email For Payemnts',
        description=
        f'> **_Fenix CoinBase Addresses_**\n\n> **_- BitCoin_**\n> **_36kSQnYoihBdEBSZNQqJouHSrFNLbvDdDE_**\n\n> **_- LiteCoin_**\n> **_MMkN5xDL3CghaH4koy4GbHcqLSHj3DnAM7_**\n\n> **_- Solana_**\n> **_B5fmkEwMBrmDPhN9WU4RT4CG4kDFu6sveB1FzeEQZspW_**\n\n> **_- Email_**\n> **_fenixplayz777@gmail.com_**\n\n> **__- Long Press The Embed To Copy All Address__**',
        color=0x2f3136)
    embed.set_footer(
        text=f"Fenix CoinBase Wallet Address",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@client.command(aliases=["bitcoin"])
async def btc(ctx):
    embed = discord.Embed(
        title=f'BitCoin Wallet Address & Email For Payemnts',
        description=
        f'**_> CoinBase: `36kSQnYoihBdEBSZNQqJouHSrFNLbvDdDE`\n> Exodus: `bc1qckrdllym06h0eq73zvqxm403xn7a8kadxyrkmw`\n\n> Coinbase Email: `fenixplayz777@gmail.com`_**',
        color=0x2f3136)
    embed.set_footer(
        text=f"Fenix BitCoin Wallet Address",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@client.command(aliases=["litecoin"])
async def ltc(ctx):
    embed = discord.Embed(
        title=f'LiteCoin Wallet Address & Email For Payemnts',
        description=
        f'**_> CoinBase: `MMkN5xDL3CghaH4koy4GbHcqLSHj3DnAM7`\n> Exodus: `LXNnqvBtUd8eKs2VNucvCxqp8TQgBrbFbc`\n\n> Coinbase Email: `fenixplayz777@gmail.com`_**',
        color=0x2f3136)
    embed.set_footer(
        text=f"Fenix LiteCoin Wallet Address",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


@commands.is_owner()
@client.command(aliases=["solana"])
async def sol(ctx):
    embed = discord.Embed(
        title=f'Solana Wallet Address & Email For Payemnts',
        description=
        f'**_> CoinBase: `B5fmkEwMBrmDPhN9WU4RT4CG4kDFu6sveB1FzeEQZspW`\n> Exodus: `8MaLdC9LC4AC3N55BzCMupd6niSpXRDNDWWTX4TEZFPX`\n\n> Coinbase Email: `fenixplayz777@gmail.com`_**',
        color=0x2f3136)
    embed.set_footer(
        text=f"Fenix Solana Wallet Address",
        icon_url=
        f"https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/997049816003661854/a_35d186326a62399eb05b4db4b0c53e9d.gif?size=1024"
    )
    await ctx.send(embed=embed)


#################################
@client.command(aliases=["latency"])
async def ping(ctx):
    embed = discord.Embed(color=0x2f3136,
                          description=f"Ping - {int(client.latency * 1000)}ms")
    await ctx.send(embed=embed)


@client.command(aliases=["a"])
async def about(ctx):
    embed = discord.Embed(
        color=0x2f3136,
        description=
        f"Hey, i am the manager of this server and am developed by fenix.")
    await ctx.send(embed=embed)


@client.command(aliases=["d"])
async def dev(ctx):
    embed = discord.Embed(color=0x2f3136,
                          description=f"My developer is: Fenix")
    await ctx.send(embed=embed)


################# MOD CMDS #################
@client.command(aliases=['ar'])
@commands.has_permissions(administrator=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    ro = role.id
    rrole = ctx.guild.get_role(ro)
    await member.add_roles(rrole)
    await ctx.reply(f'Added {role.name} to {member.name}',
                    mention_author=False)


@client.command(aliases=['rr'])
@commands.has_permissions(administrator=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    ro = role.id
    rrole = ctx.guild.get_role(ro)
    await member.remove_roles(rrole)
    await ctx.reply(f'Removed {role.name} from {member.name}',
                    mention_author=False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    description = f'<:success:992024105975037992> | {ctx.channel.mention} Is Now Hidden'
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=description))


@client.command(aliases=["nick", "setnick"])
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nick):
    old_name = member.name
    await member.edit(nick=nick)
    description = f"Changed Nick of {old_name} To {nick}"
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=description))


@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    description = f'<:success:992024105975037992> {ctx.channel.mention} Is Now Visible'
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=description))


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = " no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'{tick} | Kicked {member.mention} Reason: {reason}')


@commands.cooldown(3, 300, commands.BucketType.user)
@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send(
        '**<:success:992024105975037992> | Unbanning  {} Members**'.format(
            len(banlist)))
    for users in banlist:
        await ctx.guild.unban(user=users.user, reason=f"By {ctx.author}")


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    description = f'<:success:992024105975037992> {ctx.channel.mention} Has Been Locked!'
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=description))


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    description = f'<:success:992024105975037992> {ctx.channel.mention} Has Been Unlocked!'
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                        description=description))


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def lockall(ctx):
    await ctx.send(f"**{tick} | Locking All Channels Please Wait!**")
    for idk in ctx.guild.channels:
        await idk.set_permissions(ctx.guild.default_role, send_message=False)
    await ctx.send(f"**{tick} | Successfully Locked All Channels**")


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def unlockall(ctx):
    await ctx.send(f"**{tick} | Unlocking All Channels Please Wait!**")
    for idk in ctx.guild.channels:
        await idk.set_permissions(ctx.guild.default_role, send_message=True)
    await ctx.send(f"**{tick} | Successfully Unlocked All Channels**")


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def unhideall(ctx):
    await ctx.send(f"**{tick} | UnHiding All Channels Please Wait!**")
    for idk in ctx.guild.channels:
        await idk.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send(f"**{tick} | Successfully UnHidden All Channels**")


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def hideall(ctx):
    await ctx.send(f"**{tick} | Hiding All Channels Please Wait!**")
    for idk in ctx.guild.channels:
        await idk.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send(f"**{tick} | Successfully Hidden All Channels**")


@client.command(aliases=["rall"])
@commands.has_permissions(administrator=True)
async def roleall(ctx, role: discord.Role):
    rrole = ctx.guild.get_role(role.id)
    if role.permissions.administrator or role.permissions.ban_members:
        await ctx.send(embed=discord.Embed(
            color=discord.Colour(0x2f3136),
            title=f"",
            description=
            f"Use A Role Without Dangerous Perms Like: `Administartors`, `Ban Members` & Much More!"
        ))
    else:
        mm = await ctx.send(embed=discord.Embed(
            color=discord.Colour(0x2f3136),
            title=f"",
            description=
            f"<a:jhebwbsajabhJa:1024918925319872522> Adding Mentioned Role Members"
        ))
        for all in ctx.guild.members:
            try:
                await all.add_roles(rrole)
            except:
                pass
        await mm.edit(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                          title=f"",
                                          description=f"Added Mentioned Role!")
                      )


@client.command(aliases=["nuke"])
@commands.has_permissions(administrator=True)
async def channelnuke(ctx):
    channelthings = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    embed = discord.Embed(description=f'Channel Nuked By {ctx.author.name}',
                          color=0x2f3136)

    nukedchannel = channelthings[0].text_channels[-1]
    await nukedchannel.edit(position=channelthings[1])
    await nukedchannel.send(embed=embed)


@client.command("purge")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send((f"Purged {amount} Messages"), delete_after=5)


############### UTIL CMDS ###########


@client.command(aliases=["mc"])
async def membercount(ctx):
    scembed = discord.Embed(colour=discord.Colour(0x2f3136))
    scembed.add_field(
        name='**<:_dash:1007475039731466320> Members**',
        value=f"<:rep:992046915170619414> {ctx.guild.member_count}")
    await ctx.send(embed=scembed, mention_author=False)


@client.command()
async def banner(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    bid = await client.http.request(
        discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]

    if banner_id:
        embed = discord.Embed(color=0x2f3136)
        embed.set_author(name=f"Banner Of {user.name}")
        embed.set_footer(text=f"Requested by {ctx.author.name}",
                         icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(
            url=
            f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
        )

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            color=0x2f3136,
            description=f"Sorry, User Dont Have A Banner To Show!")
        await ctx.send(embed=embed)


@client.command(aliases=['av'])
async def showavatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    emb = discord.Embed(color=0x2f3136, title=f"Avatar Of {member.name}")
    emb.set_image(url=member.avatar_url)
    emb.set_footer(text=f"Requested by {ctx.author.name}",
                   icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=emb)


@client.command()
async def say(ctx, *, arg):
    description = (arg)
    await ctx.send(embed=discord.Embed(color=discord.Colour(0x2f3136),
                                       description=description))


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def truth(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/truth").text
    data = json.loads(content)
    text = data["question"]
    idk = discord.Embed(color=discord.Colour(0x2f3136), description=text)
    await ctx.reply(embed=idk, mention_author=False)


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def dare(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/dare").text
    data = json.loads(content)
    text = data["question"]
    idk = discord.Embed(color=discord.Colour(0x2f3136), description=text)
    await ctx.reply(embed=idk, mention_author=False)


###################### SERVER ROLE CMDS ##################
@commands.check(guildowner)
@client.command()
@commands.has_permissions(administrator=True)
async def kira(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536798074286120)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["of", "order"])
@commands.has_permissions(administrator=True)
async def order_of(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536969721983047)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["vet", "ve"])
@commands.has_permissions(administrator=True)
async def veteran(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043537204120670238)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["ha", "hasira"])
@commands.has_permissions(administrator=True)
async def hashira(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043752138817417266)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["e", "elite"])
@commands.has_permissions(administrator=True)
async def elites(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536969898139748)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["t", "titans"])
@commands.has_permissions(administrator=True)
async def titan(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043752139043905608)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["fd", "fr"])
@commands.has_permissions(administrator=True)
async def founder(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125018690879498)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["o", "ow"])
@commands.has_permissions(administrator=True)
async def own(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125020045652080)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["haxor", "haxxor"])
@commands.has_permissions(administrator=True)
async def hacker(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043751901965078678)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["prog", "fafs"])
@commands.has_permissions(administrator=True)
async def programmer(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536796920856606)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["devs", "develop"])
@commands.has_permissions(administrator=True)
async def developer(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536657040822293)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["newbie", "new-dev", "n-dev"])
@commands.has_permissions(administrator=True)
async def n_dev(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043751902401269770)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["st", "staf"])
@commands.has_permissions(administrator=True)
async def staff(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125023044587590)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["ad", "admins"])
@commands.has_permissions(administrator=True)
async def admin(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125021027115018)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["mod", "mods"])
@commands.has_permissions(administrator=True)
async def m(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125022058913802)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["buddy", "buddies"])
@commands.has_permissions(administrator=True)
async def budi(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043752511112220702)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["vip", "vips"])
@commands.has_permissions(administrator=True)
async def v(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125025192054785)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["guest", "g"])
@commands.has_permissions(administrator=True)
async def guests(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125023975714836)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command(aliases=["cute", "girl"])
@commands.has_permissions(administrator=True)
async def cutie(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1038125026001555537)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command()
@commands.has_permissions(administrator=True)
async def perms(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536658513002506)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command()
@commands.has_permissions(administrator=True)
async def audit(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043566739893534801)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@commands.check(guildowner)
@client.command()
@commands.has_permissions(administrator=True)
async def vcperm(ctx, user: discord.Member):
    guild = client.get_guild(997049816003661854)
    role = guild.get_role(1043536658286530662)
    if '' in str(user.name) or '' in str(user.name) or '' in str(user.name):
        await user.add_roles(role)
        await ctx.send(
            f"{tick} Particular Role Has Been Assigned To The Mentioned User.")
    else:
        await ctx.send(f"{cross} You Are Not Authorized To Use These Cmds!")


@client.command(aliases=["role", "r"])
async def roles(ctx):
    embed = discord.Embed(
        color=0x2f3136,
        description=
        f"```kira | order | veteran | hashira | elite | titan | founder | own | hacker | programmer | devs | new-dev | staff | admin | mod | buddy | vip | guest | cutie\n\nThese Cmds Can Only Be Used By Authorized Users By Fenix```"
    )
    await ctx.send(embed=embed)


client.run(token)
