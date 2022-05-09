from Module import *

try:
    def KickUserInVc_Command():
        @client.command()
        async def unvc(ctx,member:discord.Member):
            if ctx.author.id in DEVELOPERS and member.id != 800558571129274450:
                await member.edit(voice_channel=None)
            if not ctx.author.id in DEVELOPERS:
                await ctx.author.edit(voice_channel=None)
                await ctx.channel.send("Your not a developer!")
except:
    pass