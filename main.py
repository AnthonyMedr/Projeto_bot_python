import discord
from discord.ext import commands
import random

#id_do_servidor =  

intents = discord.Intents.all()
client = commands.Bot(command_prefix= '.' , intents = intents) #se quiser mudar a tecla para ativar comandos apague o "." no meio das aspas e coloque a da sua preferencia.

@client.event
async def on_ready():
        print('Entramos como {0.user}' .format(client))



@client.command()
async def ola(ctx):
      await ctx.send(f'olá, {ctx.author}')


@client.command()
async def dado(ctx):
      numero = random.randint(1,6)
      await ctx.send(f'o número do dado de {ctx.author} foi {numero}')



@client.command()
async def enviarembed(ctx):
    embed = discord.Embed(

        title= 'Jorge o pato',
        description = 'ele é um pato',
        color= 3014775

)
    embed.set_author(name= 'jorgin', icon_url='https://media.tenor.com/58ST5mncX7kAAAAi/mario-dance.gif')
    embed.set_thumbnail(url='https://www.tibiawiki.com.br/images/c/ca/Chopper_of_Carving_%28Overcharged%29.gif')
    embed.set_image(url='https://media.tenor.com/yTHoLS82szwAAAAd/pato-girando.gif')
    embed.set_footer(text='Pato com pé de pato girante')

    
    
    
    
    
    await ctx.send(embed = embed)  

client.run('MTExMTQ2NzAxOTEwODM2NDI4OA.GWYxQF.evh88bwPZRVi-JhLNB8bMLXmjAZfuV8SYHE6R4') #mude seu token 
