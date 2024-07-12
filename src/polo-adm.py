#!/bin/python
import argparse
import os
import pcore
import psutil

def get_device_size(device):
    # Get the size of the device in bytes using `blockdev` command
    statvfs = os.statvfs(device)
    return statvfs.f_frsize * statvfs.f_blocks

def secure_wipe(dev):
    print(f"Securely wiping {dev}")
    print("This may take a while...")
    # Convert size from MB to bytes
    size_bytes = get_device_size(dev) * 1024 * 1024
    
    with open(dev, 'wb') as disk:
        for _ in range(size_bytes):
            # Write a random byte to the disk
            disk.write(os.urandom(1))


def rebuild_boot():
    print("Rebuilding boot info")
    os.system("sudo mkinitcpio -P")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")

def banner():
    print(f"polo-adm | Polaris Polo Admin Tools | {pcore.VERSION}")
    print("---------------------------------------------------")

def main():
    banner()
    parser = argparse.ArgumentParser(description="The admin tools for Polaris GNU/Linux.")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Secure wipe command
    secure_wipe_parser = subparsers.add_parser('secure-wipe', help='Securely overwrites the data of a disk, removing any trace of data. (may take a few hours!)')
    secure_wipe_parser.add_argument('disk', type=str, help='The disk to wipe')

    # Rebuild-boot command
    rebuild_boot_parser = subparsers.add_parser('rebuild-boot', help='Rebuilds the GRUB config, as well as the initramfs.')

    args = parser.parse_args()

    if args.command == "rebuild-boot":
        rebuild_boot()
    elif args.command == "secure-wipe":
        secure_wipe(args.disk)
    else:
        parser.print_help()
if __name__ == '__main__':
    main()