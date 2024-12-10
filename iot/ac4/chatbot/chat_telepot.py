import random
import subprocess
from time import sleep
import telepot
from decouple import config
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = config("TOKEN")
bot = telepot.Bot(TOKEN)

URL_BASE = "https://api.telegram.org/bot{}".format(TOKEN)
MENSAGENS = ["Olá", "Seja bem vindx", "É um prazer conversar com você"]
SAUDACAO = ["Oi", "Olá", "oi", "olá", "OI", "Ola", "ola"]
DESPEDIDA = ["Tchau", "Fui", "Até", "Ate", "Valeu", "tchau", "fui", "até", "ate", "valeu", "Encerrar"]


def build_keyboard(chat_id, usuario):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Uso do Processador', callback_data='proc')],
        [InlineKeyboardButton(text='Data e Hora Atual', callback_data='data')],
        [InlineKeyboardButton(text='Encerrar', callback_data='Encerrar')],
    ])
    bot.sendMessage(chat_id, f'\nEm que posso ajudar {usuario}?\n\nEscolha uma das opções abaixo:',
                    reply_markup=keyboard)


def on_chat_message(msg):
    chat_id = msg["chat"]["id"]
    comando = msg["text"]
    usuario = msg["from"]["first_name"]
    if comando == "proc":
        bot.sendMessage(chat_id, f"Uso do processador: {random.randint(1, 100)}%")
    elif comando == "data":
        bot.sendMessage(chat_id, subprocess.check_output('date +"%ch"', shell=True))
    elif comando in SAUDACAO:
        bot.sendMessage(chat_id, f"{random.choice(MENSAGENS)} {usuario}")
    elif comando in DESPEDIDA:
        bot.sendMessage(chat_id, f"Foi um prazer, até logo {usuario}")
    if not comando in DESPEDIDA:
        build_keyboard(chat_id, usuario)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    chat_id = msg["from"]["id"]
    usuario = msg["from"]["first_name"]
    texto = ""
    if query_data == "proc":
        texto = f"Uso do processador: {random.randint(1, 100)}%"
    elif query_data == "data":
        texto = subprocess.check_output('date +"%ch"', shell=True)
    elif query_data in DESPEDIDA:
        texto = f"Foi um prazer, até logo {usuario}"
    bot.answerCallbackQuery(query_id, text=texto)
    bot.sendMessage(chat_id, texto)
    if not query_data in DESPEDIDA:
        build_keyboard(chat_id, usuario)


MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

while True:
    sleep(10)
