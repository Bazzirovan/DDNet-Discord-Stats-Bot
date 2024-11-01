import os
import disnake
from disnake.ext import commands
import aiohttp
import matplotlib.pyplot as plt
import io
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


intents = disnake.Intents.all()


bot = commands.Bot(command_prefix='!', intents=intents)

def create_chart(data):
    labels = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(6, 6))
    wedges, texts = plt.pie(values, startangle=140, shadow=True, labels=None)
    plt.legend(wedges, [f"{label} ({value} hours)" for label, value in data.items()], title="Gamemodes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.axis('equal')
    plt.gca().set_facecolor('none')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', transparent=True)
    buffer.seek(0)
    plt.close()
    return buffer

async def fetch_player_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

@bot.slash_command(description="Показать статистику игрока")
async def stats(inter, name: str):
    await inter.response.defer()
    url = f"https://ddstats.tw/player/json?player={name}"
    data = await fetch_player_data(url)
    gametypes = data["most_played_gametypes"]
    info = data["profile"]
    points = info["points"]
    clan = info["clan"]
    ddrace_time = kog_time = fng2_time = fng2plus_time = 0
    fng_god_time = fng_re_time = fng_open_time = 0

    for gametype in gametypes:
        if gametype["key"] == 'DDraceNetwork':
            ddrace_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'Gores':
            kog_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'fng2':
            fng2_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'fng2+':
            fng2plus_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'godfng':
            fng_god_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'refng':
            fng_re_time = round(int(gametype['seconds_played']) / 3600)
        if gametype["key"] == 'openfng':
            fng_open_time = round(int(gametype['seconds_played']) / 3600)

    fng_time = fng2_time + fng2plus_time + fng_god_time + fng_re_time + fng_open_time
    total_time = ddrace_time + kog_time + fng_time
    chart_data = {
        "DDNet": ddrace_time,
        "KoG": kog_time,
        "FNG": fng_time
    }
    chart_image = create_chart(chart_data)
    embed = disnake.Embed(
        title=f"Статистика игрока {name}",
        description=f"**Клан:** {clan}\n**Поинты:** {points}\n**Общее время:** {total_time} hours",
        color=disnake.Color.blue()
    )
    file = disnake.File(fp=chart_image, filename="chart.png")
    embed.set_image(url="attachment://chart.png")
    await inter.followup.send(embed=embed, file=file)

bot.run(TOKEN)
