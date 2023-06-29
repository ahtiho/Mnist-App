from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.uic.properties import QtCore
from model import *
import numpy as np
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
from sys import exit
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Number recognization software'
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 500
        self.button = self.findChild(QPushButton, "pushButton")
        self.icon = "000005.jpg"
        self.createUI()


    def createUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.drawItems()

    def drawItems(self):
        #Add the image
        self.imageBG = QPixmap('Zara/000001.jpg')
        self.BG = QLabel("White")
        self.imageBG = self.imageBG.scaled(300, 300)
        self.BG.setPixmap(self.imageBG)
        self.BG.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.BG, 1, 0, 3, 3)

        #Add the text
        self.button = QPushButton("Find file")

        self.button.setStyleSheet("""
        "color: blue;"
                        "background-color: yellow;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
        """)

        self.button.clicked.connect(self.clicker)
        self.grid.addWidget(self.button, 6, 0, 3,3)





    def clicker(self):
        #self.text.setText('You clicked the button')
        filename = QFileDialog.getOpenFileName(self, 'Open Image', "", "All files (*.jpg)")
        if filename:
            self.imageBG = filename[0]
            self.BG.setPixmap(QPixmap(filename[0]).scaled(300,300))
            self.button.hide()
            self.button_other = QPushButton("Find other file")
            self.button_predict = QPushButton("Make the prediction!")
            self.button.setStyleSheet("""
            "color: blue;"
                        "background-color: yellow;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;"

                    """)

            self.button_other.clicked.connect(self.clicker)
            self.button_predict.clicked.connect(lambda: self.prediction(filename[0]))
            self.grid.addWidget(self.button_other, 8, 0, 3, 3)
            self.grid.addWidget(self.button_predict,6,0,3,3)



    def prediction(self, photo):
        photo = Image.open(photo)
        photo = tf.keras.utils.normalize(photo, axis=1)
        photo = np.reshape(photo, (28,28))
        photo = photo.flatten()
        photo = photo.reshape(1, 784)

        print(photo.shape)
        prediction = model.predict([photo])
        prediction = np.argmax(prediction)

        text = "The prediction for the number in the picture is senner {}".format(prediction)
        self.result = QLabel(text)
        self.grid.addWidget(self.result, 9, 0, 3, 3)

        self.button_other.hide()
        self.button_predict.hide()
        self.question = QLabel('Do you want to make another prediction?')
        self.yes = QPushButton('Yes')
        self.no = QPushButton('No')
        self.yes.clicked.connect(self.reset_ui)
        self.no.clicked.connect(exit)
        self.grid.addWidget(self.question, 6, 0, 3, 3)
        self.grid.addWidget(self.yes, 7, 0, 3, 3)
        self.grid.addWidget(self.no, 8, 0, 3, 3)



    def reset_ui(self):
            self.result.hide()
            self.yes.hide()
            self.no.hide()
            self.question.hide()
            self.clicker()