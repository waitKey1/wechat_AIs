from bot.openai.open_ai_bot import OpenAIBot

gptbot = OpenAIBot()
model="gpt-4-1106-preview"
resText = gptbot.ask(
    '请你扮演一名著名、幽默的情感大师，且你对全球各国的寓言故事了如指掌。请你用开朗，幽默、梦幻对世界充满好奇的语气，写一段350字左右，有趣、梦幻且充满寓意的话向元宇宙开发者协会的成员们(人员包括美术、程序、音乐、策划、兴趣爱好者等等)报一个晚安。要求：1、不需要讲你是谁和寓言来自哪，2、必须要有寓意且积极向上、完整，3、字数控制在350字以内。4、尽量扮演一个真正的人用口语化的语言徐徐道来。5、禁止用所以这个词。6、出现的动物或植物必须是不常出现的动植物。不可以是狐狸，小猫，狗等常看见的生灵',
    model)

print(resText)
resText = gptbot.ask('请你扮演一名热情，开朗、幽默在世界各地旅游的小精灵，你对全球各国的发生的事情都了如指掌。请你用梦幻、充满寓意对世界透露着好奇的语气，写一段80字左右的话向元宇宙开发者协会的成员们报个早安迎接新的一天的到来。要求：1、不需要讲你是谁或寓言来自哪，2、必须要有韵味，3、字数控制在80字左右。4、尽量扮演一个真正的人用口语化的语言徐徐道来。5、禁止出现所以这个词，6、每次早安，绝大部分为中文然后在不影响语义连贯性的情况下夹杂一，两段英文',model)

print(resText)