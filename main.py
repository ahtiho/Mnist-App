from PyQt6.QtCore import Qt, QSize, QAbstractTableModel
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate
import sys

from window_img import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_img = window()
    window_img.show()
    sys.exit(app.exec())
