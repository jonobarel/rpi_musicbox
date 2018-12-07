#import RPi.GPIO as GPIO
import time
import os
import signal

from subprocess import Popen as po

music_path = 'music/' #relative path to music. Maybe make this configurable? let's keep it simple for now.
wd = os.path.dirname(os.path.realpath(__file__)) #working directory

files = os.listdir(music_path)
for f in files:
    print(f)
    #subprocess.run(["omxplayer", music_path+f])
    #time.sleep(3)

NEXT=25
PLAY=None
LED=18

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED,GPIO.OUT)
#GPIO.setup(NEXT,GPIO.IN)

#TODO get a list of running players and kill them all. KILL THEM WITH FI9E!
#TODO set the input and output labels to variables so that people using this can decide where they want to make connections


p = None
i = 0
n = len(files)

#signal that the app is running
#TODO set the sleep delay to a variable and make this better
#what is the python equivalent of ruby's "3.times.do {}"?
po(["omxplayer", "audio/341695__projectsu012__coins-1.wav"])
for i in [1,2,3]:
    GPIO.output(LED,True)
    time.sleep(0.2)
    GPIO.output(LED,False)
    time.sleep(0.2)
    

while True:
    if GPIO.input(NEXT):
        GPIO.output(LED, False)
    else:
        if (i==n): #we're playing the last song. Time to stop and reset the player to 0
            if p!= None:
                os.killpg(os.getpgid(p.pid),1)
            i=0
        GPIO.output(LED,True)
        #create a process to play a song, and track it. We first need to check if there is one.
        if (p != None): #kill the currently playing song
            "stopping playback for "+p.args[1]
            #p.send_signal(1) #TODO kill playing song
            #TODO add a LED for playback
            os.killpg(os.getpgid(p.pid), 1)
        print("playing "+files[i])
        p = po(["omxplayer", music_path+files[i]],start_new_session=True)
        #i = (i+1)%n #next file or go to first
        i+=1
        time.sleep(1)
