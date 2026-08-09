from monitor.system_stats import get_system_stats
from monitor.gpu_stats import get_gpu_stats
from monitor.process_stats import get_top_processes
from monitor.cpu_stats import get_cpu_stats 
from monitor.system_stats import get_system_stats
from monitor.network_stats import get_network_stats

from models.system_snapshot import SystemSnapshot

class SystemCollector:

    def collect(self):
        stats = get_system_stats()

        return SystemSnapshot(
            cpu = get_cpu_stats(),
            ram = stats["ram"],
            disk = stats["disk"],
            gpu = get_gpu_stats(),
            processes = get_top_processes(),
            network = get_network_stats()
        )