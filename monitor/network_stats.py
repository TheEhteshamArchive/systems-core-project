import psutil
import time


def get_network_stats():
    before = psutil.net_io_counters()

    time.sleep(1)

    after = psutil.net_io_counters()

    download_speed = (
        after.bytes_recv - before.bytes_recv
    ) / (1024 ** 2)

    upload_speed = (
        after.bytes_sent - before.bytes_sent
    ) / (1024 ** 2)

    return{
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),

        "total_received": round(
            after.bytes_recv / (1024 ** 3), 2
        ),

        "total_sent": round(
            after.bytes_sent / (1024 ** 3), 2
        )
    }

if __name__ == "__main__":
    print(get_network_stats())