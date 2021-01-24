from telethon import TelegramClient, events, sync
from selenium import webdriver
import gmail_data_use as tgApi_get
import check as check_dt
import time

api_id = 
api_hash = ''
bot_token = ''
client = TelegramClient('anon', api_id, api_hash)


with TelegramClient('anon', api_id, api_hash) as client:
    # GmailFarmerBot
    client.send_message('me', '➕ Зарегистрировать новый аккаунт')

@client.on(events.NewMessage(chats='me'))
async def my_event_handler(event):
    test = str(event.raw_text)
     #print(event.raw_text)
    if test.find("Зарегистрируйте") == -1:
        print("ney!")

    else:
        browser = webdriver.Chrome("D:/chrome/chromedriver.exe")
        browser.get("https://accounts.google.com/signup?hl=en")
        time.sleep(2)
        email_get, name_get, surname_get, pass_get = check_dt.editing(test)
        tgApi_get.data_use(email_get, name_get, surname_get, pass_get, browser)
        browser.close()


client.start()
client.run_until_disconnected()

