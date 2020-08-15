import discord, urllib.request, json
from discord.ext import commands
from info import token, omdbKey, reddit
from random import randint

bot = commands.Bot(command_prefix = '.')
emb = discord.Embed()
att = discord.Attachment

global artCount, analogCount
artCount = 0
analogCount = 0
artworks = []  # url of artwork
analogs = []

def main():
    get_art()
    bot.run(token)

def get_art():
    global artCount, analogCount
    artSub = reddit.subreddit("ArtPorn")
    new_artSub = artSub.new(limit=100)
    print("Getting from " + artSub.display_name)

    analogSub = reddit.subreddit("analog")
    new_analogSub = analogSub.new(limit=100)
    print("Getting from " + analogSub.display_name)

    for link in new_artSub:
        artworks.append(link)
        artCount = artCount + 1

    for link in new_analogSub:
        analogs.append(link)
        analogCount = analogCount + 1


''' --------------------Bot commands -------------------------'''

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_member_join(member):
    print(member + " has joined the server.")

@bot.event
async def on_member_remove(member):
    print(member + " has left the server.")

@bot.command()
async def ping(ctx): #context
    await ctx.send('Pong! ' + str(round(bot.latency * 1000)) + " ms")

@bot.command()
async def art(ctx):
    value = randint(0, 29)
    #emb.set_image(url="https://lh3.googleusercontent.com/J-mxAE7CPu-DXIOx4QKBtb0GC4ud37da1QK7CzbTIDswmvZHXhLm4Tv2-1H3iBXJWAW_bHm7dMl3j5wv_XiWAg55VOM=s0")
    filenameTemp = "art/art-" + str(value) + ".jpg"
    await ctx.send("Here is a cool image", file=discord.File(filenameTemp))
    #await ctx.send("Here is a cool image", file = "i.redd.it/uabfnvhig5g51.jpg")

@bot.command()
async def clap(ctx):
    emb.set_image(url="https://media1.tenor.com/images/e509e6ceb238801c758af109ff6d0e71/tenor.gif?itemid=4893625")
    await ctx.send(embed=emb)

@bot.command()
async def movie(ctx, *, arg):
    arg = arg.replace(" ", "+")
    movieUrl = "http://www.omdbapi.com/?t=" + arg + "&apikey=" + omdbKey
    with urllib.request.urlopen(movieUrl) as url:
        data = json.loads(url.read().decode())
        print(data)
        try: #Check if a movie is found
            title = data["Title"]
            year = data["Year"]
            director = data["Director"]
            runtime = data["Runtime"]
            genre = data["Genre"]
            x = ","

            lb_url = "https://letterboxd.com/film/" + title
            for char in x:
                lb_url = lb_url.replace(char, "").lower()
            lb_url = lb_url.replace(" ", "-").lower()

            await(ctx.send("\nTitle: " + title + "\nYear: " + year + "\nDirector: " + director +
                           "\nRuntime: " + runtime + "\nGenre: " + genre+ "\n\n" + lb_url))

        #If no movie is found :
        except KeyError as e:
            await(ctx.send("No movie found, try again"))

@bot.command()
async def redditart(ctx):
    rVal = randint(0, artCount - 1)
    current = artworks[rVal]
    print("ID: " + str(rVal) + "\nUrl: " + current.url
          + "\nAuthor: " + current.author.name)
    emb.set_image(url = artworks[rVal].url)
    await ctx.send("\nUrl: " + current.url
          + "\nAuthor: " + current.author.name, embed=emb)

@bot.command()
async def analog(ctx):
    rVal = randint(0, analogCount - 1)
    current = analogs[rVal]
    print("ID: " + str(rVal) + "\nUrl: " + current.url
          + "\nAuthor: " + current.author.name)
    emb.set_image(url = analogs[rVal].url)
    await ctx.send("\nUrl: " + current.url
          + "\nAuthor: " + current.author.name, embed=emb)


#Start the program
main()