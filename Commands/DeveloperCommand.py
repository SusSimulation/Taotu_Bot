from Module import *  

class Filesender:
    def __init__(self,c):
        self.c = c
    async def send(self):
        try:
            await self.c.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\__main__.py"))
            await self.c.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Module.py"))
            await self.c.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\AuditLog.txt"))
            for filename in os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands"):
                await self.c.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\{filename}"))
        except PermissionError:
            pass

def Developer_Command():
    @client.command()
    async def r(ctx):
        AddAudit(ctx,"$r",ctx)
        if isinstance(ctx.channel, discord.DMChannel):
            try:
                if ctx.author.id in DEVELOPERS:
                    embed = discord.Embed(title="Developer Only Commands:",description=f"Requested by {ctx.author} in {ctx.guild}", color=0xADD8E6)
                    for i,command in enumerate(DEVELOPER_COMMANDS):
                        embed.add_field(name=f"{command}",value=f"Command {i+1}",inline=True)
                    await ctx.author.send(embed=embed)
                    Task_Reply = await client.wait_for("message",timeout=100, check=check)
                    if Task_Reply.content.lower() == DEVELOPER_COMMANDS[0]:
                        AddAudit(ctx,"!files",ctx)
                        NewFiles = Filesender(ctx)
                        await NewFiles.send()
            except asyncio.TimeoutError:
                pass
            
        elif not isinstance(ctx.channel, discord.DMChannel) and ctx.author.id in DEVELOPERS:
            with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\PleaseDMmethis.txt","r") as f:
                s = f.read()

            await ctx.channel.send(f"{s}")

        else:

            with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\Developer_Command_NotDeveloper.txt","r") as f:
                s = f.read()

            await ctx.channel.send(f"{s}")