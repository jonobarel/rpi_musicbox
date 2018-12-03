import RPi.GPIO as GPIO
import time
import os
import signal

from subprocess import Popen as po

path = '/home/pi/music/'
files = os.listdir(path)
for f in files:
    print(f)
    #subprocess.run(["omxplayer", path+f])
    #time.sleep(3)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)

#TODO get a list of running players and kill them all. KILL THEM WITH FI9E!
#TODO set the input and output labels to variables so that people using this can decide where they want to make connections


p = None
i = 0
n = len(files)

#signal that the app is running
#TODO set the sleep delay to a variable and make this better
#what is the python equivalent of ruby's "3.times.do {}"?
po(["omxplayer", "/home/pi/audio/mariocoin.mp3"])
for i in [1,2,3]:
    GPIO.output(18,True)
    time.sleep(0.2)
    GPIO.output(18,False)
    time.sleep(0.2)
    

while True:
    if GPIO.input(25):
        GPIO.output(18, False)
    else:
        if (i==n): #we're playing the last song. Time to stop and reset the player to 0
            if p!= None:
                os.killpg(os.getpgid(p.pid),1)
            i=0
        GPIO.output(18,True)
        #create a process to play a song, and track it. We first need to check if there is one.
        if (p != None): #kill the currently playing song
            "stopping playback for "+p.args[1]
            #p.send_signal(1) #TODO kill playing song
            #TODO add a LED for playback
            os.killpg(os.getpgid(p.pid), 1)
        print("playing "+files[i])
        p = po(["omxplayer", path+files[i]],start_new_session=True)
        #i = (i+1)%n #next file or go to first
        i+=1
        time.sleep(1)
