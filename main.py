"""
Quoicoubot
Bot Discord goofy
"""
import os
import random
import discord
from discord.ext import commands

# Gestion des intents
intents = discord.Intents.all()

# Création du bot
bot = commands.Bot(command_prefix="!", description="Quoicoubot", intents=intents)

# Mots à répondre
mots_a_repondre = ["oui", "quoi", "non"]

# Gestion des mots clés
mots_cles = {
    "quoi": ["quoi ?", "quoi", "koi", "pourquoi", "pourquoi ?", "quoi?", "pourquoi?", "pq", "pq?", "pq ?", "pk", "pk?",
             "pk ?"],
    "oui": ["oui", "oui ?", "oui?", "ui", "ui?", "ui ?", "uii", "uii?", "uii ?"],
    "non": ["non", "nn", "non?", "non ?", "nn?", "nn ?"]
}

# Gestion des réponses
reponses = {
    "quoi": ["feur", "coubeh😹", "feuse"],
    "oui": ["stiti😹", "stiti"],
    "non": ["bril😹", "bril"]
}


# Gestion des events / commandes
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    for mot in mots_a_repondre:
        await traite_message(message, mot)


@bot.command()
async def coucou(ctx):
    await ctx.send("Double coucou")


# Traitement des messages
async def traite_message(message, mot):
    for end in mots_cles[mot]:
        if message.content[-len(end):] == end:
            await message.reply(random.choice(reponses[mot]))
            return

# Run
bot.run(os.getenv('DISCORD_TOKEN'))