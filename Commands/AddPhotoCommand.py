from Module import *
import shutil


class FileSaver:
    def __init__(self,c):
        self.c = c

    async def save(self):
        await self.c.channel.send(f'upload a {typefiles}.')

        msg = await client.wait_for("message",timeout=330, check=check)

        for attachment in msg.attachments:
                try:
                    open(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo\\{attachment.filename}")
                    rc = True
                except IOError:
                    rc = False

                if any(attachment.filename.lower().endswith(image) for image in typefiles) and not rc:
                    await attachment.save(attachment.filename)
                    newname = ''.join(random.sample(name,len(name)))
                    os.rename(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\{attachment.filename}",f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\{newname}.png")
                    shutil.move(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\{newname}.png","C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo")
                    await self.c.channel.send("Added!")

                else:
                    with open("C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\Commands\\Sentences\\CANTREPLACEFILE.txt","r") as f:
                        s = f.read()
                    await self.c.channel.send(f"{s}")


def AddPhoto_Command():

    @client.command()
    async def add(ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.message.delete()
        AddAudit(ctx,"$add",ctx)
        if not isinstance(ctx.channel, discord.DMChannel) or ctx.author.id in DEVELOPERS:

                NewObject = FileSaver(ctx)
                await NewObject.save()
        elif isinstance(ctx.channel, discord.DMChannel) and ctx.author.id in DEVELOPERS:
            NewObject = FileSaver(ctx)
            await NewObject.save()