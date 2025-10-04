"""
How does a melon farm work? 
move left+forward or left until air infront or sign, then forward until block, then right, then forward, and repeat
Going to actually try and have good commets for once lmao
"""

import core.movement_pm as move
import core.security as sec
import minescript as m
import asyncio 
import libraries.keyboard as keyboard
import random


running = True
stop_event = asyncio.Event()


# Constantly check if a certain button is called
def on_key_event(event):
    # Detect RIGHT CTRL press only
    if event.name == "right ctrl" and event.event_type == "down":     # Change right ctrl to your button of choice
        m.echo("<!!>Right Ctrl pressed -> stopping...")
        stop_event.set()

keyboard.hook(on_key_event)


# main farming function
async def farming():
    global running, task, tasks
    while running: 
        tasks = await move.phase_move_left_until_air(task, tasks) # move left 
        await asyncio.sleep(random.uniform(.05, .1)) # random wait time to make it look less bot like

        await move.phase_move_forward_until_block() # move forward till the block
        await asyncio.sleep(random.uniform(.05, .1)) # random wait time to make it look less bot like

        tasks = await move.phase_move_right_until_air(task, tasks) # move right 
        await asyncio.sleep(random.uniform(.05, .1)) # random wait time to make it look less bot like

        await move.phase_move_forward_until_block() # move forward
        await asyncio.sleep(random.uniform(.05, .1)) # random wait time to make it look less bot like


## main function this is what makes everything run
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
    tasks.cancel()


    try:
        await task
    except asyncio.CancelledError:
        pass


### RUn the actual script 
m.echo("<+> Starting Farm")
asyncio.run(main())

