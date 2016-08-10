#!/usr/bin/env python
import mraa
import random
import requests
import json
from time import sleep
	
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
	
def get_color_mongo():
	mongoID = "b6MjZVfMLjMkaYEWGiOgkqAOYshLnzMg"
	url = 'https://api.mongolab.com/api/1/databases/impulseiot/collections/color/569b85f1e4b017432d15da2d?apiKey=' + mongoID
	response = requests.get(url)
	json_reponse = response.json()
	print "json_reponse"
	print json_reponse
	final_answer = json_reponse["currentColor"]
	return final_answer
	

print (mraa.getVersion())
REDPIN = mraa.Gpio(11)
GREENPIN = mraa.Gpio(10)
BLUEPIN = mraa.Gpio(13)


FADESPEED = 5 #make this higher to slow down

REDPIN.dir(mraa.DIR_OUT)
REDPIN.write(1)
GREENPIN.dir(mraa.DIR_OUT)
GREENPIN.write(1)
BLUEPIN.dir(mraa.DIR_OUT)
BLUEPIN.write(1)

while (1):
	#sleep(5)
	#get_color_random()
	color = get_color_mongo()
	print "color = " + str(color)
	
	if color == 0:
		REDPIN.write(0)
		GREENPIN.write(0)
		BLUEPIN.write(1)
	elif color == 1:
		REDPIN.write(0)
		GREENPIN.write(1)
		BLUEPIN.write(0)
	elif color == 2:
		REDPIN.write(0)
		GREENPIN.write(1)
		BLUEPIN.write(1)
	elif color == 3:
		REDPIN.write(1)
		GREENPIN.write(0)
		BLUEPIN.write(0)
	elif color == 4:
		REDPIN.write(1)
		GREENPIN.write(0)
		BLUEPIN.write(1)
	elif color == 5:
		REDPIN.write(1)
		GREENPIN.write(1)
		BLUEPIN.write(0)
	elif color == 6:
		REDPIN.write(1)
		GREENPIN.write(1)
		BLUEPIN.write(1)