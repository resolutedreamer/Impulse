#!usr/bin/env python  
#coding=utf-8  

import serial
import pyaudio  
import wave  
from scipy.io import wavfile # get the api
import sys
import msvcrt
import requests
import json

##play = True;
##back = False;
##restart= False;
##forward = False;

def main():
    if(len(sys.argv) <= 1):
       print("ERROR: Please input at least one song");
       sys.exit()
       
    com = raw_input("Input COM: ")
    
    for i in range(1, len(sys.argv)):
        song_name = sys.argv[i];
        playSong(song_name, com)
        sleep(3);
    ##  playSong('song.wav', 'COM41');

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

## TODO: Accept Myo Armband controls
##
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

def playSong(title, com):
    global play, back, restart, forward
    
    fs, data = wavfile.read(title) # load the data
    count = 0;
    light_mapping = [];
    arduino = serial.Serial(com, 9600)
    data = data.T[0];

    #define stream chunk   
    chunk = fs/8;

    index = 0;
    total_size = len(data);
    maximum = int(max(data));
    minimum = int(min(data));

    if(maximum < 0):
        intervalSize = (minimum - maximum)/7;
    else:
        intervalSize = (maximum - minimum)/7;

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
      index += chunk;

    #open a wav format music  
    f = wave.open(title,"rb")  

    #instantiate PyAudio  
    p = pyaudio.PyAudio()  

    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data != '':
##        if (forward == True):
##           forward = false;
##           return;
        
        try:
            previous_light = light
            light = light_mapping.pop()
            print(previous_light)
            print(light)
            if light != previous_light:
                arduino.write(str(light))
                send_to_mongo(light)
        except:
            pass
        
        stream.write(data)  
        data = f.readframes(chunk)
        
##        if msvcrt.kbhit():
##            handleInterrupt();

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  

    arduino.close();

# call main
if __name__ == '__main__':
  main()
