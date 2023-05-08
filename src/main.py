#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread, Signal

from gui import Gui

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    widget = Gui()
    widget.resize(600, 400)

    widget.show()
    sys.exit(app.exec())
