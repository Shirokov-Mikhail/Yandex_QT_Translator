import io
import sys
import pandas as pd
import csv
# from stock_exchange import starter
from PyQt6 import uic
import requests
import sqlite3
import os
from PyQt6.QtGui import QPixmap
import pyglet
import json
from PyQt6.QtCore import Qt
from SecondWindow import SecondWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QApplication, QPushButton, \
    QLabel, QLCDNumber, QCheckBox, QButtonGroup, QSpinBox, QDialog, QVBoxLayout, QTableWidgetItem, QWidget, \
    QFileDialog, QTableWidget, QTextEdit, QComboBox


# playsound("sound/pukane-4.mp3")
class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        try:
            try:
                try:
                    uic.loadUi('ui/MainWindow.ui', self)
                except FileNotFoundError:
                    self.logs.append('Main файл потерян')
                    print('Main файл потерян')
                self.logs = []
                self.inputText: QTextEdit
                self.outputText: QTextEdit
                self.inputText.setEnabled(False)
                self.outputText.setEnabled(False)
                self.translate: QPushButton
                self.translate.setEnabled(True)
                self.back: QPushButton
                self.login_button: QPushButton
                self.back.setEnabled(False)
                self.lan1: QComboBox
                self.lan2: QComboBox
                self.lan2.setEnabled(False)
                self.lan1.setEnabled(False)
                print(self.lan1.currentText())
                self.free_rr: QLCDNumber
                self.starter()
                self.translate.clicked.connect(self.trenslator)
                self.back.clicked.connect(self.smenter)
                self.inputText.toPlainText()
            except SyntaxError:
                self.logs.append('ошибка синтаксиса начало')
                print('ошибка синтаксиса')
        except ValueError:
            self.logs.append(ValueError)
            print(ValueError)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_M:
            self.statusBar().showMessage(*self.logs)

    def starter(self):
        try:
            self.second_window = SecondWindow()
            self.second_window.exec()
            self.enterCom(self.second_window.rezelter())
        except ValueError as s:
            self.logs.append(ValueError)
            print(ValueError)

    def on_combobox_change(self, value):
        self.label.setText(value)

    def back_function(self, id):
        try:
            try:
                con = sqlite3.connect('bd.sqlite')
                cur = con.cursor()
                result = cur.execute("""SELECT num FROM main""").fetchall()
                base = [i[0] for i in result]
                num = base[id]
                print(base)
                self.updeter(num)
                con.commit()
                con.close()
            except SystemError:
                self.updeter(5)
                self.logs.append('удивительно что она сработала нате 5 для теста')
                print('удивительно что она сработала нате 5 для теста')
        except OSError:
            self.logs.append('Ищите ршибку у чебя у меня проблем нет')
            print('Ищите ршибку у чебя у меня проблем нет')

    def updeter(self, number):
        try:
            self.free_rr.display(f'{number}')
        except Exception:
            self.logs.append('ошибка updater')
            print('ошибка updater')

    def updeter_bd(self, id):
        con = sqlite3.connect('bd.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""UPDATE main SET num = num - 1
WHERE id = {id + 1}""").fetchall()
        con.commit()
        con.close()
        self.back_function(id)

    def trenslator(self, tr='1'):
        API_KEY = 'ключ'
        URL = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        print(self.inputText.toPlainText().split('\n'))
        trans = 'ru-ru'
        try:
            if self.lan1.currentText() == 'Англиский':
                trans = 'en' + trans[2:]
            elif self.lan1.currentText() == 'Немецкий':
                trans = 'de' + trans[2:]
            elif self.lan1.currentText() == 'Французкий':
                trans = 'fr' + trans[2:]
            elif self.lan1.currentText() == 'Белорусский':
                trans = 'be' + trans[2:]
            elif self.lan1.currentText() == 'Русский':
                trans = 'ru' + trans[2:]
        except ValueError as e:
            self.logs.append('ошибка lan 1')
            print('ошибка lan 1')

        try:
            if self.lan2.currentText() == 'Англиский':
                trans = trans[:-2] + 'en'
            elif self.lan2.currentText() == 'Немецкий':
                trans = trans[:-2] + 'de'
            elif self.lan2.currentText() == 'Французкий':
                trans = trans[:-2] + 'fr'
            elif self.lan2.currentText() == 'Белорусский':
                trans = trans[:-2] + 'be'
            elif self.lan2.currentText() == 'Русский':
                trans = trans[:-2] + 'ru'
        except ValueError as e:
            self.logs.append('ошибка lan 2')
            print('ошибка lan 2')
        text_to_translate = self.inputText.toPlainText()
        IAM_TOKEN = 't1.9euelZqKjZyZlI7PjZeKiYmWk5rHx-3rnpWai4rKzpOclJLKyZvGzZSbk47l8_dDN2NF-e8iJlV9_d3z9wNmYEX57yImVX39zef1656VmsbJipzOjMyJmpWJyMyWipuL7_zF656VmsbJipzOjMyJmpWJyMyWipuL.z6dTcv0DeQA16ta47r61tJumxeEN-C6sx7yE7rdMl-y9nvbu8qJxuZFUIZn3-dVWwUhu8yFfhD5aqgHyRGnICw'
        folder_id = 'b1g50fq74ab4fhhng89n'
        target_language = 'en'
        texts = ["Hello", "World"]


        body = {
            "targetLanguageCode": target_language,
            "texts": text_to_translate,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }
        self.zapros(headers=headers, body=body)

        # response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        #                          json=body,
        #                          headers=headers
        #                          )

        try:
            sound = pyglet.media.load('sound/pukane-4.mp3', streaming=False)
            sound.play()
        except FileNotFoundError:
            print('проблемы с музыкой музыка не найдена')
        pyglet.app.run()

    def zapros(self, headers, body):
        try:
            try:
                response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                         json=body,
                                         headers=headers)
                text_inp = str(response.text)  # Преобразуем строку в объект Python
                data = json.loads(text_inp)  # Преобразование строки JSON в словарь Python
                text_value = data["translations"][0]["text"]  # Получение значения text
                self.updeter_bd(self.id)
                print(text_value)
                try:
                    sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('проблемы с музыкой музыка не найдена')
                    self.logs.append('проблемы с музыкой музыка не найдена')
            except Exception:
                raise ValueError
            try:
                sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                sound.play()
            except FileNotFoundError:
                print('проблемы с музыкой музыка не найдена')
                self.logs.append('проблемы с музыкой музыка не найдена')

        except ValueError:
            try:
                try:  # ошибка в body
                    IAM_TOKEN = 't1.9euelZqKjZyZlI7PjZeKiYmWk5rHx-3rnpWai4rKzpOclJLKyZvGzZSbk47l8_dDN2NF-e8iJlV9_d3z9wNmYEX57yImVX39zef1656VmsbJipzOjMyJmpWJyMyWipuL7_zF656VmsbJipzOjMyJmpWJyMyWipuL.z6dTcv0DeQA16ta47r61tJumxeEN-C6sx7yE7rdMl-y9nvbu8qJxuZFUIZn3-dVWwUhu8yFfhD5aqgHyRGnICw'
                    folder_id = 'b1g50fq74ab4fhhng89n'
                    target_language = 'en'
                    body = {
                        "targetLanguageCode": target_language,
                        "texts": self.inputText.toPlainText(),
                        "folderId": folder_id,
                    }
                    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                             json=body,
                                             headers=headers)
                    text_inp = str(response.text)  # Преобразуем строку в объект Python
                    data = json.loads(text_inp)  # Преобразование строки JSON в словарь Python
                    text_value = data["translations"][0]["text"]  # Получение значения text
                    print(text_value)
                    self.updeter_bd(self.id)
                except Exception:
                    try:  # Ошибка не в body
                        IAM_TOKEN = 't1.9euelZqKjZyZlI7PjZeKiYmWk5rHx-3rnpWai4rKzpOclJLKyZvGzZSbk47l8_dDN2NF-e8iJlV9_d3z9wNmYEX57yImVX39zef1656VmsbJipzOjMyJmpWJyMyWipuL7_zF656VmsbJipzOjMyJmpWJyMyWipuL.z6dTcv0DeQA16ta47r61tJumxeEN-C6sx7yE7rdMl-y9nvbu8qJxuZFUIZn3-dVWwUhu8yFfhD5aqgHyRGnICw'
                        headers = {
                            "Content-Type": "application/json",
                            "Authorization": "Bearer {0}".format(IAM_TOKEN)
                        }
                        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                                 json=body,
                                                 headers=headers)
                        text_inp = str(response.text)  # Преобразуем строку в объект Python
                        data = json.loads(text_inp)  # Преобразование строки JSON в словарь Python
                        text_value = data["translations"][0]["text"]  # Получение значения text
                        print(text_value)
                        self.updeter_bd(self.id)
                    except Exception:
                        print('Fatality Error')
                        self.logs.append('Fatality Error')
                        raise OSError
            except OSError:
                print('ошибка системы ищите проблему сами')
                self.logs.append('ошибка системы ищите проблему сами')

    def enterCom(self, value=[False]):
        try:
            try:
                try:
                    if value[1]:
                        self.lan1.setEnabled(True)
                        self.lan2.setEnabled(True)
                        self.back.setEnabled(True)
                        self.translate.setEnabled(True)
                        self.inputText.setEnabled(True)
                        self.outputText.setEnabled(True)
                        self.back_function(value[0])
                        self.id = value[0]
                    else:
                        raise SystemError
                except SystemError:
                    self.logs.append('ошибка Value неправельной перезапуск')
                    print('ошибка Value неправельной перезапуск')
                    self.starter()
            except ValueError:
                self.inputText.setText('Опа Ошибочка вышла но ничего мы с ней справмся вы же своих не боросаете')
                self.outputText.setText(
                    self.trenslator('Опа Ошибочка вышла но ничего мы с ней справмся вы же своих не боросаете'))
        except SyntaxError:
            self.logs.append('ошибка синтаксиса')
            print('ошибка синтаксиса')

    def smenter(self):
        try:
            try:
                try:
                    sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('проблемы с музыкой музыка не найдена')
                    self.logs.append('проблемы с музыкой музыка не найдена')

                text2 = self.inputText.toPlainText()
                self.inputText.setText(self.outputText.toPlainText())
                self.outputText.setText(text2)
            except SystemError:
                self.logs.append('System')
                print('System')
        except SyntaxError:
            self.logs.append('Syntax')
            print('Syntax')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
