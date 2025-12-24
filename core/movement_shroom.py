import system.lib.minescript as m
import asyncio
import core.block_check as bc
import core.teleport as teleport
import core.globals as globals
import random

async def phase_move_forward_until_air(task = None, tasks=None):
    m.echo("Moving forward")
    m.player_press_forward(True)
    x,y,z = m.player().position
    teleported = globals.teleported
    try: 
        await asyncio.sleep(.3)
        while not globals.stop_pressed:
            #m.echo("itteraration wxyz")
            new_x, new_y, new_z = m.player().position
            # m.echo(f"new_x:x, new_y:y, new_z:z; {new_x}:{x}, {new_y}:{y}, {new_z}:{z}")
            if not new_x - 1 < x < new_x + 1 and not globals.teleported:
                m.echo("Air Detected")
                await asyncio.sleep(random.uniform(.67, .89))
                m.player_press_forward(False)
                # await asyncio.sleep(random.uniform(0.3, .5))
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            # m.echo("Teleport Conditions Checked")
            elif tasks is not None and not globals.teleported:
                # m.echo("Tasks is not None")
                # m.echo(f"new_x:x, new_y:y, new_z:z; {new_x}:{x}, {new_y}:{y}, {new_z}:{z}")
                if new_x == x and new_y == y and new_z == z:
                    # m.echo("Teleport Conditions met")
                    tasks = await teleport.warp(task, tasks)
                    globals.teleported = True
                    m.echo(teleported)
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            elif globals.teleported:
                m.echo("elif teleported true")
                x = new_x
                y = new_y
                z = new_z
                globals.teleported = False
            time = random.uniform(0.1, .3)
            # print("Time: ", time)
            await asyncio.sleep(time)

    except asyncio.CancelledError:
        m.echo("Movement cancelled")
    finally:
        m.player_press_forward(False)
        m.player_press_right(False)

    return tasks

async def phase_move_forward_left_until_air(task = None, tasks=None):
    m.echo("Moving forward+right")
    m.player_press_forward(True)
    m.player_press_right(True)
    x,y,z = m.player().position
    teleported = False
    try: 
        await asyncio.sleep(.3)
        while not globals.stop_pressed:
            if teleported:
                x,y,z = m.player().position
                teleported = False
                await asyncio.sleep(0.2)
            #m.echo("Itteration xyz")
            new_x, new_y, new_z = m.player().position
            if not new_x - 1 < x < new_x + 1:
                m.echo("Air Detected")
                await asyncio.sleep(random.uniform(.71, .92)) 
                m.player_press_forward(False)
                # await asyncio.sleep(random.uniform(0.3, .5))
                break
            ### Check if the player is moving in any direction. If not teleport back to start
            elif tasks is not None and not teleported:
                # m.echo("Teleport Conditions Checked")
                # m.echo("Tasks is not None")
                ## m.echo(f"new_x:x, new_y:y, new_z:z; {new_x}:{x}, {new_y}:{y}, {new_z}:{z}")
                if new_x == x and new_y == y and new_z == z:
                    # m.echo("Teleport Conditions met")
                    m.player_press_forward(False)
                    m.player_press_right(False)
                    tasks = await teleport.warp(task, tasks)
                    teleported = True
                    m.echo(teleported)
                    m.player_press_forward(True)
                    m.player_press_right(True)
                else: 
                    x = new_x
                    y = new_y
                    z = new_z
            time = random.uniform(0.1, .3)
            # print("Time: ", time)
            await asyncio.sleep(time)



    except asyncio.CancelledError:
        m.echo("Movement cancelled")
    finally:
        m.player_press_forward(False)
        m.player_press_right(False)

    return tasks