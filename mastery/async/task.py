import asyncio

async def nested():
    return 42

async def runTask():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)


async def runTaskWithFuture():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.ensure_future(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)

asyncio.run(runTask())
asyncio.run(runTaskWithFuture())