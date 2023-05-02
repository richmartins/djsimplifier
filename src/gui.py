#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6 import QtWidgets


class Gui(QtWidgets.QWidget):
    n = 0

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("DJSimplifier")
        # --------- Widgets ---------
        layout = QtWidgets.QVBoxLayout(self, self.add_url())

        # --------- Main layout  ---------
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(20)
        self.layout.addLayout(layout)

    def add_url(self) -> list:
        self.n += 1
        label_url = QtWidgets.QLabel(f"Url {self.n}")
        input_url = QtWidgets.QLineEdit()
        return [label_url, input_url]
