# Import the required module for text 
# to speech conversion 
from gtts import gTTS 
import webhook

# This module is imported so that we can 
# play the converted audio 
import os 
def read_text_file():
    # The text that you want to convert to audio 
    fil="busdata.txt"
    webhook.webHk(fil)
    f = open(fil, "r")
    # Language in which you want to convert 
    language = 'da' 
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myobj = gTTS(text=f.read(), lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome 
    myobj.save("busUpdates.mp3") 
    
    # Playing the converted file 
    os.system("busUpdates.mp3")
    return "busUpdates.mp3"
