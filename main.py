from telethon import TelegramClient
import os

api_id = int(os.getenv("25046118"))
api_hash = os.getenv("860190cb259f0617c63384685da484b")
phone = os.getenv("+79895741790")

session_path = "tech.session"  # итоговый .session файл

client = TelegramClient(session_path, api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input("Введите код из Telegram: ")
        await client.sign_in(phone, code)
        print("ОК, сессия сохранена в", session_path)

with client:
    client.loop.run_until_complete(main())
