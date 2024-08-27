from telethon import TelegramClient, sync

file = open('output.txt','w')

api_id = '29363209'
api_hash = '4882b60730443fc2faf0cf3930daf5cf'


client = TelegramClient('session_name', api_id, api_hash)

async def get_chat_members():
    try:
        chat = await client.get_entity('matreshka_consult')
        members = await client.get_participants(chat)
        return members
    except Exception as e:
        print(f"Error: {e}")
        return None

with client:
    members = client.loop.run_until_complete(get_chat_members())
    if members:
        for member in members:
             print(type(member.username))
             if member.username != None:
                file.write(f'{member.username}\n')
