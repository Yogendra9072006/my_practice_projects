# This example requires the 'message_content' intent.
import os
import discord
from openai import OpenAI



token = os.getenv("DISCORD_TOKEN")

openai = OpenAI() 
"""IMPORTANT NOTE: If you are taking 'client' as variable for discord functions, do not take client also for openai ,
 It can create conflict and show ERROR Instead use openai word. """



class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
              if self.user in message.mentions:
                response = openai.completions.create(
                  model="gpt-3.5-turbo-instruct-0914",
                  prompt = message.content,
                  temperature=1,
                  max_tokens=256,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0
                )
                channel = message.channel
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
