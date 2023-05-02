#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class Gui(QtWidgets.QWidget):
    n = 1

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("DJSimplifier")
        plus_btn_container = QtWidgets.QHBoxLayout()
        layout = QtWidgets.QHBoxLayout()
        download_btn_container = QtWidgets.QHBoxLayout()

        # --------- Widgets ---------
        plus_btn = QtWidgets.QPushButton("+")
        plus_btn.clicked.connect(self.handle_plus_btn)
        plus_btn_container.addWidget(plus_btn)

        label_url = QtWidgets.QLabel(f"Url {self.n}")
        input_url = QtWidgets.QLineEdit()
        layout.addWidget(label_url)
        layout.addWidget(input_url)

        download_btn = QtWidgets.QPushButton("Download")
        download_btn.clicked.connect(self.handle_download_btn)
        download_btn_container.addWidget(download_btn)

        # --------- Main layout  ---------
        self.main_container = QtWidgets.QGridLayout(self)
        self.main_container.addLayout(
            plus_btn_container, 1, 1, alignment=Qt.AlignRight)
        self.main_container.addLayout(layout, 2, 1, alignment=Qt.AlignHCenter)
        self.main_container.addLayout(
            download_btn_container, 3, 1, alignment=Qt.AlignRight)

    def handle_plus_btn(self) -> None:
        print("here")
        new_layout = QtWidgets.QHBoxLayout()
        urls_widgets = self.add_url()

        new_layout.addWidget(urls_widgets[0])
        new_layout.addWidget(urls_widgets[1])

        # get the layout and row count
        layout = self.layout()
        last_row = layout.rowCount() - 1

        # add the widgets to the new row
        layout.addWidget(new_layout, last_row, 0)

    def handle_download_btn(self) -> None:
        ...

    def add_url(self) -> list:
        self.n += 1
        label_url = QtWidgets.QLabel(f"Url {self.n}")
        input_url = QtWidgets.QLineEdit()
        return [label_url, input_url]
