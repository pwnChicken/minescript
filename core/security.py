### Check that the players Y coordinate is within certain values
### Check that the item on the players hand isn't swapped
### Check if the players coordinates are moving, if not stop breaking blocks
### Check if there are any entintys flying around, scan for chat messages potentially too
#### ---->>>> Check if the players yaw/pitch changed <<<<----

#### ENTITIES line 700

from dataclasses import dataclass
from system.lib.minescript import entities, player
from core.sound import play_sound
from system.lib import minescript as m
import asyncio


async def entity_check(task):
    ### get player positions 
    try:
        m.echo("<+> Entity check started")
        while not task.done():
            player_pos = player().position
            ## get entities 
            radius = 10

            near_entities = entities(
                position=player_pos,
                max_distance=radius,
                type='entity.minecraft.player'
            )
            for ent in near_entities:
                #print(m.player_name())
                if ent.name != m.player_name():
                    play_sound()
                    m.echo(f"Entities {ent.name} at {ent.position}")
                    ## just checks if entity is ther. won't do anything, maybe play a slight sound queue

            await asyncio.sleep(.05)
    except asyncio.CancelledError:
        m.echo("<!> Entity check cancalled")
        return
    
async def player_item(task):
    #### make sure the players item isn't swapped. if swapped stop script within 2 seconds.
    try: 
        m.echo("<+> Player Item check started")
        start_player_item = m.player_hand_items()
        while not task.done():
            player_item = m.player_hand_items()
            # m.echo(player_item)
            if not start_player_item.main_hand:
                m.echo("Nothing held... Stopping script")
                task.cancel()
                break

            if not player_item.main_hand  or player_item.main_hand.get("item") != start_player_item.main_hand.get("item"):
                play_sound()
                m.echo("Player item swapped")
                await asyncio.sleep(0.3)
                task.cancel()
                m.echo("Farming stopped")
            await asyncio.sleep(0.5)

    except asyncio.CancelledError:
        m.echo("<!> Player item either changed or has nothing")
        return

async def sudden_movement(task):
    ### check for suddent movement such as teleport 
    try:
        m.echo("<+> Sudden Movement check started")
        while not task.done():
            x,y,z = player().position
            await asyncio.sleep(0.1)
            new_x,new_y,new_z = player().position
            if x - 15 < new_x < x + 15 and y - 5 < new_y < y + 5 and z - 15 < new_z < z + 15:
                ### m.echo("No sudden movement detected")
                continue
            else:
                play_sound()
                m.echo("suddent movemnet detected. Stopping script")
                task.cancel()
                break


    except asyncio.CancelledError:
        m.echo("<!> movement canceled")
        return


async def edge_cases(task):
    entity_task = asyncio.create_task(entity_check(task))
    item_task = asyncio.create_task(player_item(task))
    movement_task = asyncio.create_task(sudden_movement(task))

    try:
        await asyncio.shield(task)  # wait until main task is done or canceled
    finally:
        for t in [entity_task, item_task, movement_task]:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass
    