from bot.openai.open_ai_bot import OpenAIBot
import lib.itchat as itchat
import schedule
import time
import threading
def send_Evening_message():

    try:
        gptbot = OpenAIBot()
        model="gpt-4-1106-preview"
        resText = gptbot.ask(
            '请你扮演一名著名、幽默的情感大师，且你对全球各国的寓言故事了如指掌。请你用开朗，幽默、梦幻对世界充满好奇的语气，写一段350字左右，有趣、梦幻且充满寓意的话向元宇宙开发者协会的成员们(人员包括美术、程序、音乐、策划、兴趣爱好者等等)报一个晚安。要求：1、不需要讲你是谁和寓言来自哪，2、必须要有寓意且积极向上、完整，3、字数控制在350字以内。4、尽量扮演一个真正的人用口语化的语言徐徐道来。5、禁止用所以这个词。6、出现的动物或植物必须是不常出现的动植物。不可以是狐狸，小猫，狗等常看见的生灵',
            model)

        #friend = itchat.search_friends(name='小灵')[0]  # 替换成你要发送消息的好友昵称
        #friend.send(resText)

        itchat.update_chatroom(True)
        # 获取目标群组
        chatrooms = itchat.search_chatrooms(name='元宇宙开发者协会')
       # print(chatrooms)

        # 如果找到了群组
        if chatrooms:
            if len(chatrooms) == 1:
                # 只找到一个匹配的群组
                chatroom = chatrooms[0]
                receiver = chatroom['UserName']
                print("找到唯一的匹配群组，其 UserName 是：", receiver)
            else:
                # 找到多个匹配的群组
                print("找到多个匹配的群组，请选择要操作的群组：")
                for index, room in enumerate(chatrooms):
                    print(f"{index + 1}. {room['NickName']}")
                receiver = chatrooms[0]['UserName']
            # 发送消息给群组
            itchat.send(resText, toUserName=receiver)
    # 定义定时任务
    except Exception as e:
        print(e)

def send_Morning_message():
    try:
        gptbot = OpenAIBot()
        model="gpt-4-1106-preview"
        resText = gptbot.ask(
            '请你扮演一名热情，开朗、幽默在世界各地旅游的小精灵，你对全球各国的发生的事情都了如指掌。请你用梦幻、充满寓意对世界透露着好奇的语气，写一段80字左右的话向元宇宙开发者协会的成员们报个早安迎接新的一天的到来。要求：1、不需要讲你是谁或寓言来自哪，2、必须要有韵味，3、字数控制在80字左右。4、尽量扮演一个真正的人用口语化的语言徐徐道来。5、禁止出现所以这个词，6、每次早安，绝大部分为中文然后在不影响语义连贯性的情况下夹杂一，两段英文',
            model)

        #friend = itchat.search_friends(name='小灵')[0]  # 替换成你要发送消息的好友昵称
        #friend.send(resText)

        itchat.update_chatroom(True)
        # 获取目标群组
        chatrooms = itchat.search_chatrooms(name='元宇宙开发者协会')
       # print(chatrooms)

        # 如果找到了群组
        if chatrooms:
            if len(chatrooms) == 1:
                # 只找到一个匹配的群组
                chatroom = chatrooms[0]
                receiver = chatroom['UserName']
                itchat.send(resText, toUserName=receiver)
                print("找到唯一的匹配群组，其 UserName 是：", receiver)
            else:
                # 找到多个匹配的群组
                print("找到多个匹配的群组，请选择要操作的群组：")
                for index, room in enumerate(chatrooms):
                    print(f"{index + 1}. {room['NickName']}")
                    receiver = chatrooms[index]['UserName']
            # 发送消息给群组
                    itchat.send(resText, toUserName=receiver)
        # 定义定时任务
    except Exception as e:
        print(e)

def scheduled_job():
    schedule.every().day.at("15:00").do(send_Evening_message)  # 在每天的23点发送消息
    schedule.every().day.at("00:00").do(send_Morning_message)  # 在每天的8点发送消息
    print('启动监控')
    while True:
        schedule.run_pending()
        time.sleep(1)

def init():
    pass

def strategyV1():
    #
    init()
    # 创建并启动定时任务的线程
    schedule_thread = threading.Thread(target=scheduled_job)
    schedule_thread.start()