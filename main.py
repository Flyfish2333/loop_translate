import socket
import sys
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QObject
from PySide2.QtWidgets import QApplication

from Methods.TranslateThread import TranslateThread
from Ui import resources


class MainWindow(QQuickView, QObject):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.cycles = mainView.findChild(QObject, "cycles")
        self.translateText = mainView.findChild(QObject, "translateText")
        self.layoutText = mainView.findChild(QObject, "layoutText")

    def doStart(self):
        cycles = self.cycles.property("text")
        translateText = self.translateText.property("text")
        try:
            cycles = int(cycles)
            self.translateThread = TranslateThread(translateText, cycles)
            self.translateThread.signal.connect(self.translateThreadBack)
            self.translateThread.start()
        except Exception as e:
            self.layoutText.setProperty("text", str(e))
        finally:
            return

    def translateThreadBack(self, msg):
        self.layoutText.setProperty("text", msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('qrc:/main.qml')
    mainView = engine.rootObjects()[0]
    mainView.show()
    context = MainWindow()
    context.mainView = mainView
    engine.rootContext().setContextProperty("main", context)
    doStart = mainView.findChild(QObject, "doStart")
    doStart.clicked.connect(context.doStart)
    app.exec_()