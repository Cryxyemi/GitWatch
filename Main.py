import asyncio
from config import watch
from src.Checker import check_watch


async def main():
    watches = watch.get_watches()

    for watchh in watches:
        repo = watchh[2]

        await check_watch(watchh)

        print(f"Starting watch {repo}")

    print("GitWatch is running")

asyncio.run(main())
