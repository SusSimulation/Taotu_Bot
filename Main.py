from Commands.On_Ready import *
from Commands.HelpCommand import *
from Commands.TrustIssuesGame import *
from Commands.TwentyQuestionsGameCommand import *
from Commands.PhotoCommand import *
from Commands.AddPhotoCommand import *
from Commands.DeveloperCommand import *
from Commands.SlapperCommand import *
from Commands.HighschoolDXDp import *
from Commands.MiskCommand import *
from Commands.VoiceKick import *
from Commands.ZeldaCommand import *
from Commands.StreaksTracker import *
from Module import *

if __name__ == "__main__":
    try:
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
        StreakTacking_Task()

        with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\TOKEN.txt", "r") as content:
            print("TOKEN OPENED")
            content = content.read()
            client.run(f"{content}")
    except discord.ext.commands.errors.CommandNotFound:
        pass

else:
    pass
