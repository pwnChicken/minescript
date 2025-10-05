import core.block_check as bc
import core.globals as globals


print("Front", bc.get_block_in_front())
print("Left", bc.get_block_to_left())
print("Right", bc.get_block_to_right())

globals.stop_pressed = True