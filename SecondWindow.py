import io
import sys
import pandas as pd
import csv
# from stock_exchange import starter
from PyQt6 import uic
import requests
import sqlite3
from PyQt6.QtGui import QPixmap, QIcon
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
                self.label: QLabel
                self.label_2: QLabel
                self.new_btn: QPushButton
                self.new_btn.clicked.connect(self.new_user)
                self.registrator = False
                self.errorLog = []
                self.returner = [5, False, self.errorLog]
                self.setWindowTitle('Вход')
                try:
                    icon_pixmap = QPixmap('logo/logo.jpg')  # Замените на путь к вашей иконке
                    icon = QIcon(icon_pixmap)
                    self.setWindowIcon(icon)
                except FileNotFoundError:
                    print('неприятности с logo')
                    self.errorLog.append('неприятности с logo')
            except FileNotFoundError:
                print('неприятности с Dialog.ui')
                self.errorLog.append('неприятности с Dialog.ui')
        except ValueError:
            print('ошибка ValueError')
            self.errorLog.append('ошибка ValueERROr')

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

    def new_user(self):
        if self.registrator == False:
            try:
                self.label.setText('Ведите логин для регистрации и нажмите + еще раз')
                self.label_2.setText('Ведите пароль для регистрации и нажмите + еще раз')
                self.registrator = True
            except Exception:
                print('ошибка в 1 секторе')
                self.errorLog.append('ошибка в 1 секторе')
        else:
            try:
                con = sqlite3.connect('bd.sqlite')
                cur = con.cursor()
                all_login_id = [int(i[0]) for i in cur.execute("""SELECT id FROM main""").fetchall()]
                all_password_id = [int(i[0]) for i in cur.execute("""SELECT id FROM passwords""").fetchall()]
                all_logins = [i[0] for i in cur.execute("""SELECT name FROM main""").fetchall()]
                all_paswords = [i[0] for i in cur.execute("""SELECT password FROM passwords""").fetchall()]
                try:
                    if self.pasword.text() in all_paswords:
                        id = all_paswords.index(self.pasword.text())
                    else:
                        new_pass = f"""INSERT INTO passwords VALUES ({max(all_password_id) + 1},'{self.pasword.text()}')
                                                                             """
                        id = max(all_password_id) + 1
                        cur.execute(new_pass)
                except Exception:
                    print('ошибка в pass')
                    self.errorLog.append('ошибка в pass при регистрации')
                try:
                    if self.login.text() in all_logins:
                        self.label.setText('Логин не подходит')
                    else:
                        new_login = f"""INSERT INTO main VALUES ({max(all_login_id) + 1},'{self.login.text()}', {id}, 5)
                                                             """
                        cur.execute(new_login)

                except Exception:
                    print('ошибка в login')
                    self.errorLog.append('ошибка в login при регистрации')
                con.commit()
                con.close()
                self.returner = [max(all_login_id), True, self.errorLog]
                try:
                    sound = pyglet.media.load('sound/translate_true.mp3', streaming=False)
                    sound.play()
                except FileNotFoundError:
                    print('проблемы с музыкой музыка не найдена')
                    self.errorLog.append('проблемы с музыкой музыка не найдена')
                self.close()
            except Exception:
                print('супер ошибка в системе и везде')
                self.errorLog.append('супер ошибка в системе и везде')