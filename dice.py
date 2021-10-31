from nextcord.ext import commands
import nextcord
import random

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@ bot.event
async def on_ready():
    print("Connected.")

global howthebotisdoing
howthebotisdoing = True


@bot.command()
@ commands.has_guild_permissions(use_slash_commands=True)
async def roll(ctx, *, message):
    if howthebotisdoing:
        try:
            if message.startswith("rick"):
                await ctx.reply(
                    "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
# if not rickroll
            else:
                if (message[0] == 'd'):
                    repeat = 1
                else:
                    if (message[1] == 'd'):
                        if int(message[0]) != 0:
                            repeat = int(message[0])
                        else:
                            await ctx.reply(embed=nextcord.Embed(
                                title="Dice not rolled at all!", color=0xFF0000))
                            return
                    else:
                        await ctx.reply(embed=nextcord.Embed(
                            title="You can only roll the dice up to 9 times!", color=0xFF0000))
                        return
                number = message.split('d')[1]
                if number != '4' and number != '6' and number != '8' and number != '10' and number != '12' and number != '20' and number != '100':
                    await ctx.reply(embed=nextcord.Embed(
                        title="The only options available are: 4, 6, 8, 12, 20 and 100.", color=0xFF0000))
                    return
                number = int(number)
                if int(repeat) == 1:
                    randomNumber = random.randint(1, number)
                    if (randomNumber == 1):
                        await ctx.send(embed=nextcord.Embed(title=f"{ctx.author.display_name} rolls a natural 1! It's a critical failure! (d{number})",  color=0x7CFC00))
                    elif (randomNumber == number):
                        await ctx.send(embed=nextcord.Embed(title=f"{ctx.author.display_name} rolls a natural {number}! It's a critical success! (d{number})",  color=0x7CFC00))
                    else:
                        await ctx.send(embed=nextcord.Embed(
                            title=f"{ctx.author.display_name} rolls a {randomNumber}. (d{number})", color=0x7CFC00))
                    await ctx.message.delete()
                    return
                else:
                    numbers = []
                    title = ""
                    for i in range(int(repeat)):
                        randomNumber = random.randint(1, number)
                        numbers.append(randomNumber)
                        title += f"{randomNumber} + "
                    title = title[:-2]
                    titleSum = 0
                    for i in numbers:
                        titleSum += i
                    title += f"= {titleSum}"
                    embed = nextcord.Embed(
                        title=f"{ctx.author.display_name} rolls a {title}. ({int(repeat)}d{number})", color=0x7CFC00)
                    await ctx.send(embed=embed)
                    await ctx.message.delete()
                    return
        except:
            await ctx.reply(embed=nextcord.Embed(
                title="Command done wrong!", color=0xFF0000))
    else:
        return


@ bot.command()
@ commands.has_guild_permissions(administrator=True)
async def switch(ctx):
    global howthebotisdoing
    if (howthebotisdoing == True):
        howthebotisdoing = False
        await ctx.reply(embed=nextcord.Embed(
            title="The bot turned off.", color=0x7CFC00))
    elif (howthebotisdoing == False):
        howthebotisdoing = True
        await ctx.reply(embed=nextcord.Embed(
            title="The bot turned on.", color=0x7CFC00))


bot.run('TOKEN')
