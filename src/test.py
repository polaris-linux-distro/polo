import requests

def search_aur(query):
    url = f"https://aur.archlinux.org/rpc/?v=5&type=search&arg={query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
    else: 
        results = None
    return results

def search_flathub(query):
    url = f"https://flathub.org/api/v2/search?query={query}"
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
            print(f"Flathub/Flatpak - {result["name"]}")
            print(f"description: {result['summary']}")
    if results_aur != None:
        for result in results_aur:
            print(f"AUR - {result["Name"]}")
            print(f"description: {result['Description']}")
    if results_pacman != None:
        for result in results_pacman:
            print(f"Pacman - {result["pkgname"]}")
            print(f"description: {result['pkgdesc']}")

search("org.fedoraproject.MediaWriter")