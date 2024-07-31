# IM MAKING FUCKIGN AUR AND NOONE CAN STOP ME!!!!!!!!!!!!!!!!!!!!!!!!!!
import requests
import subprocess
import os
from git import Repo
import sys
import glob

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
    results_aur_hack = list()
    if results_flathub != None:
        for result in results_flathub:
            if query in result["name"].lower() and "i18n" not in result["name"].lower():
                print(f"Flathub/Flatpak - {result["name"]}")
                print(f"description: {result['summary']}")
                print("")
    if results_pacman != None:
        for result in results_pacman:
            if query in result["pkgname"].lower() and "i18n" not in result["pkgname"].lower():
                results_aur_hack.append(result["pkgname"])
    if results_aur != None:
        for result in results_aur:
            if query in result["Name"].lower() and "i18n" not in result["Name"].lower() and result["Name"] not in results_aur_hack:
                print(f"Packages - {result["pkgname"]}")
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
        install(pkg, False, True)

def package_exists_pacrepos(package_name):
    try:
        # Run the pacman search command
        result = subprocess.run(
            ['pacman', '-Ss', package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the search returned results
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return

        # Split the output by lines
        lines = result.stdout.splitlines()
        
        # Check if the package is found in the official repos or Chaotic-AUR
        found = False
        for line in lines:
            if line.startswith(('core/', 'extra/', 'multilib/', 'chaotic-aur/')):
                found = True
                print(line)

        if not found:
            print(f"Package '{package_name}' not found in the repositories.")

    except FileNotFoundError:
        print("Error: 'pacman' command not found. Make sure it is installed and in your PATH.")

def install(package_name, stdin, aur_specific=False):
    # First, is this in normal pacrepos?
    if package_exists_pacrepos(package_name) and aur_specific != True:
        os.system(f"sudo pacman -S {package_name}")
        return
    # If not then keep going
    elif package_exists(package_name):
        pkgdir = f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}"
        if os.path.exists(f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}"):
            # fuck it, lazy solution and i don't wanna hear shit about it pull requesters
            os.system(f"rm -rf {os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        Repo.clone_from(f"{AUR_BASE_URL}/{package_name}.git", f"{os.path.expanduser('~')}/.polo/pkgs/{package_name}")
        subprocess.run(['makepkg', '-sc', '--noconfirm'], cwd=pkgdir)
        pattern = '*.pkg.tar.zst'
        files = glob.glob(f'{pkgdir}/{pattern}')

        if stdin == False:
            for file in files:
                subprocess.run(['sudo', 'pacman', '-U', file, '--noconfirm'], cwd=pkgdir)
        elif stdin == True:
            for file in files:
                subprocess.run(['sudo', '-S', 'pacman', '-U', file, '--noconfirm'], input=sys.stdin.read().encode(), cwd=pkgdir)    
    else:
        # so sad, too bad the package "ASDFMOVIEPLAYERSSSSSSSSSSSSS" doesn't exist
        print("Package not found")
        print("Nothing to do")