import os
import time
import psutil

cpu = psutil.cpu_percent(interval=1)
print(f"CPU usage:{cpu}%") 
#this variable collects data about cpu usage by calculating 
#it over 1-second interval

memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")
#this variable collects data about memory usage

disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
#this variable collects data about disk usage 

