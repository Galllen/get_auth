from telethon import TelegramClient
import os


api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("TG_PHONE")

session_path = "tech.session" 

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
