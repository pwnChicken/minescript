"""
Movement: Start W, then change to W+D, then W and rinse and repeat

Edge cases: Implement yaw/pitch changes too!! 

"""


import core.movement_shroom as move
import core.security as sec
import system.lib.minescript as m
import core.globals as globals
import asyncio
import libraries.keyboard as keyboard
import random 

running = True
stop_event = asyncio.Event()

def on_key_event(event):
    if event.name =="right ctrl" and event.event_type == "down":
        m.echo("<!!> Right Ctrl pressed -->> Stopping... ")
        globals.stop_pressed = True
        
        stop_event.set()

keyboard.hook(on_key_event)

async def farming():
    global running, task, tasks
    while running: 
        #print(tasks)
        tasks = await move.phase_move_forward_until_air(task, tasks)
        #print(tasks)
        await asyncio.sleep(random.uniform(.192, .64))

        tasks = await move.phase_move_forward_left_until_air(task, tasks)
        await asyncio.sleep(random.uniform(.172, .61))



async def main():
    global running, task, tasks

    task = asyncio.create_task(farming())
    tasks = asyncio.create_task(sec.edge_cases(task))
    m.player_press_attack(True)

    while not task.done():
        if stop_event.is_set():
            m.echo("<-> Stopping Script")
            running = False
            task.cancel()
            tasks.cancel()

        await asyncio.sleep(0.05)
    m.player_press_attack(False)
    task.cancel()
    tasks.cancel()

    try: 
        await task
    except asyncio.CancelledError:
        pass

### Run the actual script 
m.echo("<+> Starting Farm")
asyncio.run(main())