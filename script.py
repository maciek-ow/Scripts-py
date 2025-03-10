import os
import time
import psutil

lg="logs.txt"
file = open(lg,'a')
seconds =time.time()
local_time=time.ctime(seconds)
file.write(f"\n Time of starting the script " + local_time + "\n")
tick=1 #variable holding tick number
while (tick<=5):
    cpu = psutil.cpu_percent(interval=1)
    file.write(f"CPU usage:{cpu}% \n") 
    print(f"CPU usage:{cpu}%")
    #this variable collects data about cpu usage by calculating 
    #it over 1-second interval

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    file.write(f"Memory Usage: {memory.percent}% \n")
    #this variable collects data about memory usage

    disk = psutil.disk_usage('/')
    file.write(f"Disk Usage: {disk.percent}% \n")
    print(f"Disk Usage: {disk.percent}%")
    #this variable collects data about disk usage


    tick = tick +1 #incrementing tick
    time.sleep(1) #Pause for 5 second
file.close()