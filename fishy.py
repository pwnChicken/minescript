import system.lib.minescript as m
import time
import random
import core.globals as globals
import libraries.keyboard as keyboard
import asyncio

globals.fishy_toggle = True
stop_event = asyncio.Event()

# Constantly check if a certain button is called
def on_key_event(event):
    # Detect RIGHT CTRL press only
    if event.name == "right ctrl" and event.event_type == "down":     # Change right ctrl to your button of choice
        m.echo("<!!>Right Ctrl pressed -> stopping...")
        globals.fishy_toggle = False

        stop_event.set()

keyboard.hook(on_key_event)
m.echo("Key_Event Started")

n = 0
m.echo(globals.fishy_toggle)
while globals.fishy_toggle:

    for ent in m.entities():
        if ent.name and "!!!" in ent.name:
            m.echo("Fishing Itteration", n)
            m.player_press_use(True)
            m.player_press_use(False)
            time.sleep(random.uniform(0.3,0.7))
            m.player_press_use(True)
            m.player_press_use(False)
            time.sleep(random.uniform(0.3,0.7))
            n=+1
    time.sleep(0.1)