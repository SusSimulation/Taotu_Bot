import os, random
import discord
import asyncio
from discord.ext import commands,tasks

client = commands.Bot(command_prefix='$', help_command=None)


CODEFOREVENT = 26126

#Lists
DEVELOPERS, DEVELOPER_COMMANDS = [
        #gfdhgdfnhgfgfh
    ], [
        "!files"
        
    ]

COMMANDS = [
    "$help",
    "$20q",
    "$photo",
    "$zelda",
    "$dxd",
    "$add",
    "$start_streak",
    "$end_streak",
    "$hen",
    "$r",
    "$ti",
    "$unvc",
    "$slap",
]

COMMANDS_D = [
    "Displays a list of commands, your using it right now.",
    "Twenty questions game to play in a discord channel.",
    "Will post a random photo.",
    "A command that posts wholesome photos of Zelda.",
    "A command that posts wholesome photos of Highschool DxD.",
    "'$Add' is a command that allows you to add photos to the '$photo' command.",
    "Starts your streak and will post every day. $start_streak (what your streak is at)",
    "Will end your streak, you will need to type '$start_streak' again.",
    "This is a command that will send a photo from the subreddit r/h*****",
    "Developer only command, will only work in the dms of the bot.",
    "A custom game named trust issues, the inspiration to make this game was from Kaguya-sama.",
    "Will disconnect someone if they are in a voice chat. $unvc (Who?)",
    "Will slap someone, $slap (@ who?) (why?)",
]

typefiles = ["png",
    "gif",
    "jpg",
    "jpeg",
    "webp"
]


CoolGuilds = [
    #gdfhgfghfgxdth
    ]


#Vars
BotId = 914289358633304095


#Functions
def check(m):
    return m.author.id != BotId



    

        
        
