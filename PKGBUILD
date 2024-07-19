pkgname=polo
pkgver=1.0
pkgrel=1
pkgdesc="Polaris Polo Package manager/Utilities."
arch=('any')
license=('GPL')
source=('src/' 'files/')
md5sums=('SKIP' 'SKIP')

package() {
    rm -rf "$srcdir/src/__pycache__"
    rm "$srcdir/src/zmq"
    rm "$srcdir/src/keyboard"
    cd "$srcdir/files"
    find . -type f -exec install -Dm644 {} "$pkgdir/{}" \;
    
    cd "$srcdir/src"
    find . -type f -exec install -Dm755 {} "$pkgdir/usr/share/polaris/{}" \;
}