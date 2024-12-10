"""
Recebendo mensagens
Para implementar o receptor, defina a conexão e o canal da mesma forma que foi feito
no produtor de mensagens.
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='aluno', exchange_type='fanout')
queue = channel.queue_declare(queue='contabil').method.queue
channel.queue_bind(exchange='aluno', queue=queue, routing_key='matricula')


def callback(ch, method, properties, body):
    print(" [x] Recebida %r" % body)


channel.basic_consume(queue='contabil', on_message_callback=callback, auto_ack=True)
print(' [*] Aguardando mensagens... Para sair: CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()

"""
Declare a exchange. A exchange é o intermediário. É a entidade que irá receber as mensagens publicadas no servidor e 
irá endereçar para as filas. Lembre-se que a
publicação está sendo feita pela exchange de nome: ALUNO.
Declarando a exchange tanto no consumidor quanto no produtor se evita problemas de ter que subir um antes do outro.
Declare então uma fila para a exchange encaminhar as mensagens. Supondo que estamos no sistema de contabilidade e 
estamos querendo saber os alunos que se matricularam, declaramos o nome da fila como contabil.
Vinculamos então, a fila à exchange através do comando bind.
Lembra da routing-key? ela serve para filtrar as mensagens. Como esta fila só se interessa em matrículas, utilizo a 
palavra matricula como chave de filtro.
Defina uma ação para processar a mensagem recebida (que no nosso exemplo apenas irá imprimir a mensagem na tela). O 
nome da função não importa.
Inicie o consumo de mensagens referenciando a função que as processa e o nome da fila.
O método start_consuming() irá invocar a função callback sempre que chegar uma mensagem na fila da contabilidade.
"""

"""
ENVIANDO E RECEBENDO AS MENSAGENS
=================================

Com o servidor rodando, inicialize o arquivo: enviar.py e o receber.py
Verifique que após publicar cada mensagem, o receptor as recebe muito rapidamente!

Ao acessar o servidor do RabbitMQ, é possível observar as filas criadas, as Exchanges, os vínculos e as métricas de mensagens.
Bem como, fazer toda a gestão do servidor de mensageria.
Servidor (http://localhost:15672/#/):
Autenticação padrão do RabbitMQ:
Usuário: guest
Senha: guest
"""