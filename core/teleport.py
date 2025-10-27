import system.lib.minescript as m
import asyncio
import random
import core.security as sec

### Warps the player to the desired coordinates/warps
async def warp(task, tasks):
    m.echo(f"Teleporting to the beginning of the farm!!!")


    if tasks and not tasks.done() and tasks is not asyncio.current_task():
        # m.echo(f"Canceling tasks {tasks}")
        tasks.cancel()

    await asyncio.sleep(random.uniform(1, 2))
    
    if task.cancelled(): 
        m.echo("Task cancelled")
        return

    m.echo("Teleporting")
    await asyncio.sleep(random.uniform(.4, .9))
    m.execute('/warp garden') ### Replace with /warp garden
    await asyncio.sleep(random.uniform(.6, .8))
    tasks = asyncio.create_task(sec.edge_cases(task))
    return tasks