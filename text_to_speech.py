
# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")