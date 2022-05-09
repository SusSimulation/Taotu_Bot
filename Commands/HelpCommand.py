from Module import *

def Help_Command():
    @client.command()
    async def help(ctx):
        embed = discord.Embed(title=" The commands:",description=f"Requested by {ctx.author}", color=0xADD8E6)
        for i in range(len(COMMANDS)):
            embed.add_field(name=f"{COMMANDS[i]}",value=f"{COMMANDS_D[i]}",inline=True)
        await ctx.channel.send(embed=embed)