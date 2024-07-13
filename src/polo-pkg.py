#!/usr/bin/python
import os
import argparse
import pcore

# this library was a pain in the ass, so don't expect sanity in any of these code comments.
import aur

# i need to replace this... ever. pls rember
# f = open("/etc/polaris/type", "r")
# ostype = f.read().strip()
# i did rember

# not the game, moron
def pacman(args):
    os.system(f"bash -c 'sudo pacman {args} --noconfirm'")

# packages but superflat world
def flatpak(args):
    os.system(f"bash -c '/usr/bin/flatpak {args}'")

# does this work? maybe lemme test one sec
# 30 secs later it works
# very nice
def cacheclear():
    os.system("bash -c 'sudo paccache -rk0'")
    for pkg in os.listdir(f"{os.path.expanduser('~')}/.polo/pkgs/"):
        os.system(f"rm -rf {os.path.expanduser('~')}/.polo/pkgs/{pkg}")

def update():
    #ohhhhhhhhhhhh boy
    cacheclear()
    os.system("sudo pacman -Syyu")
    aur.update()
    if pcore.ostype == "cli":
        flatpak("update")

def banner():
    print(f"polo-pkg | Polaris Polo Package Manager | {pcore.VERSION}")
    print("---------------------------------------------------")

def main():
    banner()
    parser = argparse.ArgumentParser(description="The package manager for Polaris GNU/Linux.")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Update command
    subparsers.add_parser('update', help='Update the package database')

    # Install command
    install_parser = subparsers.add_parser('install', help='Install a package')
    install_parser.add_argument('package', type=str, help='The package to install')
    install_parser.add_argument('-f', '--flatpak', action='store_true', help='Install from Flatpak')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a package')
    remove_parser.add_argument('package', type=str, help='The package to remove')
    remove_parser.add_argument('-f', '--flatpak', action='store_true', help='Remove from Flatpak')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search for a package')
    search_parser.add_argument('package', type=str, help='The package to search for')
    search_parser.add_argument('-f', '--flatpak', action='store_true', help='Search for a package from Flatpak')

    # Build command
    build_parser = subparsers.add_parser('build', help='Build a package from source')

    args = parser.parse_args()

    # Perfectly sane... just ignore the piles of if statements

    if args.command == 'update':
        update()
    elif args.command == 'install':
        if args.flatpak:
            if pcore.ostype == "svr":
                print("Flatpak is not supported on Polaris Server.")
            elif pcore.ostype == "cli":
                flatpak(f"install {args.package}")
        elif args.flatpak != True:
            aur.install(args.package)
    elif args.command == 'remove':
        if args.flatpak:
            if pcore.ostype == "svr":
                print("Flatpak is not supported on Polaris Server.")
            elif pcore.ostype == "cli":
                flatpak(f"remove {args.package}")
        elif args.flatpak != True:
            pacman(f"-R {args.package}")
    elif args.command == 'search':
        if args.flatpak:
            if pcore.ostype == "svr":
                print("Flatpak is not supported on Polaris Server.")
            elif pcore.ostype == "cli":
                flatpak(f"search {args.package}")
        elif args.flatpak != True:
            aur.search(args.package)
    elif args.command == "build":
        os.system("makepkg -si")
    else:
        parser.print_help()

    # Remember the garbage collector, dumbass.
    # No, don't, we switched to another method (sys.conf)
    # f.close()

# nae nae
if __name__ == '__main__':
    main()
