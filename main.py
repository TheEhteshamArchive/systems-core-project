from monitor.system_stats import get_system_stats
from ai.ollama_client import ask_ai
from collectors.system_collector import SystemCollector

import time


def main():

    collector = SystemCollector()

    while True:
        snapshot = collector.collect()

        print(snapshot)

        analysis = ask_ai(snapshot)

        print("\n=== AI Analysis ===")
        print(analysis)

        print("\nWaiting...\n")
        time.sleep(10)


if __name__ == "__main__":
    main()