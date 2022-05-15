from numpy import isin
from Module import *

def DXD_Command():
    @client.command()
    async def dxd(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
        AddAudit(ctx,"$dxd",ctx)
        if not isinstance(ctx.channel, discord.DMChannel):
            if ctx.channel.is_nsfw() or ctx.author.id in DEVELOPERS:
                while True:
                    try:
                        fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\DxdFiles"))
                        await ctx.channel.send(file = discord.File(
                            f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\DxdFiles\\{fn}"))
                        break
                    except discord.errors.HTTPException:
                        pass
        else:
            with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\NOTTHISTYPEOFCHANNEL.txt","r") as f:
                s = f.read()
            await ctx.channel.send(f"{s}")