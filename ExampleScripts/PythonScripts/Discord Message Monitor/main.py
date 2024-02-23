import discord
from discord import app_commands
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.ext import tasks
import datetime
import time
import requests 
import pprint
import random
import asyncio
given_token="REDACTED"
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
BASE = "https://discord.com/api/v9/"
TOKEN = given_token
def timeout_user(*, user_id: int, guild_id: int, until: int):
    endpoint = f'guilds/{guild_id}/members/{user_id}'
    headers = {"Authorization": f"Bot {TOKEN}"}
    url = BASE + endpoint
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(hours=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    session = requests.patch(url, json=json, headers=headers)
    if session.status_code in range(200, 299):
        return session.json()
    else: 
        return print("Did not find any\n", session.status_code)

@tasks.loop(time=datetime.time(hour=0, minute=30, second=0, microsecond=0))
async def add_credits():
  if True:
    f = open("message_tokens.txt", "r")
    entries = f.readlines()
    for i in range(len(entries)):
      credits = int(entries[i][19:23])
      credits = credits + 1
      entries[i] = entries[i][0:18] + ":" + "%04d" % credits
    s = open("message_tokens.txt", "w")
    s.writelines(entries)
    s.close()
# asyncio.run(add_credits.start())
def add_strings(nested_list, string1, string2):
  new_nested_list = nested_list
  new_nested_list.append([string1, string2])
  return new_nested_list

@client.event
async def on_message(message):
  DM = False
  try: 
    guild0 = message.guild.id
  except:
    DM = True
  if message.author == client.user:
    return
  f = open("message_tokens.txt", "r")
  data_tokens = f.readlines()
  for i in range(len(data_tokens)):
    if str(message.author.id) in data_tokens[i]:
      credits = data_tokens[i][19:23]
      user = client.get_user(int(message.author.id))
      try:
        if DM == False:
          response = await user.send(str(message.author) + ", you now have " + str(int(credits) - 1) + " messaging tokens.")
        else:
          response = await user.send(str(message.author) + " No DM response. If you are messaging to be remove timeout then it should be successful.")
        guild = client.get_guild(REDACTED)
        member = guild.get_member(message.author.id)
        user_id = member.id
        guild_id = guild.id
        try:
          timeout_r = timeout_user(user_id=user_id,guild_id=guild_id,until=0)
        except:
          print("exception")
        pprint.pprint(timeout_r)
      except:
        print("Message Monitor blocked by: " + str(message.author))
        guild = message.guild
        member = guild.get_member(message.author.id)
        user_id = member.id
        guild_id = guild.id
        try:
          timeout_r = timeout_user(user_id=user_id,guild_id=guild_id,until=99)
        except:
          print("fail")
        pprint.pprint(timeout_r)
        await message.channel.send("**You must unblock the message bot in order to chat here.**")
      if int(credits) < 1:
        await message.delete()
        # time.sleep(25)
        # await response.delete()
        return
      if DM == False:
        int_credits = int(credits) - 1
      a = open("message_tokens.txt", "r")
      edit_list = a.readlines()
      for n in range(len(edit_list)):
        if str(message.author.id) in edit_list[n]:
          edit_list[n] = str(message.author.id) + ":" + str("%04d" % (int_credits,))
      str_edit_list = ""
      for x in range(len(edit_list)):
        edit_list[x] = edit_list[x].replace("\n", "")
        str_edit_list = str_edit_list + str(edit_list[x]) + "\n"
      print(edit_list)
      print(str_edit_list)
      s = open("message_tokens.txt", "w")
      s.write(str_edit_list)
      s.close()
      # time.sleep(25)
      # await response.delete()
  print(message.author.display_name + ":" + message.content)


client.run(given_token)

