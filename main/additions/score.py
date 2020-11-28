import asyncio
import json
import re

import vk_api
from vk_api.longpoll import VkLongPoll

from main.additions import friends_lp, online, profile
from tools.messages import messages


finished = True


async def info(delay, peer_id, command):
    global onl
    await asyncio.sleep(delay)
    if "!н счетскик" in command or "!н счет" in command or "!н сч" in command or "!н счёт" in command:
        if peer_id > 2000000000:
            history = vk.method('messages.getConversationsById', {'peer_ids': peer_id})
            name = history['items'][0]['chat_settings']['title']
        else:
            user = vk.method('users.get', {'user_ids': peer_id, 'fields': 'friend_status'})
            fname = user[0]['first_name']
            lname = user[0]['last_name']
            name = str(fname)+" "+str(lname)

        historys = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        count = historys['count']

        with open("main/database/database_lp_temp.json", "r", encoding="utf-8") as file:
               data = json.loads(file.read())
        data_temp = data['templates']
        itr = 0
        for temp in data_temp:
            itr += 1

        with open("main/database/database_lp_dtemp.json", "r", encoding="utf-8") as file:
               data = json.loads(file.read())
        data_temp = data['templates']

        ditr = 0
        for temp in data_temp:
            ditr += 1

        onlines = online.online_info()

        if onlines:
            onl = "❌"
        elif not onlines:
            onl = "✅"

        read_info = finished

        if read_info:
            read = "❌"
        elif not read_info:
            read = "✅"

        autofr = friends_lp.auto_add_friends_info()

        autodrs = profile.info_autodr()
        if not autodrs:
            drs = "❌"
        elif onlines:
            drs = "✅"

        autostatus = profile.info_autostatus()
        if autostatus:
            stats = "❌"
        elif not autostatus:
            stats = "✅"

        msg_1 = f"""
        Кол-во сообщений: {count}
        """.replace('    ', '')

        messages.write_msg(peer_id, msg_1)

# async def info_user(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н кто ты" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['conversation_message_id']
        # msg_text = history['items'][0]['text']
        # msg_text = msg_text.replace('ты', '')

        # regexp = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        # _args = re.findall(regexp, msg_text)
        # args = []
        # payload = ""

        # for arg in _args:
            # if arg[1] != '':
                # args.append(arg[1])
            # if arg[2] != '':
                # payload = arg[2][1:]

        # if len(args) == 1:
            # commands = args[0].lower()
            # argss = None

            # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
            # user_id = history['items'][0]['reply_message']['from_id']
            # print(user_id)
            # user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status, city, sex'})
            # name = user[0]['first_name']
            # friend = user[0]['friend_status']
            # sex = user[0]['sex']
            # friends = int(friend)
            # sexs = int(sex)
            # user_ids = "id"+str(user_id)

        # else:
            # commands = args[0].lower()
            # argss = args[1:]

            # user_id = ''.join(argss).replace('https://vk.com/', '')
            # print(user_id)
            # user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status, city, sex'})
            # user_id = user[0]['id']
            # name = user[0]['first_name']
            # friend = user[0]['friend_status']
            # sex = user[0]['sex']
            # friends = int(friend)
            # sexs = int(sex)
            # user_ids = "id"+str(user_id)

        # friend_status = 'нет' if friends == 0 else 'заявка отправлена' if friends == 1 else 'имеется входящая заявка от пользователя' if friends == 2 else 'да'
        # sex_status = 'мужской' if sexs == 2 else 'женский'

        # msg_1 = f"""
        # Информация о пользователе:
        # Имя: {name}
        # ID: @{user_ids}({user_id})
        # Пол: {sex_status}
        # Есть в друзьях: {friend_status}
        # """.replace('    ', '')

        # messages.write_msg(peer_id, msg_1)

# async def info_msg(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н дебаг" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['reply_message']['id']
        # info = vk.method('messages.getById', {'message_ids': msg_id})
        # messages.write_msg(peer_id, f"{info}")

# async def bind(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н связать" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # user_id = history['items'][0]['from_id']
        # user = vk.method('users.get', {'user_ids': user_id, 'fields': 'friend_status, city, sex'})
        # sex = user[0]['sex']
        # sex_status = 'дурак' if sex == 2 else 'дура'

        # msg_1 = f"""
        # Ты шо {sex_status}?
        # Беседа не связана, это тебе не дежурный ирис, связавать нечего
        # """.replace('    ', '')

        # messages.write_msg(peer_id, msg_1)
    # elif "!гей связать" in command:

        # msg_1 = f"""
        # ✅ Гей клуб связан с беседой!
        # """.replace('    ', '')

        # messages.write_msg(peer_id, msg_1)

# async def idm(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н идм" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['id']

        # msg_1 = f"""
        # +api MAVKantispam https://lordral.ru/callback/
        # """.replace('    ', '')

        # messages.write_msg(-174105461, msg_1)

        # messages.edit_msg(peer_id, "Переключён на платный IDM", msg_id)
    # elif "!н мой идм" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['id']

        # msg_1 = f"""
        # +api mavkantispam https://NikitolIrisDev.pythonanywhere.com/callback
        # """.replace('    ', '')

        # messages.write_msg(-174105461, msg_1)

        # messages.edit_msg(peer_id, "Переключён на мой IDM", msg_id)
    # elif "!н мди" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['id']

        # msg_1 = f"""
        # +api mavkantispam https://belikanov.online/iris/callback.php
        # """.replace('    ', '')

        # messages.write_msg(-174105461, msg_1)

        # messages.edit_msg(peer_id, "Переключён на MDI", msg_id)


# async def chats(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н +чат" in command:
        # with open("main/database/database_lp.json", "r", encoding="utf-8") as file:
               # data = json.loads(file.read())
        # data_chats = data['chats']
        # print(data_chats)
        # data_chats.append(str(peer_id))
        # print(data_chats)
        # data = {"chats": data_chats}
        # print(data)
        # with open("main/database/database_lp.json", "w", encoding="utf-8") as file:
            # file.write(json.dumps(data, ensure_ascii=False, indent=4))
        # messages.write_msg(peer_id, "Чат привязан!")

# async def read_on(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # global finished
    # if command == "!н стч":
        # finished = False

# async def read(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # global finished
    # if command == "!н стч":
        # messages.write_msg(peer_id, "✅ Авточиталка сообщений в специальных чатах включена!")
        # with open("main/database/database_lp.json", "r", encoding="utf-8") as file:
                   # data = json.loads(file.read())
        # data_chats = data['chats']
        # while finished == False:
            # for i in range(len(data_chats)):
                # print(vk.method("messages.markAsRead", {'peer_id': data_chats[i]}))

# async def read_off(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # global finished
    # if command == "!н спч":
        # messages.write_msg(peer_id, "✅ Авточиталка сообщений в специальных чатах выключена!")
        # finished = True


# async def chats_del(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н -чат" in command:
        # with open("main/database/database_lp.json", "r", encoding="utf-8") as file:
               # data = json.loads(file.read())
        # data_chats = data['chats']
        # print(data_chats)
        # data_chats.remove(str(peer_id))
        # print(data_chats)
        # data = {"chats": data_chats}
        # print(data)
        # with open("main/database/database_lp.json", "w", encoding="utf-8") as file:
            # file.write(json.dumps(data, ensure_ascii=False, indent=4))
        # messages.write_msg(peer_id, "Чат отвязан!")

# async def chats_name(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н чз" in command:
        # chat_id = peer_id - 2000000000
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['conversation_message_id']
        # msg_text = history['items'][0]['text']
        # chat = vk.method('messages.getChat', {'chat_id': chat_id})
        # chat_name = chat['title']
        # regexp = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        # _args = re.findall(regexp, msg_text)
        # args = []
        # payload = ""

        # for arg in _args:
            # if arg[1] != '':
                # args.append(arg[1])
            # if arg[2] != '':
                # payload = arg[2][1:]

        # if len(args) == 1:
            # commands = args[0].lower()
            # argss = None

            # messages.write_msg(peer_id, "Укажите название беседы!")
        # else:
            # commands = args[0].lower()
            # argss = args[1:]

            # name = ''.join(argss)

            # i = 1
            # while i >= 0:
                # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
                # msg_text = history['items'][0]['text']
                # chat = vk.method('messages.getChat', {'chat_id': chat_id})
                # chat_name = chat['title']
                # if chat_name == name:
                    # print('ok')
                # if "!н счз" in msg_text:
                    # i = -1
                    # print("Автоизменение названия беседы отключенно")
                # if chat_name != name:
                    # vk.method('messages.editChat', {'chat_id': chat_id, 'title': name})
                    # print("Название изменено")

# async def execute(delay, peer_id, command):
    # await asyncio.sleep(delay)
    # if "!н апи" in command:
        # history = vk.method('messages.getHistory', {'count': 1, 'peer_id': peer_id, 'rev': 0})
        # msg_id = history['items'][0]['conversation_message_id']
        # msg_text = history['items'][0]['text']
        # regexp = r"(^[\S]+)|([\S]+)|(\n[\s\S \n]+)"
        # _args = re.findall(regexp, msg_text)
        # args = []
        # payload = ""

        # for arg in _args:
            # if arg[1] != '':
                # args.append(arg[1])
            # if arg[2] != '':
                # payload = arg[2][1:]

        # if len(args) == 1:
            # commands = args[0].lower()
            # argss = None

            # print(payload)
            # test = str(eval(payload))
            # messages.write_msg(peer_id, test)
        # else:
            # commands = args[0].lower()
            # argss = args[1:]

            # print(payload)
            # test = str(eval(payload))
            # messages.write_msg(peer_id, "Ответ вк: " + str(test))


        # '''
        # count = int(count)
        # msg_1 = ''.join(payload)
        # '''

with open("main/database/database_token.json", "r", encoding="utf-8") as file:
   data = json.loads(file.read())
token = data['token']

# Авторизуемся как сообщество
vk = vk_api.VkApi(app_id=6146827, token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, wait = 0)
