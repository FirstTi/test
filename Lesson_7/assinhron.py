import asyncio
import requests
import aiohttp
from datetime import datetime

resource_list = ["https://github.com/", "https://www.youtube.com/", "https://pythonru.com/",
                 "https://ru.wikipedia.org/wiki/", "https://ioboot.in/kak-izmenit-temu-pycharm/"
                 ]

sync_t1 = datetime.now()
for resource in resource_list:
    r = requests.get(resource)    #последовательный запуск запросов, обратились к гитхабу, дождались ответа, и так далее
    print(len(r.text))
sync_t2 = datetime.now()
sync_delta = sync_t2 - sync_t1
print(sync_delta)

async def get_data(url):
    print(f"Start {url}")                          # при создании функций для асинхронного програмирования необходимо писать перед обьявлением
    async with aiohttp.ClientSession() as session: # функции async(при создании Менеджера контекста нужно добавлять a.__enter__ и a.__exit__)
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))

t1 = datetime.now()
jobs = [get_data(url) for url in resource_list]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(jobs))
t2 = datetime.now()

delta = t2 - t1
print(f"Время выполнения :{delta.microseconds}")
