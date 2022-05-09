from Module import *  

def Developer_Command():
    @client.command()
    async def r(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            try:
                if ctx.author.id in DEVELOPERS:
                    embed = discord.Embed(title="Developer Only Commands:",description=f"Requested by {ctx.author} in {ctx.guild}", color=0xADD8E6)
                    for i,command in enumerate(DEVELOPER_COMMANDS):
                        embed.add_field(name=f"{command}",value=f"Command {i+1}",inline=True)
                    await ctx.author.send(embed=embed)
                    while True:
                        Task_Reply = await client.wait_for("message",timeout=100, check=check)
                        if Task_Reply.content.lower() == DEVELOPER_COMMANDS[0]:
                            print(f"dev opened by {ctx.author}")
                            try:
                                await ctx.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Main.py"))
                                for filename in os.listdir("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands"):
                                    await ctx.channel.send(file=discord.File(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\{filename}"))
                            except PermissionError:
                                pass
                            break

                        else:
                            pass
            except asyncio.TimeoutError:
                pass
        else:
            await ctx.channel.send("Please Type this command in my dms.")