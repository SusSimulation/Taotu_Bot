from Module import *

def Photo_Command():
    @client.command()
    async def photo(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
        AddAudit(ctx,"$photo",ctx)
        if not isinstance(ctx.channel, discord.DMChannel):
            if ctx.guild.id in CoolGuilds or ctx.author.id in DEVELOPERS:
                try:
                    fn = random.choice(os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo"))
                    await ctx.channel.send(file= discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo\\{fn}"))
                except discord.errors.HTTPException:
                    pass
        else:
            with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\NOTTHISTYPEOFCHANNEL.txt","r") as f:
                s = f.read()
            await ctx.channel.send(f"{s}")