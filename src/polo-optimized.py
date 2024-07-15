import os
import re

sys_block_path = "/sys/block"

def get_disk_type(disk):
    path = f"{sys_block_path}/{disk}/queue/rotational"
    try:
        with open(path, 'r') as file:
            rotational = file.read().strip()
            if rotational == '0':
                return 'SSD'
            elif rotational == '1':
                return 'HDD'
    except FileNotFoundError:
        return "Disk not found or not a valid block device."

    return "Unknown"

def get_non_removable_disks():
    disks = []
    
    for disk in os.listdir(sys_block_path):
        removable_path = os.path.join(sys_block_path, disk, "removable")
        if os.path.isfile(removable_path):
            with open(removable_path, 'r') as file:
                removable = file.read().strip()
                if removable == '0':
                    if disk != re.compile("zram.") or disk != re.compile("dm-.") or disk != re.compile("loop."):
                        disks.append(disk)
    
    return disks

def main():
    disks = get_non_removable_disks()
    for disk in disks:
        disk_type = get_disk_type(disk)
        if disk_type == "SSD":
            os.system(f"echo mq-deadline > /sys/block/{disk}/queue/scheduler")
        elif disk_type == "HDD":
            os.system(f"echo bfq > /sys/block/{disk}/queue/scheduler")
        elif disk_type == "Unknown":
            print("Disk type unknown. Skipping!")

main()