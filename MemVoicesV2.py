#meta developer: @bbbqmq_govnocoder

from .. import loader


@loader.tds  
class AnimeVoicesMod(loader.Module): 
 """Мемные войсы""" 
  
 strings = {"name": "MemVoices"} 
   
   
 async def eblancmd(self, message): 
  """Еблан""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/9", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def ebanniycmd(self, message): 
  """Ебанный рот""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/28", voice_note=True, reply_to=reply.id if reply else None) 
  return 
   
 async def poyasneniyecmd(self, message): 
  """Пояснение школьника""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/31", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def yrokicmd(self, message): 
  """Учи уроки""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/32", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def shytkicmd(self, message): 
  """Шутки про мать в 2020 году""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/33", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def povezlocmd(self, message): 
  """Повезло Повезло""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/66", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def petyxicmd(self, message): 
  """Эй петухи""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/67", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yacmd(self, message): 
  """Я два метра ростом""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/68", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def hilimsyacmd(self, message): 
  """Хилимся живем""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/69", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def shefcmd(self, message): 
  """Шеф за нами погоня""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/70", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def prishelcmd(self, message): 
  """Нахуй я сюда пришел?""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/72", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def pognalicmd(self, message): 
  """Ну че народ погнали нахуй""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/80", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def kydacmd(self, message): 
  """Куда хуяришь блядь""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/81", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def salocmd(self, message): 
  """Отдай сало""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/nexxlvoices/82", voice_note=True, reply_to=reply.id if reply else None) 
  return