from Module import *

def Misk_Command():
    @client.command()
    async def hen(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
        AddAudit(ctx,"$hen",ctx)
        if not isinstance(ctx.channel, discord.DMChannel):
            if ctx.channel.is_nsfw() or ctx.author.id in DEVELOPERS:
                try:
                    while True:
                        fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\MiskFiles"))
                        await ctx.channel.send(file = discord.File(
                            f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\MiskFiles\\{fn}"))

                        break
                except discord.errors.HTTPException:
                        pass
        else:
            with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\NOTTHISTYPEOFCHANNEL.txt","r") as f:
                s = f.read()
            await ctx.channel.send(f"{s}")