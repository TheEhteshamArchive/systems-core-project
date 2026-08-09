import ollama

def ask_ai(snapshot):
    prompt=f"""
    You are a Linux system monitoring assistant.

    Analyze this system snapshot:

    CPU:
    Usage: {snapshot.cpu['usage']}%
    Frequency: {snapshot.cpu['frequency']} Mhz
    Temperature: {snapshot.cpu['temperature']}°C

    RAM:
    {snapshot.ram}%

    Disk:
    {snapshot.disk}%

    GPU:
    Name: {snapshot.gpu['name']}
    GPU Utilization: {snapshot.gpu['gpu_usage']}%
    VRAM:
    {snapshot.gpu['vram_used']}MB / {snapshot.gpu['vram_total']}MB
    Temperature:
    {snapshot.gpu['temperature']}°C

    Top Processes:
    {snapshot.processes}

    Important interpretation rules:
    - Always mention CPU, RAM, Disk, and GPU.
    - Identify unusual resource usage.
    - Keep analysis concise.
    - Only mention issues that are actually unusual.
    

    TEMPERATURE:
    - CPU and GPU temperatures below 80°C are normal.
    - 80-90°C is warm and worth monitoring.
    - Above 90°C is concerning.
    - never describe temperatures below 80°C as hot, high, elevated, or dangerous.
    - A temperature around 40°C is cool and completely normal.
    - Temperature around 30-60°C are cool and normal.
    - Do not describe temperatures below 80°C as elevated.

    GPU:
    - GPU Utilization is seperate from CPU usage.
    - Do not say the GPU is consuming CPU time.
    - VRAM usage refers only to the GPU memory.
    - GPU utilization below 80% is normal.
    - Only descrive GPU utilization as high if it is above 80% and sustained.
    - GPU utilization alone is not a problem unless combined with high temperature or performance issues.
    - GPU utilization is not a problem by itself.
    - GPU usage between 0-80% is normal.
    - Only warn about GPU usage if it is above 90% for a sustained period AND temperatures are high.
    - VRAM usage below 80% of total VRAM is normal.
    - 1-4GB VRAM usage on a 16GB GPU is normal.
    - Do not warn about VRAM usage unless it is close to the GPU's capacity.
    VRAM CALCULATION:
    - Calculate VRAM percentage as: vram_used / vram_total * 100.
    - Example: 1000MB used out of 16000MB is approximately 6%.
    - Never call VRAM usage high unless it is above 80% of total VRAM.

    MEMORY:
    - Ram usage percentage refers to system RAM.
    - VRAM usage refers only to GPU memory.
    - Do not confuse process RAM usage with VRAM.
    - Process memory values are RAM percentages, not VRAM.
        Recommendations:
        - Do not give generic maintenance advice.
        - Do not recommend cooling improvements unless temperaturewws are actually high.
        - Avoid repeating general PC maintenance tips.
        - Only provide recommendations based on detected problems
        VRAM:
        - Calculate VRAM usage from the provided values.
        - Do not call VRAM usage high unless it is above 80% of total VRAM.
        - 1-4GB of VRAM usage on a 16GB GPU is normal.
        RAM:
        - Do not recommend RAM upgrades unless system RAM usage is consistently above 85%.
    
    NETWORK:
    - Mention network activity if download or upload speed is unusually high.
    - 0 MB/s is normal when there is no active network usage.
    - Do not warn about low network activity
    
    PROCESS ANALYSIS:
    - Judge process usage based on total system resources,
    - A process using a large percentage of available RAM is not automatically a problem if overall RAM usage is low.
    - Only warn about processes if they cause noticable system resource pressure.

    PROCESS VALUES:
    - Process CPU usage may exceed 100% because linux reports usage across multiple CPU cores.
    - A process above 100% CPU does not automatically mean a problem.
    - Consider total system CPu usage before reporting a CPU warning
    - Conisder high CPU usage relative to the process, not just the percentage alone.
    - Mention processes only if they are unusually consuming resources
    - Only warn about a process if it causes high overall CPU usage, performance issues, or sustained resource pressure.

    STATUS:
    - Overall system status should be based primarily on total CPU, RAM, GPU, temperature, and disk usage.
    - Individual processes should not change the status to WARNING unless they significantly affect the system.
    - Overall status must be based on actual problems.
    - A healthy temperature always overrides high utilization warnings.
    - Do not mark the system as WARNING if CPU/GPU temperatures are normal.
    - Do not create hypothetical future problems.
    
    Provide a short report with:

    1. Overall Status:
        - Healthy / Warning / Critical
    
    2. Warnings:
        - Only include real issues.

    3. Recommendations:
        - Give practical suggestions if needed.

    Keep the entire response under 100 words.
    Use short bullet points.
    Avoid explanations unless there is an actual problem.
    Avoid repeating that the system is healthy multiple times.
    If there are no warnings, simply say "No issues detected."
    Do not add generic advice when no action is needed
    OUTPUT LENGTH:
    - Keep the analysis under 5 sentences unless a serious warning exists.
    - Do not explain every normal metric.
    - Only explain unusual findings.
    """

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
