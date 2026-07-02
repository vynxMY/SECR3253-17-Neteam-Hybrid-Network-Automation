#!/usr/bin/env python3

import socket
import subprocess
from datetime import datetime


def run_command(command):
    """Execute a shell command and return its output."""
    return subprocess.check_output(command, shell=True, text=True).strip()


print("=" * 60)
print("        Linux System Monitoring")
print("=" * 60)

# Hostname
print(f"\nHostname: {socket.gethostname()}")

# Current Date and Time
print(f"Current Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# CPU Usage
cpu = run_command(
    "top -bn1 | grep 'Cpu(s)' | awk '{print 100 - $8 \"%\"}'"
)
print(f"\nCPU Usage: {cpu}")

# Memory Usage
memory = run_command(
    "free -h | awk '/Mem:/ {print $3 \" / \" $2}'"
)
print(f"Memory Usage: {memory}")

# Disk Usage
disk = run_command(
    "df -h / | awk 'NR==2 {print $3 \" / \" $2 \" (\" $5 \")\"}'"
)
print(f"Disk Usage: {disk}")

# Logged-in Users
print("\nLogged-in Users:")
print(run_command("who"))

# Top 5 CPU Processes
print("\nTop 5 Processes by CPU Usage")
print("-" * 50)
print(f"{'PID':<8}{'PROCESS':<25}{'CPU (%)':>10}")
print("-" * 50)
# Aligning the Process ID 
output = run_command("ps -eo pid,comm,%cpu --sort=-%cpu | head -6")
lines = output.splitlines()[1:]  # Skip the header

for line in lines:
    parts = line.split(None, 2)
    if len(parts) == 3:
        pid, process, cpu = parts
        print(f"{pid:<8}{process:<25}{cpu:>10}")