import os
import datetime
from typing import List

def collect_system_info() -> dict:
    """Collect system information."""
    system_info = {
        "current_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "current_time": datetime.datetime.now().strftime("%H:%M:%S"),
        "operating_system": os.name,
        "cpu_count": os.cpu_count(),
        "memory_usage": f"{os.sysconf_names['SC_PAGE_SIZE'] * os.sysconf_names['SC_PHYS_PAGES'] / (1024.0 ** 3):.2f} GB"
    }
    return system_info

def check_disk_usage() -> List[dict]:
    """Check disk usage for each partition."""
    disk_usage = []
    for partition in os.disk_partitions():
        usage = os.disk_usage(partition.mountpoint)
        disk_usage.append({
            "partition": partition.device,
            "total_size": f"{usage.total / (1024.0 ** 3):.2f} GB",
            "used_size": f"{usage.used / (1024.0 ** 3):.2f} GB",
            "free_size": f"{usage.free / (1024.0 ** 3):.2f} GB",
            "percentage": f"{usage.percent}%"
        })
    return disk_usage

def generate_report(system_info: dict, disk_usage: List[dict]) -> str:
    """Generate maintenance report."""
    report = f"System Information:\n"
    report += f"-------------------\n"
    report += f"Current Date: {system_info['current_date']}\n"
    report += f"Current Time: {system_info['current_time']}\n"
    report += f"Operating System: {system_info['operating_system']}\n"
    report += f"CPU Count: {system_info['cpu_count']}\n"
    report += f"Memory Usage: {system_info['memory_usage']}\n\n"
    report += f"Disk Usage:\n"
    report += f"-----------\n"
    for disk in disk_usage:
        report += f"Partition: {disk['partition']}\n"
        report += f"Total Size: {disk['total_size']}\n"
        report += f"Used Size: {disk['used_size']}\n"
        report += f"Free Size: {disk['free_size']}\n"
        report += f"Percentage: {disk['percentage']}\n\n"
    return report

def main():
    system_info = collect_system_info()
    disk_usage = check_disk_usage()
    report = generate_report(system_info, disk_usage)
    print(report)

if __name__ == "__main__":
    main()