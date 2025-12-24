"""
Purpose of this is to stop everything minescript side in case it didn't stop (clicking/moving)

"""
from system.lib import minescript as m

def stopping():
    m.player_press_attack(False)
    m.player_press_backward(False)
    m.player_press_left(False)
    m.player_press_right(False)
    m.player_press_forward(False)