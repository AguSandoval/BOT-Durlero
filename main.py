import os
import discord
from discord.ext import commands, tasks
import requests
import scripts
import random

client = commands.Bot(command_prefix = '!')
status = discord.Game("ser Elon Musk")


@client.event
async def on_ready():
  print('-- -- -- --- BOT Durlero está en línea! --- -- -- --')
  await client.change_presence(status=discord.Status.idle, activity=status)


@client.command(pass_content=True)
async def btc(ctx, cant=0.0):
  btc_ars_ripio = scripts.btc_ars_RIPIO(scripts.read_api_RIPIO())
  btc_usd_ripio = scripts.btc_usd_RIPIO(scripts.read_api_RIPIO())
  btc_ars_buy, btc_ars_sell = btc_ars_ripio[0], btc_ars_ripio[1]
  btc_usd_buy, btc_usd_sell = btc_usd_ripio[0], btc_usd_ripio[1]
  btc_ars_sell_cant = scripts.format_value(float(btc_ars_sell) * cant)
  btc_ars_sell = scripts.format_value(float(btc_ars_sell))
  btc_ars_buy = scripts.format_value(float(btc_ars_buy))
  btc_usd_sell_cant = scripts.format_value(float(btc_usd_sell) * cant)
  btc_usd_sell = scripts.format_value(float(btc_usd_sell))
  btc_usd_buy = scripts.format_value(float(btc_usd_buy))
  if cant != 0:
    await ctx.send(f'Si vendes **{cant}BTC** en **RIPIO**, vas a obtener: \n'
                   f'>>\t\t__**${btc_ars_sell_cant}**__ ARS\n'
                   f'>>\t\t__**${btc_usd_sell_cant}**__ USD')
  elif cant == 0.0:
    #ars = btc_ars * float(cant)
    await ctx.send(f'\t\t>>>>> __**BITCOIN - RIPIO**__ <<<<<\n'
                   f'__*Valor en ARS:*__ \n'
                   f'\t- Compra: ${btc_ars_buy}\n'
                   f'\t- Venta: ${btc_ars_sell}\n\n'
                   f'__*Valor en Dólares:*__\n'
                   f'\t- Compra: {btc_usd_buy}USD\n'
                   f'\t- Venta: {btc_usd_sell}USD')
  else:
    await ctx.send('*Si tenes dudas, usá !help o !help btc* - Debes escribir sólo !btc para ver el valor del BITCOIN ó'
                   '!btc (cantidad) para saber cuantos pesos obtendrías de la venta de BTC en RIPIO')







@client.command(pass_content=True)
async def dolar(ctx, cant=0.0):
    dolar_blue = scripts.get_dollar_blue()
    dolar_blue_compra, dolar_blue_venta = dolar_blue[0], dolar_blue[1]
    if cant != 0:
        #dolar_blue_compra = scripts.format_value(str(dolar_blue_compra * cant))
        dolar_blue_venta = scripts.format_value(str(dolar_blue_venta * cant))
        await ctx.send(f'Si vendés $**{cant} Dólares**, obtendrías: \n'
                   f'>>\t\t__**${dolar_blue_venta}**__ ARS\n\n')
    elif cant == 0.0:
        dolar_blue_compra = scripts.format_value(str(dolar_blue_compra))
        dolar_blue_venta = scripts.format_value(str(dolar_blue_venta))
        await ctx.send(f'\t\t>>>>> __**DÓLAR BLUE**__ <<<<<\n'
                       f'__*Valor en ARS:*__ \n'
                       f'\t- Compra: ${dolar_blue_compra}\n'
                       f'\t- Venta: ${dolar_blue_venta}\n\n')

@client.command(pass_context=True)
async def eth(ctx, cant=0.0):
    eth_ars_ripio = scripts.eth_ars_RIPIO(scripts.read_api_RIPIO())
    eth_usd_ripio = scripts.eth_usd_RIPIO(scripts.read_api_RIPIO())
    eth_ars_buy, eth_ars_sell = eth_ars_ripio[0], eth_ars_ripio[1]
    eth_usd_buy, eth_usd_sell = eth_usd_ripio[0], eth_usd_ripio[1]
    eth_ars_sell_cant = scripts.format_value(float(eth_ars_sell) * cant)
    eth_ars_sell = scripts.format_value(float(eth_ars_sell))
    eth_ars_buy = scripts.format_value(float(eth_ars_buy))
    eth_usd_sell_cant = scripts.format_value(float(eth_usd_sell) * cant)
    eth_usd_sell = scripts.format_value(float(eth_usd_sell))
    eth_usd_buy = scripts.format_value(float(eth_usd_buy))
    if cant != 0:
        await ctx.send(f'Si vendes **{cant}ETH** en **RIPIO**, vas a obtener: \n'
                   f'>>\t\t__**${eth_ars_sell_cant}**__ ARS\n'
                   f'>>\t\t__**${eth_usd_sell_cant}**__ USD')
    elif cant == 0.0:
        await ctx.send(f'\t\t>>>>> __**ETHEREUM - RIPIO**__ <<<<<\n'
                       f'__*Valor en ARS:*__ \n'
                       f'\t- Compra: ${eth_ars_buy}\n'
                       f'\t- Venta: ${eth_ars_sell}\n\n'
                       f'__*Valor en Dólares:*__\n'
                       f'\t- Compra: {eth_usd_buy}USD\n'
                       f'\t- Venta: {eth_usd_sell}USD')

@client.command(pass_context=True)
async def ltc(ctx, cant=0.0):
    ltc_ars_ripio = scripts.ltc_ars_RIPIO(scripts.read_api_RIPIO())
    ltc_ars_buy, ltc_ars_sell = ltc_ars_ripio[0], ltc_ars_ripio[1]
    ltc_ars_sell_cant = scripts.format_value(float(ltc_ars_sell) * cant)
    ltc_ars_sell = scripts.format_value(float(ltc_ars_sell))
    ltc_ars_buy = scripts.format_value(float(ltc_ars_buy))
    if cant != 0:
        await ctx.send(f'Si vendes **{cant}LTC** en **RIPIO**, vas a obtener: \n'
                   f'>>\t\t__**${ltc_ars_sell_cant}**__ ARS')
    elif cant == 0.0:
        await ctx.send(f'\t\t>>>>> __**LITECOIN - RIPIO**__ <<<<<\n'
                    f'__*Valor en ARS:*__ \n'
                    f'\t- Compra: ${ltc_ars_buy}\n'
                    f'\t- Venta: ${ltc_ars_sell}\n')


@client.command(pass_context=True)

async def verga(ctx):
    b = random.randint(1, 15)
    await ctx.send('B' + b*'=' + 'D')

@client.command(pass_context=True)
async def gay(ctx):
    a = random.randint(0, 100)
    if a == 0:
        await ctx.send('**FULL MACHO PAPÁ!** CAMPEÓN, GORILA ESPALDA PLATEADA, COCOS DE ACERO, MAQUINOLA, LINCE DE LAS PRADERAS IBÉRICAS')
    elif a == 100:
        await ctx.send('**FULL GAY**, andá a hacerte ortear')
    else:
        await ctx.send('Saliste ' + str(a) + '% gay, **putito como la abuela**')


@client.command(name = 'ping', help = '- Muestra el ping del bot')
async def ping(ctx):
  await ctx.send(f'La latencia es {round(client.latency * 1000)}ms')


token = os.environ['token']
client.run(token)
