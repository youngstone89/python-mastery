import asyncio
from time import sleep

sem = asyncio.Semaphore(10)

# ... later
async def do(counter):
    print(f'number:{counter}')
    await sem.acquire()
    try:
        print('do')
    finally:
        sem.release()


asyncio.run(do(1))
asyncio.run(do(2))