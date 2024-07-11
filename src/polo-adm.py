#!/bin/python
import argparse
import os

def secure_wipe(dev):
    print(f"Securely wiping {dev}")
    print("This may take a while...")
    os.system(f"sudo bash -c 'dd if=/dev/urandom of={dev} status=progress'")
    os.system(f"sudo bash -c 'dd if=/dev/zero of={dev} status=progress'")

def rebuild_boot():
    print("Rebuilding boot info")
    os.system("sudo mkinitcpio -P")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")

def banner():
    print("polo-adm | Polaris Polo Admin Tools")
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
if __name__ == '__main__':
    main()