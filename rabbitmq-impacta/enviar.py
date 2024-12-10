"""
RABBITMQ
========
Este arquivo é responsável pela publicação de mensagens

Em uma máquina com o docker instalado, puxe a imagem para sua máquina. Digite:
docker pull rabbitmq

Rodar RabbitMQ com Docker:
docker run -d --hostname rabbitmq-node --name rabbitmq --security-opt apparmor=unconfined -p 15672:15672 -p 5672:5672
rabbitmq:3-management

O que são estes parâmetros?
docker run -d - Inicializa o container em background e imprime o id
--hostname - Nome do servidor dentro do container
--name - Nome do container
-p - Mapeia portas de dentro do container para a máquina hospedeira
rabbitmq:3-management - Nome da imagem docker a ser usada.

Agora que você já tem um servidor RabbitMQ rodando, veja como é fácil publicar mensagens.
Utilizaremos a biblioteca de nome PIKA para python_dir.
Instalar pika:
pip install pika

O loop while irá manter a nossa aplicação pronta para enviar uma nova mensagem atrás da outra.
Para enviar, criamos uma conexão e um canal.
Então, solicitamos ao usuário para escrever uma mensagem.
Então, enviamos a mensagem pela ​ exchange ​ alunos com a ​ routing-key ​ matricula.
Guarde estas palavras: ​ exchange ​ e ​ routing-key pois vamos explicá-las na criação dos receptores.
Se não criarmos um receptor para estas mensagens, elas chegarão no servidor do RabbitMQ e serão descartadas por não
ter ninguém as escutando em nenhuma fila.
Vamos então implementar um receptor para estas mensagens.
"""

import pika

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    userinput = input('insira a mensagem: ')
    channel.basic_publish(exchange='aluno', routing_key='matricula', body=userinput)
    print(" [x] Sent: ", userinput)
