import discord
import requests
import random

TOKEN = "MTQ1NTUxODQ5ODQ2NDcyNzIyNA.G30ZHU.eGC5f6VfAETksymFQ96PEiL8RQCG07aevlgalY"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!gita":
        chapter = random.randint(1, 18)
        verse = random.randint(1, 50)

        url = f"https://vedicscriptures.github.io/slok/{chapter}/{verse}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            shloka = data.get("slok", "Verse not found")
            meaning = data.get("transliteration", "")

            reply = (
                f"📜 **Bhagavad Gita {chapter}:{verse}**\n\n"
                f"🕉️ {shloka}\n\n"
                f"📖 *{meaning}*"
            )
        else:
            reply = "❌ Could not fetch verse."

        await message.channel.send(reply)

client.run(TOKEN)
