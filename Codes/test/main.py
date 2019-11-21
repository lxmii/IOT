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
import threading




#text2sp.read_text_file()    
def on_connectPC(client_PC, userdata, flags, rc):
    client_PC.subscribe("topic/moDet")
    print("PC subscribed to moDet")
def on_connectPhoton(client_Photon, userdata, flags, rc): 
    client_Photon.subscribe("topic/Voice")
    print("Photon Subscribed to Voice"+str(rc))
    
    
def myPC(msg):
    if msg.decode("utf-8")=="moDet":
        print("PC creates voice file")
        p= text2sp.read_text_file()
        f = open(p, "rb")
        
        imagestring = f.read()
        f.close()
        print("PC publishes data and Voice")
        byteArray = bytearray(imagestring)
        client_PC.publish(topic='topic/Voice', payload=byteArray, retain=False) #PC publishes Voice to photon
    #client.disconnect()
def myPhoton(msg):
    global lp
    print("Write")
    
    f = open('rcv.mp3', 'wb')
    f.write(msg)
    lp= True
    #print("lp flag set to "+str(lp))
    os.system(f)
    f.close()
    
   
        
def on_messagePhoton(client_Photon, userdata, msg): #subscription received
    print("Voice from PC recieved by Photon")
    myPhoton(msg.payload)
    
def on_messagePC(client_PC, userdata, msg): #subscription received
    #moDet is subscribed by PC
    print("Motion detected on site")
    myPC(msg.payload)
   
        
def on_publishPC(client_PC,userdata,result):             #create function for callback
    print("Voice published by PC\n")
def on_publishPhoton(client_Photon,userdata,result):             #create function for callback
    print("MoDet published by photon\n")

def Photon():
    
    global lp
    if os.path.exists('./test.txt'):  
        print("Found test.txt")
        prevStat= os.path.getmtime('./test.txt')
        latestStat= prevStat
    while True: 
        #print("PC relinquished control") 
        #print("lp flag set to "+str(lp))
        while lp==True:
            
            print("Checking for changes")       
            if latestStat!=prevStat:
                 
                
                prevStat=latestStat
                print("Motion detected")
                client_Photon.publish(topic='topic/moDet', payload="moDet", retain=False) #photon detects movement and publishes
                time.sleep(1)
                lp=False
                #client_Photon.loop_stop()
            else: 
                latestStat= os.path.getmtime('./test.txt')
                #print("Sleeping")
                time.sleep(0.5)
        time.sleep(1)
    
def PC():
    global lp
    while not lp:
        print("PC sleeps") 
        lp=True
        time.sleep(0.25)
    
    
    
lp=True    
client_PC = mqtt.Client()
client_Photon = mqtt.Client()

client_PC.on_connect = on_connectPC
client_PC.on_message = on_messagePC
client_PC.on_publish = on_publishPC 

client_Photon.on_connect = on_connectPhoton
client_Photon.on_message = on_messagePhoton
client_Photon.on_publish = on_publishPhoton 



client_PC.connect("5.196.95.208", 1883, 60)
client_Photon.connect("5.196.95.208", 1883, 60)

client_Photon.loop_start() 
client_PC.loop_start()
Photon= threading.Thread(target=Photon())
PC= threading.Thread(target=PC())
Photon.start()
PC.start() 

'''

Photon()
PC()

#print("PC thread started")


'''


