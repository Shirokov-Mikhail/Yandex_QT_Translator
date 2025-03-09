import io
import sys

from PyQt6 import uic
from yandex_cloud_ml_sdk import YCloudML
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QApplication, QPushButton, \
    QLabel, QLCDNumber, QCheckBox, QButtonGroup, QSpinBox, QDialog, QVBoxLayout, QTableWidgetItem, QWidget, \
    QFileDialog, QTableWidget, QTextEdit, QComboBox


# playsound("sound/pukane-4.mp3")

# 123
class Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('MainWindow.ui', self)
        self.logs = []
        self.inputText: QTextEdit
        self.outputText: QTextEdit
        self.Text_base: QTextEdit
        self.button: QPushButton
        self.models: QComboBox
        self.lan2: QComboBox

        self.button.clicked.connect(self.Gpt)

    def Gpt(self):
        try:
            modals = 'yandexgpt-lite'
            if self.lan2.currentText() == 'YaGPT-Pro':
                modals = 'yandexgpt'
            prompt = self.inputText.toPlainText()
            chel = self.inputText.toPlainText()
            messages = [
                {
                    "role": "system",
                    "text": f"{prompt}",
                },
                {
                    "role": "user",
                    "text": f"""{chel}""",
                },
            ]
            self.zapros(messages=messages, modals=modals)

        except OSError as e:
            print('ошибка ', e)
            self.logs.append('ошибка c системой')

    def zapros(self, messages, modals='yandexgpt-lite'):
        sdk = YCloudML(
            folder_id="b1g50fq74ab4fhhng89n",
            auth="t1.9euelZrIyZqTlceYiceLmZSelpeSzO3rnpWai4rKzpOclJLKyZvGzZSbk47l8_c_PEpB-e9jVVUR_d3z939qR0H572NVVRH9zef1656VmpeOjp6XlZCLm5bJyJLIy8-O7_zF656VmpeOjp6XlZCLm5bJyJLIy8-O.ARed2iVO00aMciC2niI6HrvSVbU3IefcXhwYaRr-CqSPUOEnpmKpLyp-Mq9Qq9C3ATW7NlfxtFOUyqn4gxUUAw",
        )

        result = (
            sdk.models.completions(modals).configure(temperature=1).run(messages)
        )

        for alternative in result:
            self.outputText.setText(alternative.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Translator()
    ex.show()
    sys.exit(app.exec())
