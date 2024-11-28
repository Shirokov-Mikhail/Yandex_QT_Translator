import io
import sys
import pandas as pd
import csv
# from stock_exchange import starter
from PyQt6 import uic
import requests
import sqlite3
from PyQt6.QtGui import QPixmap
import pyglet
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QApplication, QPushButton, \
    QLabel, QLCDNumber, QCheckBox, QButtonGroup, QSpinBox, QDialog, QVBoxLayout, QTableWidgetItem, QWidget, \
    QFileDialog, QTableWidget, QTextEdit, QComboBox


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        try:
            try:
                uic.loadUi('ui/Dialog.ui', self)
                self.pushButton: QPushButton
                self.pushButton.clicked.connect(self.user_test)
                self.login: QLineEdit
                self.pasword: QLineEdit
                self.errorLog = []
                self.returner = [5, False, self.errorLog]

            except FileNotFoundError:
                print('неприятности с Dialog.ui')
        except ValueError:
            print('ошибка ValueError')

    def user_test(self):
        try:
            if self.login.isEnabled() and self.pasword.isEnabled():
                try:
                    self.get_result('bd.sqlite', self.login.text(), self.pasword.text())
                except FileNotFoundError:
                    print('bd не найдена')
                    self.errorLog.append('bd не найдена')
                try:
                    sound = pyglet.media.load('sound/pukane-4.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('ошибка музыки музыка не найдена')
                    self.errorLog.append('ошибка музыки музыка не найдена')
            else:
                raise f'Ошибка экстренной блокировки нужно обратиться к админам'
        except ValueError as E:
            self.errorLog.append(E)

    def get_result(self, name, user, password):
        try:
            try:
                con = sqlite3.connect(name)
                cur = con.cursor()
                try:
                    result = cur.execute("""SELECT name, password FROM main""").fetchall()
                except Exception:
                    print('ошибка запроса')
                    self.errorLog.append('ошибка запроса')
                base_users = [i[0] for i in result]
                base_password_id = [i[1] for i in result]
                try:
                    base_password = [i[0] for i in cur.execute("""SELECT password FROM passwords""").fetchall()]
                    if user in base_users and password in base_password:
                        if base_password_id[base_users.index(user)] - 1 == base_password.index(password):
                            self.returner = [base_users.index(user), True, self.errorLog]
                            self.close()
                except Exception:
                    print('оштбка запроса')
                    self.errorLog.append('оштбка запроса')
                con.commit()
                con.close()
            except FileNotFoundError:
                print('bd не найдена')
                self.errorLog.append('bd не найдена')
        except ValueError as e:
            print('ошибка в get result', e)
            self.errorLog.append(f'ошибка в get result {e}')

    def rezelter(self):
        try:
            return self.returner
        except Exception:
            return [0, False, self.errorLog]
