#!/usr/bin/python
import argparse
import os
import pcore
import tqdm

def get_device_size(device):
    statvfs = os.statvfs(device)
    return statvfs.f_blocks

# lil note about this function:
# fucking kill me now AAAAAAAAAAAAAAAAAAAAAAAAAAAA
def secure_wipe(dev):
    print("Removing the master boot record...")
    os.system(f"dd if=/dev/zero of={dev} bs=446 count=1")
    print("Wiping disk... (may take a while)")
    size = get_device_size(dev)
    with tqdm.tqdm(range(size * 4), unit="chunk") as tq:
        with open(dev, "wb") as dev_io:
            for __ in range(size):
                tq.update()
                dev_io.write(os.urandom(1))
        with open(dev, "wb") as dev_io:
            for __ in range(size):
                tq.update()
                dev_io.write(os.urandom(1))
        with open(dev, "wb") as dev_io:
            for __ in range(size):
                tq.update()
                dev_io.write(b'\x00')
        with open(dev, "wb") as dev_io:
            for __ in range(size):
                tq.update()
                dev_io.write(b'\x00')

# well ain't dat simpel
def rebuild_boot():
    print("Rebuilding boot info")
    os.system("mkinitcpio -P")
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")

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