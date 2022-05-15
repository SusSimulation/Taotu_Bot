from Module import *


def On_ready_Event():
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))
        
        guild_count, guilds = 0, []

        for guild in client.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guilds.append(int(guild.id))
            guild_count += 1
        
        print(f"Bot is in " + str(guild_count) + " guilds!\n-------------------------------------------------------------------------------------------------------")