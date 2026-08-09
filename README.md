# Systems Core

A local AI-powered Linux system monitoring and event automation system.

## Overview

Systems core is a modular Linux system assitant designed to monitor hardware and software resources in real t ime and use a locally hosted LLM to analyze system behavior.

The project combines system-level monitoring, hardware telemetry, process analysis, networking data, and local AI inference into a single system.

## Features

- CPU usage, frequency and temperature monitoring
- RAM and disk monitoring
- NVIDIA GPU utilization, VRAM and temperature monitoring
- Network upload/download monitoring
- Process-level CPU and RAM monitoring
- Continuous system monitoring
- Local AI analysis using Ollama
- Modular monitoring architecture
- System snapshot abstraction

## Architecture

```text
Linux System
     │
     ▼
System Collectors
     │
     ├── CPU
     ├── RAM
     ├── Disk
     ├── GPU
     ├── Network
     └── Processes
     │
     ▼
SystemSnapshot
     │
     ▼
Ollama
     │
     ▼
AI Analysis
```

## Technologies

- Python
- Linux
- psutil
- NVIDIA GPU monitoring
- Ollama
- LLM inference
- Git

## Current Status

The project is currently in active development.

The current version can collect system telemetry continuously and provide local AI-powered analysis of the system state.

## Planned Features

- Historical system data
- Trend detection
- Anomaly detection
- Event logging
- Structured AI decisions
- Safe automated system actions
- Graphical dashboard
- Automated testing

## Why I built this

I wanted to explore the intersection of Linux system programming, hardware monitoring, software architecture and local AI.

Rather than building a simple chatbot, I wanted to create an AI system that can interact with and understand the environment in which it is running.

## Project Structure
```text
systems-core/
├── ai/
├── collectors/
├── monitor/
├── models/
├── tools/
├── main.py
├── requirements.txt
└── README.md
```
## Running

Clone the repository and install the dependencies:
```bash
git clone https://github.com/TheEhteshamArchive/systems-core-project
cd systems-core

python -m venv venv
source venv/bin/activate.fish

pip install -r requirements.txt
```

Install and configure Ollama seperately, then run:
```bash
python main.py
```
Or Run main.py inside your IDE of choice.

## Development

This project is actively developed and new functionality is being added incrementally.

