# IM MAKING FUCKIGN AUR AND NOONE CAN STOP ME!!!!!!!!!!!!!!!!!!!!!!!!!!
import requests
import subprocess
import os
from git import Repo
import sys

# da URL
AUR_BASE_URL = "https://aur.archlinux.org"
AUR_RPC_URL = f"{AUR_BASE_URL}/rpc/?v=5&type=search&arg="

def search_aur(query):
    url = f"{AUR_RPC_URL}{query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
    else: 
        results = None
    return results

def search_flathub(query):
    url = f"https://flathub.org/api/v1/apps/search/{query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
    else: 
        results = None
    return results

def search_pacman(query):
    url = f"https://archlinux.org/packages/search/json/?q={query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
    else:
        results = None
    return results

def search(query):
    results_flathub = search_flathub(query)
    results_aur = search_aur(query)
    results_pacman = search_pacman(query)
    if results_flathub != None:
        for result in results_flathub:
            if query in result["name"].lower() and "i18n" not in result["name"].lower():
                print(f"Flathub/Flatpak - {result["name"]}")
                print(f"description: {result['summary']}")
                print("")
    if results_aur != None:
        for result in results_aur:
            if query in result["Name"].lower() and "i18n" not in result["Name"].lower():
                print(f"AUR - {result["Name"]}")
                print(f"description: {result['Description']}")
                print("")
    if results_pacman != None:
        for result in results_pacman:
            if query in result["pkgname"].lower() and "i18n" not in result["pkgname"].lower():
                print(f"Pacman - {result["pkgname"]}")
                print(f"description: {result['pkgdesc']}")
                print("")
    results_num = len(results_pacman) + len(results_aur) + len(results_flathub)
    print(f"got {results_num} results.")

def netquery(package_name):
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
        install(pkg, True, True)

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

def install(package_name, stdin, aur_specific=False):
    # First, is this in normal pacrepos?
    if package_exists_pacrepos(package_name) and aur_specific != True:
        os.system(f"sudo pacman -S {package_name}")
        return
    # If not then keep going
    if package_exists(package_name):
        pkgdir = f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}"
        if os.path.exists(f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}"):
            # fuck it, lazy solution and i don't wanna hear shit about it pull requesters
            os.system(f"rm -rf {os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        Repo.clone_from(f"{AUR_BASE_URL}/{package_name}.git", f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        subprocess.run(['makepkg', '-sc', '--noconfirm'], cwd=pkgdir)
        if stdin == False:
            subprocess.run(['sudo', 'pacman', '-U', '*.pkg.tar.zst'], cwd=pkgdir)
        elif stdin == True:
            subprocess.run(['sudo', '-S', 'pacman', '-U', '*.pkg.tar.zst'], input=sys.stdin, cwd=pkgdir)    
    else:
        # so sad, too bad the package "ASDFMOVIEPLAYERSSSSSSSSSSSSS" doesn't exist
        print("Package not found")
        print("Nothing to do")