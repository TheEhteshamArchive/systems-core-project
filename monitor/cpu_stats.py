import psutil

def get_cpu_stats():
    cpu_usage = psutil.cpu_percent(interval=1)

    frequency = psutil.cpu_freq()

    temps = psutil.sensors_temperatures()

    temperatures = None

    if temps:
        for name, entries in temps.items():
            if entries:
                temperature = entries[0].current
                break
        
    return {
        "usage": cpu_usage,
        "frequency": round(frequency.current, 2) if frequency else None,
        "temperature": temperature
    }

if __name__ == "__main__":
    print(get_cpu_stats())