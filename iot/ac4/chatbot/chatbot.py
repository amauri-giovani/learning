import json
import random
from decouple import config
import subprocess
from requests import get, post

TOKEN = config("TOKEN")
URL_BASE = f"https://api.telegram.org/bot{TOKEN}"
URL_UPDATES = f"{URL_BASE}/getUpdates"
URL_SEND_MESSAGE = f'{URL_BASE}/sendMessage?'
mensagens = ["Olá", "Seja bem vindx", "É um prazer conversar com você "]


class Bot:
    def getme(self):
        self.resp_getme = get(f'{URL_BASE}/getMe').json()
        self.bot_name = self.resp_getme['result']['first_name']
        return self.bot_name

    def get_updates(self, offset=0, timeout=0):
        self.last_update_id = 0
        self.resp = get(f'{URL_UPDATES}?offset={offset}&timeout={timeout}').json()
        # if "callback_query" in self.resp:
        #     print("AQUI")
        print(self.resp)
        self.result = len(self.resp['result'])
        if self.result >= 1:
            self.last_index = self.resp['result'][self.result - 1]
            self.last_update_id = self.last_index['update_id']
            print(self.last_index)
            if "callback_query" in self.last_index:
                print("AQUI")
                self.last_index = self.last_index["callback_query"]
                self.callback_query_data = self.last_index['data']
            self.chat = self.last_index['message']['chat']
            self.chat_id = self.chat['id']
            self.first_name = self.chat['first_name']
            self.text = self.last_index['message']['text']

            if 'username' in self.chat:
                self.username = self.chat['username']
            else:
                self.username = self.first_name
            self.handle_updates()
        return self.last_update_id

    def send_message(self, text, reply_markup=None):
        self.message = f"{URL_SEND_MESSAGE}chat_id={self.chat_id}&text={text}"
        if reply_markup:
            self.message += f"&reply_markup={reply_markup}"
        return post(self.message)

    def handle_updates(self):
        if self.text in ["proc", "Proc", "processador", "Processador"]:
            self.send_message(f"Uso do processador: {random.randint(1, 100)}%")
        elif self.text in ["data", "Data"]:
            self.send_message(subprocess.check_output("date", shell=True))
        elif self.text in ["Oi", "Olá", "oi", "olá", "OI", "Ola", "ola"]:
            self.send_message(f"{random.choice(mensagens)} {self.first_name}")
        elif self.text in ["Tchau", "Fui", "Até", "Valeu", "tchau", "fui", "até", "valeu"]:
            self.send_message("Foi um prazer, até logo!")
            exit(0)
        else:
            self.send_message(f"Em que posso ajudar {self.first_name}?\n"
                              f"Escolha uma das opções com teclado", self.options_keyboard())

    def options_keyboard(self):
        reply_markup = {"inline_keyboard":
            [
                [{"text": "Consumo do Processador", "callback_data": "proc"}],
                [{"text": "Data e Hora Atual", "callback_data": "data"}],
                # [{"text": "Adicionar um workshop", "callback_data": "3"}]
            ]
        }
        return json.dumps(reply_markup)


def main():
    last_id = 0
    while True:
        last_id = bot.get_updates(last_id + 1, 30)


if __name__ == '__main__':
    bot = Bot()
    # bot.get_updates()
    print("Aguardando mensagens...")
    main()
