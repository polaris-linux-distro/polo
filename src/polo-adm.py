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
    print("Rebuilding bootloader...")
    os.system("mkinitcpio -P")
    os.system(open("/etc/limine_upgrade_command", 'r').read())

def banner():
    print(f"polo-adm | Polaris Polo Admin Tools | {pcore.VERSION}")
    print("---------------------------------------------------")

def useradd(user):
    os.system(f"useradd -m {user}")
    os.system(f"passwd {user}")

def groupadd(user, group):
    os.system(f"usermod -aG {group} {user}")

def grouprem(user, group):
    os.system(f"usermod -rG {group} {user}")

def userdel(user):
    os.system(f"userdel -f -r {user}")

def usershellchange(user, shell):
    os.system(f"usermod -s {shell} {user}")


def main():
    banner()
    parser = argparse.ArgumentParser(description="The admin tools for Polaris GNU/Linux.")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Secure wipe command
    secure_wipe_parser = subparsers.add_parser('secure-wipe', help='Securely overwrites the data of a disk, removing any trace of data. (may take a few hours!)')
    secure_wipe_parser.add_argument('disk', type=str, help='The disk to wipe')

    # Rebuild-boot command
    rebuild_boot_parser = subparsers.add_parser('rebuild-boot', help='Reinstalls Limine, as well as rebuilding the initramfs.')

    # Useradd command
    useradd_parser = subparsers.add_parser('user.add', help='Adds a new user.')
    useradd_parser.add_argument('user', type=str, help='The user to add.')

    # Groupadd command
    groupadd_parser = subparsers.add_parser('user.groupadd', help='Appends a group to a user.')
    groupadd_parser.add_argument('group', type=str, help='The group to add the user to.')
    groupadd_parser.add_argument('user', type=str, help='The user to add the group to.')

    # Groupremove command
    grouprem_parser = subparsers.add_parser('user.grouprem', help='Removes a group from a user.')
    grouprem_parser.add_argument('group', type=str, help='The group to remove the user from.')
    grouprem_parser.add_argument('user', type=str, help='The user to remove the group from.')

    # Userdel command
    userdel_parser = subparsers.add_parser('user.delete', help='Removes a user.')
    userdel_parser.add_argument('user', type=str, help='The user to remove')

    # User shellchange command
    shellchange_parser = subparsers.add_parser('user.shellchange', help="Change a user's shell.")
    shellchange_parser.add_argument('shell', type=str, help='The shell to change to.')
    shellchange_parser.add_argument('user', type=str, help='The user that you want to get their shell changed.')

    args = parser.parse_args()

    if args.command == "rebuild-boot":
        rebuild_boot()
    elif args.command == "secure-wipe":
        secure_wipe(args.disk)
    elif args.command == "user.add":
        useradd(args.user)
    elif args.command == "user.groupadd":
        groupadd(args.user, args.group)
    elif args.command == "user.grouprem":
        grouprem(args.user, args.group)
    elif args.command == "user.delete":
        userdel(args.user)
    elif args.command == "user.shellchange":
        usershellchange(args.user, args.shell)
    else:
        parser.print_help()
if __name__ == '__main__':
    main()