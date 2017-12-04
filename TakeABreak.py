import time
import webbrowser

i=0
print ("This program started at"+time.ctime())
while i < 2 :
 webbrowser.open('https://www.google.com')
 time.sleep(25)
 i= i+1 
