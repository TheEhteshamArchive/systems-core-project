import psutil
import time

def get_top_processes(limit=5):
    processes = []

    #Initializing the cpu measurements
    for process in psutil.process_iter():
        try:
            process.cpu_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(1) # waiting for measurement

    grouped_processes = {}

    for process in psutil.process_iter(["name", "memory_percent"]):
        try:
            name = process.info["name"] or "Unkown"

            cpu = process.cpu_percent()
            memory = process.info["memory_percent"]

            if name not in grouped_processes:
                grouped_processes[name] = {
                    "name": name,
                    "instances": 1,
                    "cpu": cpu,
                    "memory": memory
                }
            else:
                grouped_processes[name]["instances"] +=1
                grouped_processes[name]["cpu"] += cpu
                grouped_processes[name]["memory"] += memory
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes = list(grouped_processes.values())

    for process in processes:
        process["cpu"] = round(process["cpu"], 1)
        process["memory"] = round(process["memory"], 2)
    
    processes.sort(
        key=lambda p: p["memory"],
        reverse=True
    )

    return processes[:limit]

if __name__ == "__main__":
    for process in get_top_processes():
        print(process)