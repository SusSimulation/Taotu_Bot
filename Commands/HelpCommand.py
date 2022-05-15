from Module import *

def Help_Command():
    @client.command()
    async def help(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
        AddAudit(ctx,"$help",ctx)

        embed = discord.Embed(title=" The commands:",description=f"Requested by {ctx.author}", color=0xADD8E6)
        for i in range(len(COMMANDS)):
            embed.add_field(name=f"{COMMANDS[i]}",value=f"{COMMANDS_D[i]}",inline=False)


        await ctx.channel.send(embed=embed)