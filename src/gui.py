#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from djsimplifier import DjSimplifer


class Gui(QtWidgets.QWidget):
    n: int = 0
    urls: list = []

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("DJSimplifier")
        plus_btn_container = QtWidgets.QHBoxLayout()
        self.url_container = QtWidgets.QVBoxLayout()
        download_btn_container = QtWidgets.QHBoxLayout()

        # --------- Widgets ---------
        plus_btn = QtWidgets.QPushButton("+")
        plus_btn.clicked.connect(self.handle_plus_btn)
        plus_btn_container.addWidget(plus_btn)

        urls_widgets = self.add_url()
        self.url_container.addWidget(urls_widgets[0])
        self.url_container.addWidget(urls_widgets[1])

        download_btn = QtWidgets.QPushButton("Download")
        download_btn.clicked.connect(self.handle_download_btn)
        download_btn_container.addWidget(download_btn)

        # --------- Main layout  ---------
        self.main_container = QtWidgets.QGridLayout(self)
        self.main_container.addLayout(
            plus_btn_container, 1, 1, alignment=Qt.AlignRight)
        self.main_container.addLayout(
            self.url_container, 2, 1, alignment=Qt.AlignHCenter)
        self.main_container.addLayout(
            download_btn_container, 3, 1, alignment=Qt.AlignRight)

    def handle_plus_btn(self) -> None:
        urls_widgets = self.add_url()

        self.url_container.addWidget(urls_widgets[0])
        self.url_container.addWidget(urls_widgets[1])

    def handle_download_btn(self) -> None:

        save_path = self.ask_save_path()

        # choose were to save
        dj_simplifier = DjSimplifer(self.urls, save_path)
        try:
            dj_simplifier.download()
        except Exception as e:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText(str(e))
            msgBox.exec_()
            return False

    def add_url(self) -> list:
        self.n += 1
        id_url: int = self.n
        label_url = QtWidgets.QLabel(f"Url {self.n}")
        input_url = QtWidgets.QLineEdit()
        self.urls.append({id_url: ""})

        input_url.textEdited.connect(
            lambda text: self.handle_url_change(text, id_url))
        return [label_url, input_url]

    def handle_url_change(self, txt: str, id_url: int) -> None:
        [self.urls[i].update({id_url: txt}) for i in range(
            len(self.urls)) if id_url in self.urls[i]]

    def ask_save_path(self):
        return str(
            QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select where to save directory")
        )
