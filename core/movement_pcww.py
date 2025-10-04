
import minescript as m
import core.security as sec
import asyncio
import random

async def phase_move_right_until_air():
    m.player_press_right(True)
    await asyncio.sleep(random.uniform(1, 2))
    y = m.player().position[1]
    try:
        while True:
            new_y = m.player().position[1]
            if y > new_y:
                m.echo(f"Y level changed from {y} to {new_y}")
                break
            time = random.uniform(0.3, .7)
            # m.echo("Time: ", time)
            await asyncio.sleep(time)
    except asyncio.CancelledError:
        m.echo("Movement cancelled")
        raise  # Important: re-raise to propagate cancellation
    finally:
        m.player_press_right(False)

async def phase_move_left_until_air(task=None, tasks=None):
    m.player_press_left(True)
    await asyncio.sleep(random.uniform(1, 2))
    x,y,z = m.player().position
    try:
        await asyncio.sleep(.3)
        while True:
            new_x, new_y, new_z = m.player().position
            if y > new_y:
                m.echo(f"Y level changed from {y} to {new_y}")
                break 
            #m.echo(tasks)
            if tasks is not None:
                # m.echo("Tasks is not None")
                # m.echo(f"new_x:x, new_y:y, new_z:z; {new_x}:{x}, {new_y}:{y}, {new_z}:{z}")
                if new_x == x and new_y == y and new_z == z:
                    m.echo(f"Teleporting to the beginning of the farm!!!")
                    m.player_press_attack(False)
                    m.player_press_left(False)

                    if tasks and not tasks.done() and tasks is not asyncio.current_task():
                        m.echo(f"Canceling tasks {tasks}")
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
                    m.player_press_left(True)
                    m.player_press_attack(True)
                else: 
                    x = new_x 
                    y = new_y 
                    z = new_z
            time = random.uniform(0.3, .7)
            # m.echo("Time: ", time)
            await asyncio.sleep(time)
    except asyncio.CancelledError:
        # m.echo(f"Current task: {asyncio.current_task()}")
        m.echo("<!> Movement cancelled")
        raise  # Important: re-raise to propagate cancellation
    finally:
        m.player_press_left(False)

    return tasks