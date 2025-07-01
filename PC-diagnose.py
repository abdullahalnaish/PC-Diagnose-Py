import platform
import psutil
import socket
import shutil

def get_os_info():
    print("=== Operating System Info ===")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print()

def get_cpu_info():
    print("=== CPU Info ===")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
    print()

def get_memory_info():
    print("=== Memory Info ===")
    memory = psutil.virtual_memory()
    print(f"Total: {round(memory.total / (1024**3), 2)} GB")
    print(f"Available: {round(memory.available / (1024**3), 2)} GB")
    print(f"Used: {round(memory.used / (1024**3), 2)} GB")
    print(f"Percentage: {memory.percent}%")
    print()

def get_disk_info():
    print("=== Disk Info ===")
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {round(total / (1024**3), 2)} GB")
    print(f"Used: {round(used / (1024**3), 2)} GB")
    print(f"Free: {round(free / (1024**3), 2)} GB")
    print(f"Usage Percentage: {used / total * 100:.2f}%")
    print()

def get_network_info():
    print("=== Network Info ===")
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    except Exception as e:
        print(f"Could not retrieve IP address: {e}")
    print()

def main():
    print("PC Diagnose Tool - Basic System Report\n")
    get_os_info()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_network_info()

if __name__ == "__main__":
    main()
