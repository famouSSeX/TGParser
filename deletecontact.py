from telethon import TelegramClient, sync, functions, types

api_id = '29363209'
api_hash = '4882b60730443fc2faf0cf3930daf5cf'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Получаем список всех контактов
    contacts = await client(functions.contacts.GetContactsRequest(hash=0))

    # Удаляем все контакты
    await client(functions.contacts.DeleteContactsRequest(
        id=[contact.id for contact in contacts.users]
    ))

    print("Все контакты удалены.")

    # Завершаем сессию
    await client.disconnect()

with client:
    client.loop.run_until_complete(main())