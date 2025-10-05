import system.lib.minescript as m
import asyncio
import core.block_check as bc
import core.teleport as teleport
import core.globals as globals
import random

async def phase_move_right_until_air(task=None, tasks=None):
    m.player_press_forward(True)
    m.player_press_right(True)
    x,y,z = m.player().position
    teleported = False
    try:
        await asyncio.sleep(.3)
        while not globals.stop_pressed and not teleported:
            # m.echo(block)
            new_x, new_y, new_z = m.player().position
            if not new_x - 1 < x < new_x + 1: ### Change the block to whatever stops the water, probably signs
                m.echo("Oak Sign Detected")
                m.player_press_right(False)
                await asyncio.sleep(random.uniform(0.3, .5))
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            # m.echo("Teleport Conditions Checked")
            elif tasks is not None:
                # m.echo("Tasks is not None")
                # m.echo(f"new_x:x, new_y:y, new_z:z; {new_x}:{x}, {new_y}:{y}, {new_z}:{z}")
                if new_x == x and new_y == y and new_z == z:
                    # m.echo("Teleport Conditions met")
                    tasks = await teleport.warp(task, tasks)
                    teleported = True
                    m.echo(teleported)
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            time = random.uniform(0.1, .3)
            # print("Time: ", time)
            await asyncio.sleep(time)
    except asyncio.CancelledError:
        m.echo("movement cancelled")

    finally:
        m.player_press_right(False)
        m.player_press_forward(False)

    return tasks

"""
async def phase_move_forward_until_block():
    m.player_press_forward(True)
    try:
        while True:
            block = await bc.get_block_in_front()
            if block != "minecraft:air":  # stop at wall
                break
            time = random.uniform(0.3, 1)
            print("Time: ", time)
            await asyncio.sleep(time)
    finally:
        m.player_press_forward(False)
"""

async def phase_move_left_until_air(task=None, tasks=None):
    m.player_press_left(True)
    m.player_press_forward(True)
    x,y,z = m.player().position
    teleported = False
    try:
        await asyncio.sleep(.3)
        while not globals.stop_pressed:
            if teleported:
                x,y,z = m.player().position
            new_x, new_y, new_z = m.player().position
            # print(x, new_x)
            if not new_x - 1 < x < new_x + 1: ### Change the block to whatever stops the water, probably signs
                m.echo("Oak Sign Detected")
                m.player_press_left(False)
                await asyncio.sleep(random.uniform(0.3, .5))
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            # m.echo("Teleport Conditions Checked")
            elif tasks is not None:
                if new_x == x and new_y == y and new_z == z:
                    tasks = await teleport.warp(task, tasks)
                    teleported = True
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            time = random.uniform(0.2, .6)
            # print("Time: ", time)
            await asyncio.sleep(time)
    except asyncio.CancelledError:
        m.echo("movement cancelled")
    finally:
        m.player_press_left(False)
        m.player_press_forward(False)
    return tasks

        