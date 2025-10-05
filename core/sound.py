import os
import winsound
import system.lib.minescript as m




def play_sound():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(BASE_DIR, "test3.wav")
    sound_file = sound_file.replace("\\", "/") 
    m.echo("playing sound")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)