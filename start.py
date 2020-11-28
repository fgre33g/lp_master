import asyncio
import json
import time
from threading import Thread

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


run = False
restart = 0
prov = 0
sleep = True


class MyThread_1(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(friends_lp.add_friends_conversations(self.delay, self.peer_id, self.command))
        except:
            print("")

class MyThread_2(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(online.online(self.delay, self.peer_id, self.command))
        except:
            print("")


class MyThread_3(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(info_lp.read(self.delay, self.peer_id, self.command))
        except:
            print("")


class MyThread_4(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(friends_lp.auto_add_friends(self.delay, self.peer_id, self.command))
        except:
            print("")


class MyThread_5(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(profile.autodr(self.delay, self.peer_id, self.command))
        except:
            print("")


class MyThread_6(Thread):
    """
    A threading example
    """

    def __init__(self, delay, peer_id, command):
        """Инициализация потока"""
        Thread.__init__(self)
        self.delay = delay
        self.peer_id = peer_id
        self.command = command

    def run(self):
        try:
            asyncio.run(profile.autostatus(self.delay, self.peer_id, self.command))
        except:
            print("")


class MyThread_sleep(Thread):
    """
    A threading example
    """

    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        while sleep == True:
            print("Бот запущен")
            time.sleep(5)


class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        global run

        def start_main():
            global run
            global prov
            global sleep
            run = True
            sleep = False
            prov = 1

        start_main()

my_thread = MyThread()
my_thread.start()
thread_sleep = MyThread_sleep()
thread_sleep.start()

while True:
    if prov == 1:
        with open("main/database/database_token.json", "r", encoding="utf-8") as file:
            data = json.loads(file.read())
        token = data['token']
        vk = vk_api.VkApi(app_id=6146827, token=token)
        longpoll = VkLongPoll(vk, wait=0)
        from main.additions import bomb, friends_lp, online, ping_lp, profile, info_lp, sms
        from main.templates import press_f_1, press_f_2, anim_templates, conv, xz, templates_lp, gb

        try:
            for event in longpoll.listen():
                # Если пришло новое сообщение
                if event.type == VkEventType.MESSAGE_NEW:

                    if event.from_me:
                        command = event.text
                        delay = 0
                        peer_id = event.peer_id
                        if run == False:
                            print("лп не запущен")
                        else:
                            try:
                                asyncio.run(info_lp.info_msg(delay, peer_id, command))
                                asyncio.run(bomb.bomb(delay, peer_id, command))
                                my_thread_1 = MyThread_1(delay, peer_id, command)
                                my_thread_1.start()
                                my_thread_2 = MyThread_2(delay, peer_id, command)
                                my_thread_2.start()
                                my_thread_3 = MyThread_3(delay, peer_id, command)
                                my_thread_3.start()
                                my_thread_4 = MyThread_4(delay, peer_id, command)
                                my_thread_4.start()
                                my_thread_5 = MyThread_5(delay, peer_id, command)
                                my_thread_5.start()
                                my_thread_6 = MyThread_6(delay, peer_id, command)
                                my_thread_6.start()
                                asyncio.run(press_f_1.pressf(delay, peer_id, command))
                                asyncio.run(press_f_2.pressf(delay, peer_id, command))
                                asyncio.run(gb.gb(delay, peer_id, command))
                                asyncio.run(xz.xz(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim_info(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim1(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim2(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim3(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim4(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim5(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim6(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim7(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim8(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim9(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim10(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim11(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim12(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim13(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim14(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim15(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim16(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim17(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim18(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim19(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim20(delay, peer_id, command))
                                asyncio.run(anim_templates.BFanim21(delay, peer_id, command))
                                asyncio.run(templates_lp.create_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.templates(delay, peer_id, command))
                                asyncio.run(templates_lp.one_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.delete_templates(delay, peer_id, command))
                                asyncio.run(templates_lp.create_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplate(delay, peer_id, command))
                                asyncio.run(templates_lp.red_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dele_dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplates(delay, peer_id, command))
                                asyncio.run(templates_lp.dtemplates_temp(delay, peer_id, command))
                                asyncio.run(templates_lp.delete_dtemplates(delay, peer_id, command))
                                asyncio.run(ping_lp.ping_info(delay, peer_id, command))
                                asyncio.run(conv.fonts(delay, peer_id, command))
                                asyncio.run(conv.font(delay, peer_id, command))
                                asyncio.run(info_lp.info(delay, peer_id, command))
                                asyncio.run(info_lp.execute(delay, peer_id, command))
                                asyncio.run(conv.convert(delay, peer_id, command))
                                asyncio.run(info_lp.info_user(delay, peer_id, command))
                                asyncio.run(info_lp.bind(delay, peer_id, command))
                                asyncio.run(info_lp.idm(delay, peer_id, command))
                                asyncio.run(info_lp.chats(delay, peer_id, command))
                                asyncio.run(info_lp.chats_name(delay, peer_id, command))
                                asyncio.run(info_lp.chats_del(delay, peer_id, command))
                                asyncio.run(info_lp.read_on(delay, peer_id, command))
                                asyncio.run(info_lp.read_off(delay, peer_id, command))
                                asyncio.run(sms.dd_sms(delay, peer_id, command))
                                asyncio.run(sms.del_sms(delay, peer_id, command))
                                asyncio.run(sms.del_sms_from_user(delay, peer_id, command))
                                asyncio.run(sms.add_sms(delay, peer_id, command))
                                asyncio.run(sms.add_vsms(delay, peer_id, command))
                                asyncio.run(sms.add_spam(delay, peer_id, command))
                                asyncio.run(sms.ban_user(delay, peer_id, command))
                                asyncio.run(sms.add_user(delay, peer_id, command))
                                asyncio.run(friends_lp.add_friends(delay, peer_id, command))
                                asyncio.run(friends_lp.del_friends(delay, peer_id, command))
                                asyncio.run(friends_lp.auto_add_friends_on(delay, command))
                                asyncio.run(friends_lp.auto_add_friends_off(delay, peer_id, command))
                                asyncio.run(online.offline(0, event.peer_id, command))
                                asyncio.run(online.online_on(0, command))
                                asyncio.run(profile.dr(0, event.peer_id, command))
                                asyncio.run(profile.autodr_on(0, command))
                                asyncio.run(profile.autodr_off(0, event.peer_id, command))
                                asyncio.run(profile.status(delay, peer_id, command))
                                asyncio.run(profile.autostatus_on(0, command))
                                asyncio.run(profile.autostatus_off(0, event.peer_id, command))
                                asyncio.run(info_lp.score(delay, peer_id, command))
                            except:
                                print("Произошла ошибка")
                                # time.sleep(4)
                                continue
        except:
            print("Скрипт перезапущен")
            pass