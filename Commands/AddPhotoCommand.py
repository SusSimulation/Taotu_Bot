from Module import *
import shutil

def AddPhoto_Command():
    @client.command()
    async def add(ctx):
        await ctx.channel.send(f'upload a {typefiles}.')

        msg = await client.wait_for("message",timeout=330, check=check)

        for attachment in msg.attachments:
                try:
                    open(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo\\{attachment.filename}")
                    rc = True
                except IOError:
                    rc = False

                if any(attachment.filename.lower().endswith(image) for image in typefiles) and not rc:
                    await attachment.save(attachment.filename)
                    shutil.move(f"C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\{attachment.filename}","C:\\Users\\jaspe\\OneDrive\\Desktop\\DISCORD_BOT\\photo")
                    await ctx.channel.send("Added!")

                else:
                    await ctx.channel.send("You can't replace a file that is already there.")