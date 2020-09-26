from PySide2.QtCore import Signal, QThread

from Methods import Translate


class TranslateThread(QThread):
    signal = Signal(str)

    def __init__(self, translateText, cycles):
        super(TranslateThread, self).__init__()
        self.translateText = translateText
        self.cycles = cycles

    def run(self):
        try:
            result = self.translateText
            for i in range(self.cycles):
                result = Translate.translate(result, "en", "ja")
                result = Translate.translate(result, "ja", "zh-CN")
                result = Translate.translate(result, "zh-CN", "en")
                msg = "The " + str(i + 1) + " times translate:\n" + result
                self.signal.emit(msg)
        except Exception as e:
            self.signal.emit(str(e))