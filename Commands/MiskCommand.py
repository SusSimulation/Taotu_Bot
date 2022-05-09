from Module import *

def Misk_Command():
    @client.command()
    async def hen(ctx):
        if ctx.channel.id == 973079336301260870 or ctx.author.id in DEVELOPERS:
            try:
                while True:
                    fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\MiskFiles"))
                    await ctx.channel.send(file = discord.File(
                        f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\MiskFiles\\{fn}"))

                    break
            except discord.errors.HTTPException:
                    pass
        else:
            await ctx.channel.send("This feature is not supported in this channel.")