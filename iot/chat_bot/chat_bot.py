import random
from time import sleep

import telepot
from decouple import config


TOKEN = config("TOKEN")
bot = telepot.Bot(TOKEN)


def bot_getme():
    return bot.getMe()


mensagens = ["Vamos nessa!", "I'm botman", "acaba covid"]


def opcoes(msg):
    chat_id = msg["chat"]["id"]
    comando = msg["text"]
    print(str(random.choice(mensagens)))

    if comando == "temp":
        bot.sendMessage(chat_id, random.randint(1, 100))
    elif comando == "frase":
        bot.sendMessage(chat_id, random.choice(mensagens))
    elif comando == "tchau":
        bot.sendMessage(chat_id, "Fui")
        exit(0)


bot.message_loop(opcoes)


while True:
    sleep(10)
