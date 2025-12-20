import psutil

def check_cpu(cpu_threshold):
    current_cpu = psutil.cpu_percent(interval=1)
    print("\n[CPU]")
    print("threshold for cpu:",cpu_threshold)
    print("CPU USAGE %:", current_cpu)
    if current_cpu > cpu_threshold:
        print("CPU: Danger")
    else:
        print("CPU: Safe")

def check_memory(memory_threshold):
    current_memory = psutil.virtual_memory().percent
    print("\n[MEMORY]")
    print("threshold for memory:",memory_threshold)
    print("Current Memory %:", current_memory)
    if current_memory > memory_threshold:
        print("Memory: Danger")
    else:
        print("Memory: Safe")

def check_disk(disk_threshold):
    current_disk = psutil.disk_usage("/").percent
    print("\n[DISK]")
    print("threshold for Disk:",disk_threshold)
    print("Current Disk %:", current_disk)
    if current_disk > disk_threshold:
        print("threshold for disk:",disk_threshold)
        print("Disk: Danger")
    else:
        print("Disk: Safe")

cpu_threshold = int(input("Enter the CPU threshold: "))
memory_threshold = int(input("Enter the Memory threshold: "))
disk_threshold = int(input("Enter the Disk threshold: "))

print("\n System Health ")
check_cpu(cpu_threshold)
check_memory(memory_threshold)
check_disk(disk_threshold)
