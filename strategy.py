from bot.openai.open_ai_bot import OpenAIBot
import lib.itchat as itchat
import schedule
import time
import threading
def send_message():
    global bot

    gptbot = OpenAIBot()
    resText = gptbot.ask('请你用开朗，热情对世界充满好奇的语气写一段话向元宇宙开发者协会的成员们报一个晚安')

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

def scheduled_job():
    schedule.every().day.at("23:00").do(send_message)  # 在每天的23点发送消息
    print('启动监控')
    while True:
        schedule.run_pending()
        time.sleep(1)

def init():
    global bot
    bot=OpenAIBot()

def strategyV1():
    #
    init()
    # 创建并启动定时任务的线程
    schedule_thread = threading.Thread(target=scheduled_job)
    schedule_thread.start()