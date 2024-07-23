pkgname=polo
pkgver=1.0
pkgrel=1
pkgdesc="Polaris Polo Package manager/Utilities."
arch=('any')
license=('GPL')
source=()
md5sums=()
depends=('python' 'python-pip' 'python-gitpython' 'python-requests' 'python-pyzmq' 'flatpak' 'pacman-contrib')
install=polaris.install

package() {
    if [ -f "src/__pycache__" ]; then
        rm -rf "src/__pycache__"
    fi
    if [ -f "src/zmq" ]; then
        rm "src/zmq"
    fi
    if [ -f "src/keyboard" ]; then
        rm "src/keyboard"
    fi
    cd "../files"
    find . -type f -exec install -Dm644 {} "$pkgdir/{}" \;
    
    cd "../src"
    find . -type f -exec install -Dm755 {} "$pkgdir/usr/share/polaris/{}" \;
}