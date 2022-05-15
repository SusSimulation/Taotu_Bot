from subprocess import call

import discord

from Commands.AddPhotoCommand import *
from Commands.BlackJack import *
from Commands.DeveloperCommand import *
from Commands.HelpCommand import *
from Commands.HighschoolDXDp import *
from Commands.MiskCommand import *
from Commands.On_Ready import *
from Commands.PhotoCommand import *
from Commands.Quoting import *
from Commands.SlapperCommand import *
from Commands.TrustIssuesGame import *
from Commands.TwentyQuestionsGameCommand import *
from Commands.VoiceKick import *
from Commands.ZeldaCommand import *
from Commands.AiGennies import *
from Commands.SmahsOrPass import *
from Module import *

if __name__ == "__main__":
    On_ready_Event()
    Help_Command()
    TrustIssuesGame_Command()
    Questions20Game_Command()
    Photo_Command()
    AddPhoto_Command()
    Developer_Command()
    Slapper_Command()
    DXD_Command()
    Misk_Command()
    KickUserInVc_Command()
    Zelda_Command()
    BlackJackGame_Command()
    Quotings()
    Ai_Command()
    AddPhotoAI_Command()
    SorPass()

    @client.command(name="quit")
    async def QUIT(ctx):
        if isinstance(ctx.channel, discord.DMChannel) and ctx.author.id == 800558571129274450:
            quit()

    @client.command(name="reboot")
    async def ResetBot(ctx):
        if isinstance(ctx.channel, discord.DMChannel) and ctx.author.id in DEVELOPERS:
            AddAudit(ctx,"$reset",ctx)
            call(["python", "C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\__main__.py"])
            quit()

    with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\TOKEN.txt", "r") as content:
        print("TOKEN OPENING")
        client.run(f"{str(content.read())}")
