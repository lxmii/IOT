# importing the requests library 
import json
import datetime
datetime.datetime.now()
import requests
# api-endpoint 

def webHk(fil):
    
        
    
    
    
    # importing the requests library 
    
    
    
    url="http://xmlopen.rejseplanen.dk/bin/rest.exe"
    
    today=datetime.datetime.now()
    dat= ("%s.%s.%s"%(today.day,today.month, today.year))
    tim= ("%s:%s"%(today.hour,today.minute))
    print(dat, tim)
    
    #http://xmlopen.rejseplanen.dk/bin/rest.exe/trip?originId=657205202&destCoordX=9032640&destCoordY=56129230&destCoordName=Herning%St.&date=06.12.19&time=12:42
    
    baseURL= ("%s/trip"%url)
    
    par={'originId':'657101902', 'destCoordX':'9032640','destCoordY':'56129230','destCoordName':'Herning St.', 'date':dat,'time':tim,'format':'json'}
    
    
    print(baseURL)
    res=requests.get(url=baseURL, params=par)
    jSon=res.json()
    #print(json.dumps(jSon, indent=4, sort_keys=True))
    time= jSon['TripList']['Trip'][0]['Leg'][0]['Origin']['time']
    name= jSon['TripList']['Trip'][0]['Leg'][0]['name']
    
    print(name, time)
    # printing the output 
    F= ("Den næste bus er :%s som ankommer:%s kører til Herning station"%(name, time))  
    #print("writing %s to text file"%(F))
    f1= open(fil, "w")
    f1.seek(0)
    f1.write(F)
    f1.close()
    
