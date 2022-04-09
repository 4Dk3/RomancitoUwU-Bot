import os
import discord
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()

puteadas = ["no tiene manos para jugar osu", "ni con ayudas pudo pasar fisica", "UwU?", "maldit@ pro vida", "maldit@ pro aborto", "es amig@ de Michel Monroy", "¿De que color sos?", "graficame x²- 7", "a servicio social.", "no reconoce a Israel como un estado legítimo", "le gusta el chimbo sudado", "le encanta la guaracha", "sabe perfectamente que las clases de español, producción e investigación son Zzz", "¿ok? pero el fascismo. 🛐", "amanecio chistoso.", "reconoce a eso tilín como el mejor meme jamas creado", "se beso con Michel Monroy", "la arepa es colombiana", "le encanta el suero", "le gustan las burritas", "puta madre, el comunismo no funciona", "deja de decir mamadas y mejor dalas", "GTA SA > GTA IV", "when haces tus momos en el bot Bv, but te termina ofendiendo, oh mi lente de contacto :'v", "maravillosa jugada.jpg", "se esta volviendo salvaje.jpg", "mañana, ahorita ya es tarde", "no puedo, tengo tarea", "no hay pedo, yo me cojo a Michel Monroy", "callate putito" "pinche puto pendejo idiota perro bastardo", "¿verdad que Galeano es Zzz?","Che, ¿Cuánta' copa' tené'?👃* Se le muere maradroga *", "Perdona pero ni que fuera Galeano(Vaper), Tatiana(La folla baños), Manuela(No conoce el espacio personal), Bejarano(La come pitufos), Ortiz(Profe, ¿Qué clase es esta?), Esteban(Fuckboy de la decima), Isaac(Huele dedo), Michel(La opresora oprimida suprema, Alias pro santafe), Sulay(La personera oprimida), Arismendi(Tiene mas conocimientos un burro), Zharick(La sin criterio), Nicol barrera(¿Quien te conoce?), Matías(Pitufo pelietas), Camila(Maldita sea jimbo, el comunismo no sirve) y Nova(No la vas a poner)", "¿Te apetece coito? ugü"]

persona = ["Roman", "Eliana", "Pedro John", "Suero Jose", "Kendal", "Grecia", "Diego", "Sofia"]

# Quotes
def get_quote():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  json_data = json.loads(response.text)
  quote = json_data['insult']
  return(quote)

def putear():
  putear = random.choice(persona) + " " + random.choice(puteadas)
  return(putear)
  
@client.event
async def on_ready():
  print('Logged on')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hola'):
    await message.channel.send('Hello buddy')

  if message.content.startswith('$yes'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$si'):
    get = putear()
    await message.channel.send(get)



keep_alive()
client.run(my_secret)
