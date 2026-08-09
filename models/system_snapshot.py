from dataclasses import dataclass

@dataclass
class SystemSnapshot:
    cpu: dict
    ram: float
    disk: float
    gpu: dict
    processes: list
    network: dict

    def __str__(self):
        output = []

        output.append("=== System Status ===")
        output.append("=== CPU ===")
        output.append(f"Usage: {self.cpu['usage']}%")
        output.append(f"Frequency: {self.cpu['frequency']} Mhz")
        output.append(f"Temperature: {self.cpu['temperature']}°C")
        output.append("=== ~~~ ===")
        output.append(f"Ram Usage: {self.ram}%")
        output.append(f"Disk Usage: {self.disk}%")

        output.append("")
        output.append("=== GPU ===")
        output.append(f"Name: {self.gpu['name']}")
        output.append(f"Usage: {self.gpu['gpu_usage']}%")
        output.append(f"VRAM: {self.gpu['vram_used']}MB / {self.gpu['vram_total']}MB")
        output.append(f"Temperature: {self.gpu['temperature']}°C")
        output.append("")
        output.append("=== Network ===")
        output.append(f"Download: {self.network['download']} MB/s")
        output.append(f"Upload: {self.network['upload']} MB/s")
        output.append(f"Total Received: {self.network['total_received']} GB")
        output.append(f"Total Sent: {self.network['total_sent']} GB")
        output.append("")
        output.append("=== Top Processess ===")

        for process in self.processes:
            output.append(
                f"{process['name']}: "
                f"CPU {process['cpu']}% | "
                f"RAM {process['memory']}%"
            )
        
        return "\n".join(output)