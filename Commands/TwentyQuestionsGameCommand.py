from Module import *


class TwentyQuestions:
    def __init__(self,question_limit,gameon,timeout,ctx):
        self.question_limit = int(question_limit)
        self.gameon = bool(gameon)
        self.timeout = bool(timeout)
        self.ctx = ctx


        self.embed = discord.Embed(title=f"{self.question_limit} Questions:",description=f"{self.ctx.author.mention}; DM Taotu the word.", color=0xADD8E6)
        self.embed.add_field(name="Yes",value="Means the question asked was correct",inline=True)
        self.embed.add_field(name="No",value="Means the question asked was incorrect",inline=True)
        self.embed.add_field(name="Done",value="Means the question asked was the word",inline=True)

    async def WaitForWord(self):
        while True:
            try:
                word = await client.wait_for("message",timeout=300,check=lambda ctx: ctx.author.id != BotId and isinstance(ctx.channel, discord.DMChannel))
            except asyncio.exceptions.TimeoutError:
                self.timeout = True
                break
            await word.channel.send("Received! The game has started.")
            break

    async def WaitingForReplies(self):
        for game_start in range(self.question_limit):

            try:
                reply = await client.wait_for("message",timeout=3200, check=lambda ctx: ctx.author.id != BotId and not isinstance(ctx.channel, discord.DMChannel))
            except asyncio.TimeoutError:
                self.timeout = True
                break
            
            if reply.content.lower() in ["yes","no","done","end"] and reply.author.id == self.ctx.author.id and reply.channel.id == self.ctx.channel.id:
                if self.timeout == False:
                    if reply.content.lower() == "done":
                        await reply.channel.send("Word discovered, game over!")
                        self.game = False
                        break

                    if reply.content.lower() == "end":
                        await reply.channel.send("Word was not discovered, game over you will never know the word!")
                        self.game = False
                        break

                    embed = discord.Embed(title=f"{self.question_limit-game_start-1} Questions left:",description=f"Type your question, then the word creator will reply with either a 'yes', 'no' or 'done.' Type 'END' if you want to end the game early.", color=0xADD8E6)
                    await self.ctx.channel.send(embed=embed)

                if self.gameon == False:
                    break
            else:
                break

            if self.question_limit-game_start-1 < 1:
                await reply.channel.send("Word was not discovered, game over you will never know the word!")
                break





def Questions20Game_Command():
    @client.command(name="20q")
    async def Questions20Game(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            NewGame = TwentyQuestions(20,True,False,ctx)
            await ctx.send(embed=NewGame.embed)
            
            await NewGame.WaitForWord()

            await NewGame.WaitingForReplies()



