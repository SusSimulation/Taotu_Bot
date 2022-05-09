from Module import *

def Slapper_Command():
    @client.command()
    async def slap(ctx, member:discord.User=None,*,args =None):
        if (member == ctx.message.author or member == None and args != None):
            await ctx.send(f"{ctx.message.author.mention} slaps themselves *{args}*!") 
        elif (member == ctx.message.author or member == None and args == None):
            await ctx.send(f"{ctx.message.author.mention} slaps themselves!") 
        elif (args == None):
            await ctx.send(f"{ctx.message.author.mention} slaps {member.mention}!") 
        else:
            await ctx.send(f"{ctx.message.author.mention} slaps {member.mention} *{args}*!") 
