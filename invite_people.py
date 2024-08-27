from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import time

api_id = '29363209'
api_hash = '4882b60730443fc2faf0cf3930daf5cf'

client = TelegramClient('session_name', api_id, api_hash)

file = 'output.txt'
f = open(file)
peoplelist = [i.split('\n')[0] for i in f]

def remove_used_fragment(file_path, fragment_to_remove):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace(f'{fragment_to_remove}\n', '')
    
    try:
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print(f"The fragment '{fragment_to_remove}' has been removed from the file.")
    
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

async def invite_users_by_username(channel_id, usernames):
    try:
        channel = await client.get_entity(channel_id)
        
        for username in usernames:
            time.sleep(4)
            try:
                user = await client.get_entity(f'@{username}')
                await client(InviteToChannelRequest(
                    channel=channel,
                    users=[user]
                ))
                print(f"Invited user @{username} to the channel/megagroup.")
                remove_used_fragment(file, username)
            except Exception as e:
                print(f"Error inviting user @{username}: {e}")
    except Exception as e:
        print(f"Error: {e}")




async def main():
    async with client:
        group_id = 'u_express_obmen'
        user_ids = peoplelist

        await invite_users_by_username(group_id, user_ids)

if __name__ == "__main__":
    client.start()
    client.loop.run_until_complete(main())
