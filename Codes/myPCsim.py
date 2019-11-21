'''
Created on 1 Nov 2019

@author: lxmi
'''
'''
Created on 31 Oct 2019

@author: lxmi
'''

import os
import os.path
import sys
import paho.mqtt.client as mqtt
import text2sp
import time
from datetime import datetime
#text2sp.read_text_file()    
def on_connect(client, userdata, flags, rc):
    print("MyPC Connected with result code "+str(rc))
    client.subscribe("topic/moDet")

def on_message(client, userdata, msg):
    print("Recieving from Site")
    p= text2sp.read_text_file()
    f = open(p, "rb")
    imagestring = f.read()
    f.close()
    byteArray = bytearray(imagestring)
    client.publish(topic="topic/Voice", payload=byteArray, retain=False)
    client.disconnect()
    
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")


#def myPCsm():

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
#client.connect("test.mosquitto.org", 1883, 60)
client.connect("5.196.95.208", 1883, 60)
client.loop_start()