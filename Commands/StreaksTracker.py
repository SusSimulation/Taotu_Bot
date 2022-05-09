from Module import *

class StreaksTracker(commands.Bot):
    
    def __init__(self,context,starting_at):
        self.context = context
        self.starting_at = starting_at
        self.DailyLoop.start()


        @client.command(name="end_streak")
        async def CancelDailyLoop(ctx):
            self.DailyLoop.cancel()


    @tasks.loop(hours=24)
    async def DailyLoop(self):
        channel = client.get_channel(973046655869923428)
        await channel.send("Day {} for {}".format(self.starting_at, self.context.author.mention))
        self.starting_at += 1



def StreakTacking_Task():
    @client.command()
    async def start_streak(ctx,days_at=1):
        NewStreak = StreaksTracker(ctx,days_at)
    

    