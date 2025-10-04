import system.lib.minescript as m
import asyncio
import core.block_check as bc
import core.teleport as teleport
import random

async def phase_move_right_until_air(task=None, tasks=None):
    m.player_press_right(True)
    x,y,z = m.player().position
    teleported = False
    try:
        await asyncio.sleep(.3)
        while True and not teleported:
            block = await bc.get_block_in_front()
            if block == "minecraft:air": ### Change the block to whatever stops the water, probably signs
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            new_x, new_y, new_z = m.player().position
            if tasks is not None:
                if new_x == x and new_y == y and new_z == z:
                    tasks = await teleport.warp(task, tasks)
                    teleported = True
                    m.echo(teleported)
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            time = random.uniform(0.3, 1.5)
            print("Time: ", time)
            await asyncio.sleep(time)
    finally:
        m.player_press_right(False)
    return tasks


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


async def phase_move_left_until_air(task=None, tasks=None):
    m.player_press_left(True)
    x,y,z = m.player().position
    teleported = False
    try:
        await asyncio.sleep(.3)
        while True and not teleported:
            block = await bc.get_block_in_front()
            if block == "minecraft:air":
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            new_x, new_y, new_z = m.player().position
            if tasks is not None:
                if new_x == x and new_y == y and new_z == z:
                    tasks = await teleport.warp(task, tasks)
                    teleported = True
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            time = random.uniform(0.3, 1.5)
            print("Time: ", time)
            await asyncio.sleep(time)
    finally:
        m.player_press_left(False)
    return tasks

        