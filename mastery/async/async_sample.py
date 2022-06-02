import asyncio

async def run_test():
    print("running tests...")
    return 1

async def main():
    print('Hello ...')
    result = await run_test()
    print(result)
    print('... World!')

asyncio.run(main())