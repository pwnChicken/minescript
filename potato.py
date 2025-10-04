import os
import minescript as m
import core.movement_pcww as move
import core.security as sec
import asyncio
import libraries.keyboard as keyboard
import winsound
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_file = os.path.join(BASE_DIR, "test3.wav")
sound_file = sound_file.replace("\\", "/") 

running = True
stop_event = asyncio.Event()


def on_key_event(event):
    # Detect RIGHT CTRL press only
    if event.name == "right ctrl" and event.event_type == "down":
        m.echo("<!!>Right Ctrl pressed -> stopping...")
        stop_event.set()

keyboard.hook(on_key_event)

async def play_sound():
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)


async def farming():
    global running, task, tasks
    while running:
        tasks = await move.phase_move_left_until_air(task, tasks)
        #winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        await asyncio.sleep(random.uniform(.5, 1.35))
        await move.phase_move_right_until_air()
        await asyncio.sleep(random.uniform(.3, 1.15))
        #winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

    
async def main():
    global running, task, tasks

    task = asyncio.create_task(farming())
    tasks = asyncio.create_task(sec.edge_cases(task))
    m.player_press_attack(True)
    

    while not task.done():
        if stop_event.is_set():
            print("Stopping")
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
    


m.echo("Starting!!!")
asyncio.run(main())