import os
import subprocess

print(__file__)
print(os.path.dirname(os.path.realpath(__file__)))

print(os.listdir("music/"))

files = os.listdir("music/")

s = subprocess.Popen(["omxplayer", "--adev", "both", "--vol", "-2000", "music/"+files[1]],start_new_session=True, universal_newlines=True,stdin=subprocess.PIPE)
