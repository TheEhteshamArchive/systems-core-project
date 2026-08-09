from pynvml import *

def get_gpu_stats():
    try:
        nvmlInit()

        gpu = nvmlDeviceGetHandleByIndex(0)

        name = nvmlDeviceGetName(gpu)
        utilization = nvmlDeviceGetUtilizationRates(gpu)
        memory = nvmlDeviceGetMemoryInfo(gpu)
        temperature = nvmlDeviceGetTemperature(
            gpu,
            NVML_TEMPERATURE_GPU
        )

        return {
            "name": name,
            "gpu_usage": utilization.gpu,
            "vram_used": round(memory.used/ 1024**2),
            "vram_total": round(memory.total / 1024**2),
            "temperature": temperature
        }

    except Exception as e:
        return{
            "error": str(0)
        }

if __name__ == "__main__":
    print(get_gpu_stats())