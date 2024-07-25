import os

aur_list = [
	'pcre4',
    'aic94xx-firmware',
    'ast-firmware',
    'wd719x-firmware',
    'upd72020x-fw',
    'zramd',
	'xvkbd',
	'ptyxis',
	'qlipper'
]

os.system("plymouthd")
os.system("plymouth --show-splash")

os.system("useradd -m -s /bin/zsh builder")
os.system("echo 'y' | passwd builder -s")
for pkg in aur_list:
	os.system(f"echo y | sudo -u builder /usr/bin/python /usr/share/polaris/polo-pkg.py install {pkg}")
os.system("userdel -f builder")

os.system("plymouth --quit")
os.system("reboot")