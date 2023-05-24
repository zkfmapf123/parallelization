import asyncio
import time


async def print_sleep(name, sec):
    print(f"{name} >> started...")
    await asyncio.sleep(sec)
    print(f"{name} >> end...")
    return name


async def main():
    print("--------- start coroutin --------")

    task_list = [print_sleep("leedonggyu", i) for i in range(10)]
    corous = [asyncio.create_task(task) for task in task_list]
    results = await asyncio.wait(corous)

    for result in results:
        print(result())


if __name__ == "__main__":
    startTime = time.time()
    asyncio.run(main())
    print(time.time() - startTime)
