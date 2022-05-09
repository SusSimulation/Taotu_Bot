from Module import *

def Photo_Command():
    @client.command()
    async def photo(ctx):
        if ctx.channel.id == 973079336301260870 or ctx.author.id in DEVELOPERS:
            try:
                fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo"))
                await ctx.channel.send(file= discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo\\{fn}"))
            except discord.errors.HTTPException:
                pass
        else:
            await ctx.channel.send("This feature only works in few specific discord channels.")