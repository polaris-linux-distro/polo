import os

aur_list = [
    'aic94xx-firmware',
    'ast-firmware',
    'wd719x-firmware',
    'upd72020x-fw',
    'zramd',
	'xvkbd',
	'ptyxis',
	'qlipper'
]

os.system("useradd -m -s /bin/zsh polarislinuxtempbuilder")
os.system("usermod -aG wheel polarislinuxtempbuilder")
os.system("echo 'y' | passwd polarislinuxtempbuilder -s")
for pkg in aur_list:
	os.system(f"echo y | sudo -u builder /usr/bin/python /usr/share/polaris/polo-pkg.py install {pkg} -s")
os.system("userdel -rf polarislinuxtempbuilder")

os.system("systemctl disable polaris-postinst")
os.system("systemctl mask polaris-postinst")
os.system("systemctl enable lightdm")
os.system("reboot")