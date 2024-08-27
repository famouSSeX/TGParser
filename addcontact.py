from telethon import TelegramClient, sync, functions, types


# Замените на свои данные
api_id = '29363209'
api_hash = '4882b60730443fc2faf0cf3930daf5cf'

# Создаем экземпляр клиента Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start()



async def addcontact(usernames):
    for username in usernames:
        try:
            # Получаем пользователя по username
            user = await client.get_entity(username)
            
            # Получаем имя, фамилию и номер телефона пользователя
            first_name = user.first_name or ""
            last_name = user.last_name or ""
            phone = user.phone or ""
            
            # Добавляем пользователя в контакты
            await client(functions.contacts.AddContactRequest(
                id=user.id,
                first_name=first_name,
                last_name=last_name,
                phone=phone
            ))
            
            print(f"Пользователь {first_name} {last_name} добавлен в контакты.")
        except Exception as e:
            print(f"Не удалось добавить пользователя {username}: {e}")

async def main():
    async with client:
        # usernames = ['vingern', 'dark1nir', 'desynte']
        file = 'output.txt'
        f = open(file)
        usernames = [i.split('\n')[0] for i in f]
        await addcontact(usernames)

if __name__ == "__main__":
    client.start()
    client.loop.run_until_complete(main())

