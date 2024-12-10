import asyncio

'''
Fonte: http://brunorocha.org/python/asyncio-o-futuro-do-python-mudou-completamente.html

Nota do tradutor: Em uma loja de doces há um funcionário empacotando balas, ao finalizar cada pacote ele o lacra e 
coloca na vitrine (YIELD), então ele dá uma olhada no balcão para ver se tem algum cliente para ser atendido, se 
tiver um cliente, então ele para de empacotar balas atende o pedido do cliente (troca de contexto). E só depois de 
terminar de > atender o cliente ele então volta a empacotar as balas, caso não tenha cliente a ser atendido ele 
simplesmente continua o trabalho de empacotamento. Podemos dizer que é um funcionário fazendo duas tarefas __.
'''


@asyncio.coroutine
def empacotar_bala():
    print("Empacotando balas...")

    # parada para verificar se tem cliente no balcão
    yield from asyncio.sleep(0)

    # troca de contexto
    print("Explicitamente voltando a empacotar balas")


@asyncio.coroutine
def atender_balcao():
    print("Explicitamente verificando se tem cliente no balcão...")

    yield from asyncio.sleep(0)

    print("Voltando a empacotar as balas")


ioloop = asyncio.get_event_loop()

tasks = [
    ioloop.create_task(empacotar_bala()),
    ioloop.create_task(atender_balcao())
]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)

ioloop.close()
