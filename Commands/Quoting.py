from Module import * 

def Quotings():
    @client.command() 
    async def quote(ctx): 
        if not isinstance(ctx.channel,discord.DMChannel):
            await ctx.message.delete()
        await ctx.channel.send(f"{random.choice(quotes())}")
        AddAudit(ctx,"$quote",ctx)

    