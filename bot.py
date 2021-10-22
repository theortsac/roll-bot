from nextcord.ext import commands
import nextcord
import random

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@ bot.event
async def on_ready():
    print("Connected.")


howthebotisdoing = True


@bot.command()
@ commands.has_guild_permissions(use_slash_commands=True)
async def roll(ctx, *, message):
    if howthebotisdoing:
        try:
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
                await ctx.reply(embed=nextcord.Embed(
                    title=f"The result is: {random.randint(1, number)}", color=0x7CFC00))
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
                    title=f"Results: {title}", color=0x7CFC00)
                await ctx.reply(embed=embed)
                return
        except:
            await ctx.reply(embed=nextcord.Embed(
                title="Command done wrong!", color=0xFF0000))
    else:
        return


@bot.command()
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
