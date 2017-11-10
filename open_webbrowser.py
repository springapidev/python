
#run 3 times
#open browser
#take a bbreak at every 10 seconds

import time
import webbrowser

total_breaks=3
break_count=0

print("Breat Started "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=J4qqnWscqeQ")
    break_count=break_count+1

