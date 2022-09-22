import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random

###
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext


with open("configuracion.json") as f:
    config = json.load(f)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="tubo", description="Keko habbo Hotel",
    options=[
                create_option(
                  name="keko",
                  description="Escribe el keko",
                  option_type=3,
                  required=True
                ),create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES - Hotel España",
                          value="es"
                      ),
                      create_choice(
                          name="BR - Hotel Brasil",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM - Hotel Estados unidos",
                          value="com"
                      ),
                      create_choice(
                          name="DE - Hotel Aleman",
                          value="de"
                      ),
                      create_choice(
                          name="FR - Hotel Frances",
                          value="fr"
                      ),
                      create_choice(
                          name="FI - Hotel Finalandia",
                          value="fi"
                      ),
                      create_choice(
                          name="IT - Hotel Italiano",
                          value="it"
                      ),
                      create_choice(
                          name="TR - Hotel Turquia",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL - Hotel Holandés",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])


async def _tubo(ctx:SlashContext, keko:str, hotel:str):
    await ctx.defer()
   
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}")
 
   
    try:

     habbo = response.json()['figureString']
    except KeyError:
        await ctx.send("El keko no existe!") 
  
   

   
    

    
    
   
    try:

     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=2&gesture=std&size=m"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1

   
    
    
    


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    ###

    


     tubo_maquina = Image.open(r"imagenes/cristal_tubo_maquina.png").convert("RGBA") #imagen
     img1 = tubo_maquina.resize((98,172), Image.ANTIALIAS)#tamaño de la saco


    ###
     cristal_tubo = Image.open(r"imagenes/cristal_tubo.png").convert("RGBA") #imagen
     img1 = cristal_tubo.resize((98,172), Image.ANTIALIAS)#tamaño de la saco
  
    ###
     tubo = Image.open(r"imagenes/tubo.png").convert("RGBA") #imagen
     img1 = tubo.resize((98,172), Image.ANTIALIAS)#tamaño de la saco
    ###
    ###
     arriba_tubo = Image.open(r"imagenes/arriba_tubo.png").convert("RGBA") #imagen
     img1 = arriba_tubo.resize((98,172), Image.ANTIALIAS)#tamaño de la saco
    ###


 
   
    
    
    
     
    
    
     img1.paste(tubo,(0,0), mask = tubo) #Posicion del tubo maquina
   
  
     img1.paste(tubo_maquina,(0,0), mask = tubo_maquina) #Posicion del tubo maquina
   
    
    
  
    
    ### 
     img1.paste(img2,(18,40), mask = img2) #Posicion del keko
    
     img1.paste(cristal_tubo,(0,0), mask = cristal_tubo) #Posicion del tubo maquina
     img1.paste(arriba_tubo,(0,0), mask = arriba_tubo) #Parte de arriba tubo Posicion
    
    
   ###
   
   
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
    except UnboundLocalError:
        habbo=":("    
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   