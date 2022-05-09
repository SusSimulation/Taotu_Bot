from Module import *

def TrustIssuesGame_Command() -> None:
    @client.command()
    async def ti(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            try:
                await ctx.channel.send("How many people will be playing?")
                
                while True:
                    pp = await client.wait_for("message",timeout=100,check=lambda ctx: ctx.author != BotId and not isinstance(ctx.channel, discord.DMChannel))
                    if int(pp.content) > 10 and int(pp.content) > 1: 
                        await ctx.channel.send("Please Type a number between 1-10!")
                    else: 
                        break

                people_playing = int(pp.content)
                people, looping = [], 0

                await ctx.channel.send(f"{people_playing} people are playing.\nType your question; This question needs to be able to be awnsered with yes or no.")
                replys = []

                while True:
                    question = await client.wait_for("message",timeout=100, check=lambda ctx: ctx.author != BotId and not isinstance(ctx.channel, discord.DMChannel))
                    if question.author.id == ctx.author.id and not isinstance(question.channel, discord.DMChannel): 
                        break

                embed = discord.Embed(title=f"Question: {question.content}",description=f"Please DM me 'Yes' or 'No' corresponding to the question. I will only accept {people_playing} dms.", color=0xADD8E6)
                await ctx.channel.send(embed=embed)
                
                while looping < people_playing:
                    try:
                        looping += 1 
                        reply = await client.wait_for("message",timeout=60,check=lambda ctx: ctx.author != BotId and isinstance(ctx.channel, discord.DMChannel))
                        if isinstance(reply.channel, discord.DMChannel) and not reply.author.id in people and reply.content.lower() in ["yes","no"]:
                            people.append(reply.author.id)
                            replys.append(reply.content.lower())
                            await ctx.channel.send(f"{reply.author} awnsered.")
                            await reply.channel.send("Received!")
                        else:
                            await reply.channel.send("Please type 'yes' or 'no'")
                            looping -= 1
                    except asyncio.exceptions.TimeoutError:
                        pass
                    

                yess = replys.count("yes")
                nos = replys.count("no")
                embed = discord.Embed(title=f"{question.content}:",description="Counted all of the 'yes' and 'no'.", color=0xADD8E6)
                embed.add_field(name="Yes",value=f"{yess}",inline=True)
                embed.add_field(name="No",value=f"{nos}",inline=True)

                percentage = 100* yess//people_playing

                embed.add_field(name=f"{percentage}% said yes",value=f"{100-percentage}% said no",inline=True)
                await ctx.channel.send(embed=embed)
            except ValueError:
                await ctx.channel.send("Game stoped, Please type a number next time.")
            except asyncio.TimeoutError:
                pass
            except discord.errors.HTTPException:
                await ctx.channel.send("Bad Request! Restart!")