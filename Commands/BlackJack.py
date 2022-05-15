from pyparsing import ParseExpression
from Module import *

class BlackJackGame:
    global check
    def __init__(self,c):
        self.c = c

        self.players = []
        self.decks = []
        self.cards = [1,1,2,3,4,5,6,7,8,9,10,10,10,10,11]#[1]+[i+1 for i in range(9)] + [10]*4 # 1-->(10*4)
        self.finished_players = []
        self.finished_decks = []

    async def get_players(self):
        def check(m):
            return m.channel.id == self.c.channel.id and not isinstance(m.channel,discord.DMChannel)
        while True:
            try:
                dealingWho = await client.wait_for("message",timeout=200,check=check)

                if dealingWho.content.lower() == "deal" and dealingWho.author.id not in self.players:
                    self.players.append(dealingWho.author.id)
                    card = random.choice(self.cards)
                    self.decks.append([self.cards[card]])
                    secondcard = random.choice(self.cards)
                    self.decks[self.players.index(dealingWho.author.id)].append(self.cards[secondcard])
                    embed = discord.Embed(title=f"Your Cards: {self.decks[self.players.index(dealingWho.author.id)]}",description=f"Your total: {sum(self.decks[self.players.index(dealingWho.author.id)])}", color=0xADD8E6)
                    await dealingWho.author.send(embed=embed)
                    embed = discord.Embed(title=f"{dealingWho.author} is dealt!",description=f"They have a ({self.decks[self.players.index(dealingWho.author.id)][0]}) and a ( ? )",color=0xADD8E6)
                    await self.c.channel.send(embed=embed)
                    await dealingWho.delete()

                elif dealingWho.content.lower() == "start" and dealingWho.author.id in self.players and len(self.players) > 0 and dealingWho.author == self.c.author:
                    break
            except asyncio.TimeoutError:
                break
    try:
        async def hit_or_stay(self):
            def checks(m):
                return m.channel.id == self.c.channel.id and not isinstance(m.channel,discord.DMChannel) and m.content.lower() in ["h","hit","s","stand","stay"]
            
            embed = discord.Embed(title=f"Hit or stand?",description=f"Type Hit if you want to get another card. Type stand if you dont want another card.",color=0xADD8E6)
            await self.c.channel.send(embed=embed)
            while True:
                if len(self.players) > 0:
                    for player in self.players:
                        username = await client.fetch_user(player)
                        embed = discord.Embed(title=f"{username}'s turn!",description=f"Type 'hit' or 'stand'",color=0xADD8E6)
                        await self.c.channel.send(embed=embed)

                        HitOrStand = await client.wait_for("message",timeout=150,check=checks)

                        if HitOrStand.content.lower() in ["h","hit"]:
                            self.decks[self.players.index(player)].append(random.choice(self.cards))
                            embed = discord.Embed(title=f"Your Cards: {self.decks[self.players.index(player)]}",description= f"Total = {sum(self.decks[self.players.index(player)])}",color=0xADD8E6)
                            await HitOrStand.author.send(embed=embed)
                            if sum(self.decks[self.players.index(player)]) > 21:
                                embed = discord.Embed(title=f"{HitOrStand.author} busted",description= f"Total = {sum(self.decks[self.players.index(player)])}",color=0xADD8E6)
                                await HitOrStand.channel.send(embed=embed)
                                del self.decks[self.players.index(player)]
                                del self.players[self.players.index(player)]
                            else:

                                embed = discord.Embed(title=f"{username} was dealt a card.", color=0xADD8E6)
                                await HitOrStand.channel.send(embed=embed)
                        elif HitOrStand.content.lower() in ["s","stand","stay"]:
                            embed = discord.Embed(title=f"{username} standed!", color=0xADD8E6)
                            await HitOrStand.channel.send(embed=embed)
                            self.finished_players.append(self.players[self.players.index(player)])
                            self.finished_decks.append(sum(self.decks[self.players.index(player)]))
                            del self.decks[self.players.index(player)]
                            del self.players[self.players.index(player)]
                else:
                    break

        async def CheckWinner(self):
            if len(self.finished_players) != 0:
                if int(self.finished_decks.count(max(self.finished_decks))) == 1:
                    winnerSUM = max(self.finished_decks)
                    user = await client.fetch_user(int(self.finished_players[self.finished_decks.index(winnerSUM)]))
                    embed = discord.Embed(title=f"The winner is {user.name}",description=f"Sum of {winnerSUM}",color=0xADD8E6)
                    await self.c.channel.send(embed=embed)
                    AddAudit(self.c,f"$bjack and {self.c.author} won the game.",self.c)
                elif int(self.finished_decks.count(max(self.finished_decks))) > 1:
                    winnerSUM = max(self.finished_decks)
                    winners = []
                    for item in self.finished_players:
                        if self.finished_decks[self.finished_players.index(item)] == winnerSUM:
                            user = await client.fetch_user(int(item))
                            winners.append(user.name)
                    embed = discord.Embed(title=f"There was a tie with the number; {winnerSUM}",description=f"Winners: {winners}",color=0xADD8E6)
                    await self.c.channel.send(embed=embed)

            else:
                embed = discord.Embed(title=f"It seems no one has won the game.",description=f"Better luck next time?",color=0xADD8E6)
                await self.c.channel.send(embed=embed)
    except asyncio.TimeoutError:
        pass




def BlackJackGame_Command():
    @client.command()
    async def bjack(ctx):
        AddAudit(ctx,"$bjack",ctx)
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
            embed = discord.Embed(title=f"Game Started!",description=f"Type 'deal' if you want to play black jack, after that the host/person who typed '$bjack' will type 'start' to start the game, type either 'hit' if you want one more card or 'stand' if you dont want anymore cards. Tips: The Highest number you can get is '11' and lowest is '1'.",color=0xADD8E6)
            await ctx.channel.send(embed=embed)
            NewGame = BlackJackGame(ctx)
            await NewGame.get_players()
            await NewGame.hit_or_stay()
            await NewGame.CheckWinner()
