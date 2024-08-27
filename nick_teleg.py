from telethon import TelegramClient, sync

# Укажите ваши API ID и API Hash, полученные от Telegram
api_id = '29363209'
api_hash = '4882b60730443fc2faf0cf3930daf5cf'

# Создайте экземпляр клиента Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def get_username_by_full_id(full_user_id):
    try:
        # Получите сущность пользователя по его полному ID
        user = await client.get_entity(full_user_id)
        
        # Извлеките username пользователя
        username = user.username
        
        if username:
            return f'@{username}'
        else:
            return 'No username available'
    except Exception as e:
        print(f"Error: {e}")
        return 'Error getting username'

async def main():
    async with client:
        # Замените 'FULL_USER_ID' на полный ID пользователя, для которого вы хотите получить username
        full_user_id = '2133970622'
        
        username = await get_username_by_full_id(full_user_id)
        print(f"Username: {username}")

if __name__ == "__main__":
    client.start()
    client.loop.run_until_complete(main())