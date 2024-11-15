import psutil
import time

Threshold = 80

while True:
    #CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > Threshold:
        print(f"High CPU usage detected: {cpu_usage}%")

    #memory usage
    memory = psutil.virtual_memory()
    if memory.percent > Threshold:
        print(f"High Memory usage detected: {memory.percent}%")

    # Check disk usage
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > Threshold:
        print(f"High Disk usage detected: {disk_usage.percent}%")

    time.sleep(5)
