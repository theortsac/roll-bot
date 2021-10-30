from nextcord.ext import commands
import nextcord
import random

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@ bot.event
async def on_ready():
    print("Connected.")

numbersToSearch = [545, 514, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 444, 443, 442, 441, 440, 439,
                   438, 437, 436, 435, 434, 433, 432, 431, 430, 429, 427, 426, 425, 423, 422, 421, 420, 419, 418, 417, 416, 415, 413, 261, 96, 74, 55, 52, 46, 23]

global howthebotisdoing
howthebotisdoing = True


@bot.command()
@ commands.has_guild_permissions(use_slash_commands=True)
async def roll(ctx, *, message):
    if howthebotisdoing:
        try:
            if message.startswith("nfh"):
                randomVar = []
                split_message = message.split()
                if (len(split_message) == 1):
                    while randomVar == [] or len(randomVar) != len(set(randomVar)):
                        randomVar = random.sample(numbersToSearch, 1)
                else:
                    if (int(split_message[1]) < 10):
                        while randomVar == [] or len(randomVar) != len(set(randomVar)):
                            randomVar = random.sample(
                                numbersToSearch, int(split_message[1]))
                    else:
                        await ctx.reply(embed=nextcord.Embed(title="You can only roll the dice up to 9 times!", color=0xFF0000))
                if (len(randomVar) > 1):
                    embedTitle = f"{ctx.author.display_name} rolls: "
                    for i in randomVar:
                        embedTitle += f"{i}, "
                    embedTitle = embedTitle[:-2]
                    embedTitle += "."
                    embedTitle += " (NFH)"
                else:
                    embedTitle = f"{ctx.author.display_name} rolls a {randomVar[0]}. (NFH)"
                await ctx.send(embed=nextcord.Embed(
                    title=embedTitle, color=0x7CFC00))
                await ctx.message.delete()
# if not nfh
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
                if number != '4' and number != '6' and number != '20' and number != '50' and number != '100' and number != '550' and number != '600':
                    await ctx.reply(embed=nextcord.Embed(
                        title="The only options available are: 4, 6, 20, 50, 100, 550 and 600", color=0xFF0000))
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
                        title=f"{ctx.author.display_name} rolls a {title}. (d{number})", color=0x7CFC00)
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