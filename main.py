import io
import sys
import pandas as pd
import csv
# from stock_exchange import starter
from PyQt6 import uic
import requests
import sqlite3
import os
from PyQt6.QtGui import QPixmap, QIcon
import pyglet
import json
from PyQt6.QtCore import Qt
from SecondWindow import SecondWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QApplication, QPushButton, \
    QLabel, QLCDNumber, QCheckBox, QButtonGroup, QSpinBox, QDialog, QVBoxLayout, QTableWidgetItem, QWidget, \
    QFileDialog, QTableWidget, QTextEdit, QComboBox


# playsound("sound/pukane-4.mp3")
class Fatality_error(QDialog):
    def __init__(self):
        super().__init__()
        try:
            try:
                uic.loadUi('ui/Fatality_EROR.ui', self)
                self.pushButton: QPushButton
                self.lineEdit: QLineEdit
                self.pushButton.clicked.connect(self.smena)
                self.setWindowTitle('Окно для смены IAM')
                try:
                    icon_pixmap = QPixmap('logo/logo.jpg')  # Замените на путь к вашей иконке
                    icon = QIcon(icon_pixmap)
                    self.setWindowIcon(icon)
                except FileNotFoundError:
                    print('logo не определенно')
            except FileNotFoundError:
                print('неприятности с Fatality_EROR.ui')
        except ValueError:
            print('ошибка ValueError')

    def smena(self):
        try:
            self.close()
            try:
                sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                sound.play()
            except FileNotFoundError:
                print('проблемы с музыкой музыка не найдена')
            return self.lineEdit.text()
        except Exception:
            print('ошибибка')


class Translator(QMainWindow):
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
                self.setWindowTitle('QT пререводчик')
                self.translate: QPushButton
                self.translate.setEnabled(True)
                self.back: QPushButton
                self.login_button: QPushButton
                self.back.setEnabled(False)
                self.lan2: QComboBox
                self.lan2.setEnabled(False)
                self.smena = False
                self.free_rr: QLCDNumber
                self.starter()
                self.translate.clicked.connect(self.trenslator)
                self.back.clicked.connect(self.smenter)
                self.inputText.toPlainText()
                try:
                    icon_pixmap = QPixmap('logo/logo.jpg')  # Замените на путь к вашей иконке
                    icon = QIcon(icon_pixmap)
                    self.setWindowIcon(icon)
                except FileNotFoundError:
                    print('logo не определенно')
                    self.logs.append('logo не определенно')
                self.IAM = 't1.9euelZrNl4-SnM6Mi5OOmo-RnZaKye3rnpWai4rKzpOclJLKyZvGzZSbk47l8_cIDU9F-e9pWmJd_N3z90g7TEX572laYl38zef1656VmsuSjYmRxpOMzZuckouPm8rM7_zF656VmsuSjYmRxpOMzZuckouPm8rM.72Ij6KwJ1LvL3OfIW0ImTNToANputc5pGGzlJT1j6kyiGNzf-u9C3H5CulGjovcqb65kWCGIbe2w2FUxmopXAA'
            except SyntaxError:
                self.logs.append('ошибка синтаксиса начало')
                print('ошибка синтаксиса')
        except ValueError:
            self.logs.append(ValueError)
            print(ValueError)

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key.Key_J:
                try:
                    sound = pyglet.media.load('sound/pukane-4.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('ошибка музыки музыка не найдена')
                    self.logs.append('проблемы с музыкой музыка не найдена')
                self.Fatality_error = Fatality_error()
                self.Fatality_error.exec()
                print(self.Fatality_error.smena())
                self.IAM = self.Fatality_error.smena()
        except Exception:
            print('ОШИБКА СМЕНЫ IAM НЕВОЗМОЖНО')
            self.logs.append('ОШИБКА СМЕНЫ IAM НЕВОЗМОЖНО')
        try:
            if event.key() == Qt.Key.Key_M:
                try:
                    sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('проблемы с музыкой музыка не найдена')
                    self.logs.append('проблемы с музыкой музыка не найдена')
                if len(self.logs) == 0:
                    self.statusBar().showMessage('Ошибок нет')
                else:
                    self.statusBar().showMessage(*self.logs)
        except Exception:
            print('ОШИБКА КОНСОЛИ НЕВОЗМОЖНО')
            self.statusBar().showMessage('ОШИБКА КОНСОЛИ НЕВОЗМОЖНО')

    def starter(self):
        try:
            self.second_window = SecondWindow()
            self.second_window.exec()
            self.enterCom(self.second_window.rezelter())
        except ValueError as s:
            self.logs.append(ValueError)
            print(ValueError)

    def back_function(self, id):
        try:
            try:
                con = sqlite3.connect('bd.sqlite')
                cur = con.cursor()
                result = cur.execute("""SELECT num FROM main""").fetchall()
                base = [i[0] for i in result]
                print(base)
                print(id)
                num = base[id]
                print(base)
                if num <= 0:
                    return True
                else:
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
        try:
            con = sqlite3.connect('bd.sqlite')
            cur = con.cursor()
            result = cur.execute(f"""UPDATE main SET num = num - 1
            WHERE id = {id + 1}""").fetchall()
            con.commit()
            con.close()
            if self.back_function(id):
                raise ValueError
        except ValueError:
            return True

    def trenslator(self):
        try:
            print(self.inputText.toPlainText().split('\n'))
            target_language = 'en'
            try:
                if self.lan2.currentText() == 'Англиский':
                    target_language = 'en'
                elif self.lan2.currentText() == 'Немецкий':
                    target_language = 'de'
                elif self.lan2.currentText() == 'Французкий':
                    target_language = 'fr'
                elif self.lan2.currentText() == 'Белорусский':
                    target_language = 'be'
                elif self.lan2.currentText() == 'Русский':
                    target_language = 'ru'
            except ValueError as e:
                self.logs.append('ошибка lan 2')
                print('ошибка lan 2')
            text_to_translate = self.inputText.toPlainText()
            IAM_TOKEN = self.IAM
            folder_id = 'b1g50fq74ab4fhhng89n'
            body = {
                "targetLanguageCode": target_language,
                "texts": text_to_translate,
                "folderId": folder_id,
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(IAM_TOKEN)
            }
            try:
                self.zapros(headers=headers, body=body)
            except ValueError as e:
                print(e)
            try:
                sound = pyglet.media.load('sound/pukane-4.mp3', streaming=False)
                sound.play()
            except FileNotFoundError:
                print('ошибка музыки музыка не найдена')
                self.logs.append('проблемы с музыкой музыка не найдена')
            pyglet.app.run()
        except OSError as e:
            print('ошибка ', e)
            self.logs.append('ошибка c системой')

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
                self.outputText.setText(text_value)
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
                    IAM_TOKEN = 't1.9euelZrNl4-SnM6Mi5OOmo-RnZaKye3rnpWai4rKzpOclJLKyZvGzZSbk47l8_cIDU9F-e9pWmJd_N3z90g7TEX572laYl38zef1656VmsuSjYmRxpOMzZuckouPm8rM7_zF656VmsuSjYmRxpOMzZuckouPm8rM.72Ij6KwJ1LvL3OfIW0ImTNToANputc5pGGzlJT1j6kyiGNzf-u9C3H5CulGjovcqb65kWCGIbe2w2FUxmopXAA'
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
                    self.outputText.setText(text_value)
                    if self.updeter_bd(self.id):
                        raise BaseException
                    else:
                        self.updeter_bd(self.id)
                except Exception:
                    try:  # Ошибка не в body
                        IAM_TOKEN = 't1.9euelZrNl4-SnM6Mi5OOmo-RnZaKye3rnpWai4rKzpOclJLKyZvGzZSbk47l8_cIDU9F-e9pWmJd_N3z90g7TEX572laYl38zef1656VmsuSjYmRxpOMzZuckouPm8rM7_zF656VmsuSjYmRxpOMzZuckouPm8rM.72Ij6KwJ1LvL3OfIW0ImTNToANputc5pGGzlJT1j6kyiGNzf-u9C3H5CulGjovcqb65kWCGIbe2w2FUxmopXAA'
                        folder_id = 'b1g50fq74ab4fhhng89n'
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
                        self.outputText.setText(text_value)
                        self.updeter_bd(self.id)
                    except Exception:
                        print('Fatality Error')
                        self.logs.append('Fatality Error')
                        raise OSError
            except OSError:
                print('ошибка системы ищите проблему сами')
                self.logs.append('ошибка системы ищите проблему сами')
                return ValueError('уничтожение')

    def enterCom(self, value=[None, False]):
        try:
            try:
                try:
                    if value[1]:
                        self.lan2.setEnabled(True)
                        self.back.setEnabled(True)
                        self.translate.setEnabled(True)
                        self.inputText.setEnabled(True)
                        self.outputText.setEnabled(True)
                        self.back_function(value[0])
                        self.id = value[0]
                        self.logs += value[2]
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
    ex = Translator()
    ex.show()
    sys.exit(app.exec())
