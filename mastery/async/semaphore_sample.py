import asyncio
import time
from time import sleep

sem = asyncio.Semaphore(10)

# ... later


async def do(counter):
    print(f'number:{counter}')
    await sem.acquire()
    try:
        print('do{}'.format(counter))
        time.sleep(1)
    finally:
        sem.release()

for i in range(100):
    asyncio.run(do(i))
