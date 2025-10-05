import system.lib.minescript as m
import asyncio
import math
import core.globals as globals
import time


player_orientation = {
    "S": 0,
    "E": 90,
    "N": 180,
    "W": 270
}


def playerDirection():
    yaw = m.player_orientation()[0] % 360  # only yaw
    for i in player_orientation:
        if player_orientation[i] - 22.5 < yaw < player_orientation[i]+22.5:
            return i
        if yaw > 337.5:
            return i
    return None

def getBlockCoordinatesFront(x,y,z):
    yaw = playerDirection()
    if yaw == "S":
        # print(x,y,z+1)
        return m.getblock(x,y,z+1)
    if yaw == "E":
        # print(x-1,y,z)
        return m.getblock(x-1,y,z)
    if yaw == "N":
        # print(x,y,z-1)
        return m.getblock(x,y,z-1)
    if yaw == "W":
        # print(x+1,y,z)
        return m.getblock(x+1,y,z)
    if yaw == -1:
        return None

def getBlockCoordinatesLeft(x, y, z):
    yaw = playerDirection()
    if yaw == "S":
        return m.getblock(x+1, y, z)
    if yaw == "E":
        return m.getblock(x, y, z+1)
    if yaw == "N":
        return m.getblock(x-1, y, z)
    if yaw == "W":
        return m.getblock(x, y, z-1)
    return None

def getBlockCoordinatesRight(x, y, z):
    yaw = playerDirection()
    if yaw == "S":
        return m.getblock(x-1, y, z)
    if yaw == "E":
        return m.getblock(x, y, z-1)
    if yaw == "N":
        return m.getblock(x+1, y, z)
    if yaw == "W":
        return m.getblock(x, y, z+1)
    return None


def get_block_in_front():
    m.echo("Starting block check")
    front_block = None
    if not globals.stop_pressed:
        raw_x, raw_y, raw_z = [p for p in m.player().position]
        # print(raw_x, raw_y, raw_z)
        x = math.floor(raw_x)
        y = math.floor(raw_y)
        z = math.floor(raw_z)
        # print(x,y,z)
        front_block = getBlockCoordinatesFront(x,y,z)
        # print(result)
    return front_block
    

def get_block_to_left():
    m.echo("Checking Left block")
    left_block = None
    if not globals.stop_pressed: 
        raw_x, raw_y, raw_z = [p for p in m.player().position]
        # print(raw_x, raw_y, raw_z)
        x = math.floor(raw_x)
        y = math.floor(raw_y)
        z = math.floor(raw_z)
        left_block = getBlockCoordinatesLeft(x,y,z)

    return left_block

def get_block_to_right():
    m.echo("Checking Right block")
    right_block = None
    if not globals.stop_pressed: 
        raw_x, raw_y, raw_z = [p for p in m.player().position]
        # print(raw_x, raw_y, raw_z)
        x = math.floor(raw_x)
        y = math.floor(raw_y)
        z = math.floor(raw_z)
        right_block = getBlockCoordinatesRight(x,y,z)


    return right_block

    

async def monitor():
    while True: 
        block = await get_block_in_front()
        if block and block == "minecraft:air":
            print(f"Detected block: {block}")
            break
        await asyncio.sleep(0.01)