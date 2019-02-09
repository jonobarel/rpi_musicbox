#This is a wrapper for interfacing with an instance of omxplayer.
#When a song is played, the application launches an omxplayer process.
#Aspiration: While the song is playing it's possible to pause and resume, control volume, through appropriate inputs.
import subprocess

class SongPlayer:

    def __init__(self, files_list: [], path = "music/"):
        self.current = 0
        self.files_list = files_list
        self.procs = []
        self.current_proc = None

        if files_list == None:
            raise ValueError('missing parameter: files_list cannot be None')

        if not isinstance(files_list, list):
            raise TypeError('files_list parameter is not a list')

        if len(files_list) < 1:
            raise ValueError('files_list is empty')

        for f in files_list:
            if not isinstance(f, str):
                raise TypeError('files_list must only contain strings')
        
    

    #plays either the song at index i, or the next song on the list.
    #If a song is already playing, it will first stop the playback and begin the next one.
    def play(self):
        #start a new track
        if (self.current_proc == None or current_proc.poll() != None):
            self.current_proc = subprocess.Popen(["omxplayer", "--adev", "both", "--vol", "-2000", path+self.files_list[self.current]],start_new_session=True, stdin=subprocess.PIPE)
            self.current=(self.current+1)%len(files_list)
            
        #if a process exists, check if it is still running.
        #If so, send a pause signal.

        elif self.current_proc.poll() == None:
            current_proc.communicate('p')
        else: #process is not running
            raise Exception('Could not pause or play track')
            
            
                                  

    def next(self):
        

    #Pause the currently playing song
    #def pause(self):

    #def stop(self):
        
