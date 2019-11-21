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

import time
from datetime import datetime
#text2sp.read_text_file()    
def on_connect(client1, userdata, flags, rc):
    print("Photon Connected with result code "+str(rc))
    client1.subscribe("topic/Voice")

def on_message(client1, userdata, msg):
    print("Write")
    f = open('rcv.mp3', 'wb')
    f.write(msg.payload)
    f.close()
    client1.disconnect()
    
def on_publish(client1,userdata,result):             #create function for callback
    print("topic/moDet published with payload True \n")
    



    
def phSim():
    
    if os.path.exists('./test.txt'):  
        print("Found test.txt")
        prevStat= os.path.getmtime('./test.txt')
        latestStat= prevStat
    else:
        print("No such path")
        sys.exit()
    client1 = mqtt.Client()
    client1.on_connect = on_connect
    client1.on_message = on_message
    client1.on_publish = on_publish 
    #client.connect("test.mosquitto.org", 1883, 60)
    client1.connect("5.196.95.208", 1883, 60)
    client1.loop_start()
    while client1.loop()==0:
    
        if latestStat!=prevStat: 
            prevStat=latestStat
            print("Motion detected")
            client1.publish(topic="topic/moDet", payload="True", retain=False)
        else: 
            latestStat= os.path.getmtime('./test.txt')
        time.sleep(1)