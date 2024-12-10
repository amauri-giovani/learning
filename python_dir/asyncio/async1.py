from asyncio import get_event_loop, coroutine


# @coroutine
async def print_async(msg):
    print("msg: {}".format(msg))

loop = get_event_loop()
loop.run_until_complete(print_async("oi"))
loop.close()