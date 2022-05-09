from Module import *

def Zelda_Command():
    @client.command()
    async def zelda(ctx):
        if ctx.channel.id == 973079336301260870 or ctx.author.id in DEVELOPERS:
            while True:
                try:
                    fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\ZeldaFiles"))
                    await ctx.channel.send(file = discord.File(
                        f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\ZeldaFiles\\{fn}"))
                    
                    break
                except discord.errors.HTTPException:
                    pass
        else:
            await ctx.channel.send("This feature only works in few specific discord channels.")