import pandas as pd
import time
import psutil

lg="logs.txt" #variable holding file name
file = open(lg,'a') #opening file
seconds =time.time() 
local_time=time.ctime(seconds)
file.write(f"\n Time of starting the script " + local_time + "\n")
tick=1 #variable holding tick number
data=[] #initialazing empty list

while (tick<=60): # loop by default will gather data for 5 ticks, tick=15seconds
    cpu = psutil.cpu_percent(interval=1)#this variable collects data about cpu usage by calculating it over 1-second interval
    file.write(f"CPU usage:{cpu}% \n") 
    
    memory = psutil.virtual_memory()#this variable collects data about memory usage
    file.write(f"Memory Usage: {memory.percent}% \n") #this variable holds memory usage in Bytes and its converteted to MegaBytes afterwads
    memory_MB = psutil.virtual_memory().used / (1024 ** 2)
    memory_MB = round(memory_MB)

    disk = psutil.disk_usage('/')#this variable collects data about disk usage
    file.write(f"Disk Usage: {disk.percent}% \n")
    disk_MB = psutil.disk_usage('/').used / (1024 ** 2) #this variable holds disk usage in Bytes and its converteted to MegaBytes afterwads
    disk_MB = round(disk_MB,2) #

    Timestamp=pd.Timestamp.now().strftime('%H:%M:%S')
    data.append([Timestamp,cpu, memory.percent, disk.percent,memory_MB,disk_MB]) #appends all data to list

    tick = tick +1 #incrementing tick
    time.sleep(30) #Pause

df1 = pd.DataFrame(data,columns=['Timestamp','Cpu Usage (%)','Mem Usage (%)','Disk usage (%)','Mem Usage (MB)','Disk Usage (MB)'])
# this variable holds system monitor data
df1.set_index('Timestamp', inplace=True)
print(df1) #printing table in the terminal
file.close()

