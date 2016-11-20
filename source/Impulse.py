#!usr/bin/env python  
#coding=utf-8  

import serial
import pyaudio  
import wave  
from scipy.io import wavfile
import signal
from time import sleep

#For Myo Armband controls
import msvcrt


class ImpulseController():
    def __init__(self, playlist):
        self.play = True
        self.back = False
        self.restart = False
        self.forward = False
       
        self.get_com_port()
        self.playlist = playlist
        self.processed_songs = []
        for song in playlist:
            new_song = self.process_song(song)
            self.processed_songs.append(new_song)
    
    def get_com_port(self):
        self.com = raw_input("Input COM: ")
        return

    def send_to_mongo(color):
        mongoID = "b6MjZVfMLjMkaYEWGiOgkqAOYshLnzMg"
        url = 'https://api.mongolab.com/api/1/databases/impulseiot/collections/color?apiKey=' + mongoID
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        data = {'_id':{"$oid":'569b85f1e4b017432d15da2d'},'currentColor': color}
        data_json = json.dumps(data)
        response = requests.put(url, data = data_json, headers=headers )
        #print "response"
        #print response
        #print response.text
    
    def get_color_random():
        color = 0
        random_val = random.random()
        print "random_val = " + str(random_val)
        if random_val < (1.0/7.0):
            color = 0
        elif random_val > (1.0/7.0) and random_val <= (2.0/7.0):
            color = 1
        elif random_val > (2.0/7.0) and random_val <= (3.0/7.0):
            color = 2
        elif random_val > (3.0/7.0) and random_val <= (4.0/7.0):
            color = 3
        elif random_val > (4.0/7.0) and random_val <= (5.0/7.0):
            color = 4
        elif random_val > (5.0/7.0) and random_val <= (6.0/7.0):
            color = 5
        elif random_val > (6.0/7.0) and random_val <= (7.0/7.0):
            color = 6
        send_to_mongo(color)
        return color

    ## TODO: Accept Myo Armband controls
    ##def handleInterrupt():
    ##    key_press = msvcrt.getwch();
    ##    if key_press == ' ':
    ##        play = not play;
    ##           
    ##    if key_press ==  ',,':
    ##        back = True;
    ##    if key_press == ',':
    ##        restart = True;        
    ##    if key_press == '.':
    ##        forward = True;

    def process_song(self, title):
        ## Pre-Process the song
        print("Processing..." + title)
        fs, data = wavfile.read(title) # load the data
        light_mapping = [];
        data = data.T[0];

        #define stream chunk_size
        chunk_size = fs/16;

        index = 0;
        total_size = len(data);
        maximum = int(max(data));
        minimum = int(min(data));
        intervalSize = (minimum - maximum)/7;

        while(index < total_size):
          if(data[index] < -18000):
              light_mapping.append(0);
          elif(data[index] < -16000):
              light_mapping.append(1);
          elif(data[index] < -5000):
              light_mapping.append(2);
          elif(data[index] < 0):
              light_mapping.append(3);
          elif(data[index] < 5000):
              light_mapping.append(4);
          elif(data[index] < 16000):
              light_mapping.append(5);
          else:
              light_mapping.append(6);
          index += chunk_size;
        return (title, chunk_size)

    def play_all(self):
        for song in processed_songs:
            self.play_song(song_name, self.com)
            sleep(3);

    def play_song(self, song_data, com):
        title, chunk_size = song_data
        ## Play the song
        print("Let the song begin!")
        arduino = serial.Serial(com, 9600)

        # open a wav format music
        f = wave.open(title,"rb")  

        # instantiate PyAudio  
        p = pyaudio.PyAudio()  

        # open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk_size)
        light = 0
        def signal_handler(signal, frame):
            print 'Closing COM port'
            arduino.close()
            sys.exit(0)
    
        signal.signal(signal.SIGINT, signal_handler)

        #play stream  
        while data != '':
##          if (forward == True):
##               forward = False
##               return
##          if msvcrt.kbhit():
##              handleInterrupt()
            try:
                previous_light = light
                light = light_mapping.pop()
                if light != previous_light:
                    arduino.write(str(light))
            except:
                pass        
            stream.write(data)  
            data = f.readframes(chunk_size)
        # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio  
        p.terminate()
        arduino.close()