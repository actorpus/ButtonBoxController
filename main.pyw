from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import threading
import sys
import serial
import time


class IconHandler(threading.Thread):
    """
    this is just to provide visual feedback that the script is running
    and can be disabled with right click context menu
    """
    def __init__(self, shutdown):
        super().__init__()

        self.shutdown = shutdown

        self.start()

    def run(self):
        def fq():
            app.quit()
            self.shutdown()
            sys.exit(0)

        app = QApplication([])
        app.setQuitOnLastWindowClosed(False)

        icon = QIcon("icon.png")

        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        tray.setToolTip("ButtonBox")

        menu = QMenu()

        hide_button = QAction("hide")
        hide_button.triggered.connect(lambda: tray.setVisible(False))
        menu.addAction(hide_button)

        quit_button = QAction("Quit")
        quit_button.triggered.connect(fq)
        menu.addAction(quit_button)

        tray.setContextMenu(menu)
        sys.exit(app.exec_())


IconHandler(lambda: print("shutdown func triggered"))


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

while True:
    v = arduino.readline()
    if v:
        key = int(v.strip().decode())

        if key == 1:
            print("1")

        elif key == 2:
            print("2")

        elif key == 3:
            print("3")

        elif key == 4:
            print("4")

        elif key == 5:
            print("5")

    time.sleep(0.1)
