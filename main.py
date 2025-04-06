import os
try:
    from telethon.sync import TelegramClient
    import pandas as pd
    import time
    from tqdm import tqdm
except ImportError:
    input(f'Нажмите Enter для установки библиотек.')
    os.system('pip install telethon')
    os.system('pip install pandas')
    os.system('pip install xlsxwriter')
    os.system('pip install openpyxl')
    os.system('pip install tqdm')

api_id = 00000
api_hash = '...'
phone = '+7...'

client = TelegramClient('aboba', api_id, api_hash)
client.start(phone)

directory = input(f'Введите путь к файлу: ')
message = input(f'А шо писать?: ')
duration = 3.5

def send_message(users: list):
    for user in tqdm(users, desc='Пишем людям..', ncols=70):
        try:
            client.send_message(user, message)
            # если вы хотите прикреплять фото, или файлы к сообщению.
            #client.send_file(user, open('...', 'rb'), caption=message)
            time.sleep(duration)
        except Exception as e:
            print(f'Ошибка: {e}')
    print(f'Готово! Написали.')
    return 

if 'xlsx' in directory[:-4]:
    df = pd.read_excel(directory)
    ids = df['id'].dropna().to_list()
    send_message(ids)
    client.disconnect()
else:
    file = open(directory, 'r').readlines()
    send_message(file)
    client.disconnect()
