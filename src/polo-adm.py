#!/bin/python
import argparse
import os
import pcore
import psutil

def dskbytecpy_limitout(src, out):
    # Open the SRC and OUT devices
    src_io = open(src, "r")
    out_io = open(out, "w")
    # Get the output device size
    out_size = psutil.disk_usage(out)

    # Now write the SRC data to the OUT device.
    out_io.write(src_io.read(out_size))

def dskbytecpy(src, out):
    # Open the SRC and OUT devices
    src_io = open(src, "r")
    out_io = open(out, "w")

    # Now write the SRC data to the OUT device.
    out_io.write(src_io.read())

def secure_wipe(dev):
    print(f"Securely wiping {dev}")
    print("This may take a while...")
    dskbytecpy_limitout("/dev/zero", dev)
    dskbytecpy_limitout("/dev/urandom", dev)
    dskbytecpy_limitout("/dev/zero", dev)

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