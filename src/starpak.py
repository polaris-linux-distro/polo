import os
from PySide6 import QtCore, QtWebEngineWidgets, QtGui, QtWidgets

# Constants
SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
VERSION = 1.0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QtCore.QSize(800, 600))
        self.setWindowTitle("Starpak")
        self.setWindowIcon(QtGui.QIcon(":/qt-project.org/styles/commonstyle/images/right-32.png"))
        self.webEngine = QtWebEngineWidgets.QWebEngineView(self)
        self.setCentralWidget(self.webEngine)
    def load(self, file):
        file_url = QtCore.QUrl.fromLocalFile(file)
        self.webEngine.load(QtCore.QUrl(file_url))

def main():
    os.chdir(SCRIPTDIR)
    app = QtWidgets.QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.load(f"{SCRIPTDIR}/starpak-ui/index.html")
    app.exec()

main()