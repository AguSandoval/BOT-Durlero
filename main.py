import os
import discord
from discord.ext import commands, tasks
import youtube_dl
import discord.voice_client
import requests
import nacl

client = commands.Bot(command_prefix = '!')
status = discord.Game("ser Elon Musk")

@client.event
async def on_ready():
  print('-- -- -- --- BOT Musical está en línea! --- -- -- --')
  await client.change_presence(status=discord.Status.idle, activity=status)

#Conecta el BOT a un canal de Audio
@client.command(pass_content=True)
async def join (ctx):
  song_there = os.path.isfile('song.mp3')
  try:
    if song_there:
      os.remove('song.mp3')
      print('song.mp3 removido OK.')
  except:
    await ctx.send('Esperá a que termine para continuar con otro archivo')
  channel = ctx.message.author.voice.channel
  if not channel:
    await ctx.send("**Flaco**, primero entrá al canal donde querés que ponga música y despues llamame. ")
    return
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice and voice.is_connected():
    await voice.move_to(channel)
  else:
    voice = await channel.connect()

  ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
  url = 'https://www.youtube.com/watch?v=l2UiY2wivTs&ab_channel=DopeLyricsDopeLyrics'
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir('./'):
    if file.endswith('.mp3'):
      os.rename(file, 'song.mp3')
  voice.play(discord.FFmpegPCMAudio('song.mp3'))


#Desconecta el BOT de un canal de Audio
@client.command(pass_content=True)
async def leave(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  try:
    await voice.disconnect()
  except:
    print()


@client.command(name = 'ping', help = '- Muestra el ping del bot')
async def ping(ctx):
  await ctx.send(f'La latencia es {round(client.latency * 1000)}ms')


#token = os.environ['token']

client.run('ODU0MTc0NDI5NTI0NjU2MTQ4.YMgF7Q.Oiilsvzj7NkH8Ppc7B-C2R8n44E')
