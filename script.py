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


while (tick<=10): # loop by default will gather data for 10 seconds
    cpu = psutil.cpu_percent(interval=1)
    file.write(f"CPU usage:{cpu}% \n") 
    #this variable collects data about cpu usage by calculating 
    #it over 1-second interval

    memory = psutil.virtual_memory()
    file.write(f"Memory Usage: {memory.percent}% \n")
    #this variable collects data about memory usage

    disk = psutil.disk_usage('/')
    file.write(f"Disk Usage: {disk.percent}% \n")
    #this variable collects data about disk usage
    data.append([cpu, memory.percent, disk.percent]) #appends all data to list

    tick = tick +1 #incrementing tick
    time.sleep(1) #Pause for 5 second
df1 = pd.DataFrame(data, columns=['Cpu Usage (%)','Memory Usage (%)','Disk usage (%)']) # this variable holds system monitor data
print(df1) #printing table in the terminal
file.close()
