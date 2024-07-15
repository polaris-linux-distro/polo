# IM MAKING FUCKIGN AUR AND NOONE CAN STOP ME!!!!!!!!!!!!!!!!!!!!!!!!!!
import requests
import subprocess
import os
from git import Repo

# da URL
AUR_BASE_URL = "https://aur.archlinux.org"
AUR_RPC_URL = f"{AUR_BASE_URL}/rpc/?v=5&type=search&arg="

def search(package_name):
    # no, we're not fucking googling AUR packages.
    if package_exists(package_name) != True:
        if package_exists_pacrepos(package_name):
            print(f"{package_name} exists.")
        else:
            print(f"{package_name} does not exist.")
    else:
        print(f"{package_name} exists.")

def package_exists(package_name):
    # same comment as get_installed_aur_packages basically - these comments are not in order.
    response = requests.get(AUR_RPC_URL + package_name)
    if response.status_code == 200:
        result = response.json()
        if result['resultcount'] > 0:
            return True
    return False

def get_installed_aur_packages():
    # do.. do you need a comment here? its just gives you the installed packages.
    aur_packages = list()
    output = subprocess.check_output(['sudo', 'pacman', '-Qm'])
    packages = output.decode('utf-8').splitlines()
    aur_packages_bfp = [pkg.split()[0] for pkg in packages]
    for pkg in aur_packages_bfp:
        if package_exists(pkg):
             aur_packages.append(pkg)
    return aur_packages

def check_for_updates():
    # i have no idea- it just checks updates
    packages = get_installed_aur_packages()
    aur_info_url = f"{AUR_BASE_URL}/rpc/?v=5&type=info&arg[]="
    for package in packages:
        aur_info_url += f"{package}&arg[]="
    response = requests.get(aur_info_url)
    updates = []
    if response.status_code == 200:
        result = response.json()
        for pkg in result['results']:
            local_version = subprocess.check_output(['sudo', 'pacman', '-Qm', pkg['Name']]).decode('utf-8').split()[1]
            if pkg['Version'] != local_version:
                updates.append(pkg['Name'])
    return updates

def update():
    # checks for updates (see above for code, please comment if you can actually comment it!) and then updates any packages that need to be updated
    # if you actually needed that comment, stop coding now and retake school
    updates = check_for_updates()
    if not updates:
        print("All AUR packages are up-to-date.")
        return
    
    print("Updating the following AUR packages:")
    for pkg in updates:
        print(f"- {pkg}")

    allpkg = str()
    for pkg in updates:
        # just call once, very efficent
        allpkg += pkg
    os.system(f"sudo pacman -R {allpkg} --noconfirm")
    
    for pkg in updates:
        install(pkg, True)

def package_exists_pacrepos(package_name):
    # yet another self explanatory one...
    url = f"https://archlinux.org/packages/search/json/?name={package_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return True
        else:
            return False
    else:
        return False

def install(package_name, aur_specific=False):
    # First, is this in normal pacrepos?
    if package_exists_pacrepos(package_name) and aur_specific != True:
        os.system(f"sudo pacman -S {package_name}")
        return
    # If not then keep going
    if package_exists(package_name):
        oldcwd = os.getcwd()
        if os.path.exists(f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}"):
            # fuck it, lazy solution and i don't wanna hear shit about it pull requesters
            os.system(f"rm -rf {os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        Repo.clone_from(f"{AUR_BASE_URL}/{package_name}.git", f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        os.chdir(f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        subprocess.run(['makepkg', '-si'])
        os.chdir(oldcwd)
    else:
        # so sad, too bad the package "ASDFMOVIEPLAYERSSSSSSSSSSSSS" doesn't exist
        print("Package not found")
        print("Nothing to do")