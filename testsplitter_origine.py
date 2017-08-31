#! usr/bin/env python3

import sys
import rectangle_form

#from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout(self)
        # button definition and associated splitter
        addButton = QPushButton('Add', self)
        addButton.setToolTip('add a new slice')
        addButton.setFixedSize(110, 30)
        removeButton = QPushButton('Remove', self)
        removeButton.setToolTip('remove a slice')
        removeButton.setFixedSize(110, 30)
        saveButton = QPushButton('Save', self)
        saveButton.setToolTip('Save a slice')
        saveButton.setFixedSize(110, 30)

        splitterButton = QSplitter(Qt.Horizontal)
        splitterButton.addWidget(addButton)
        splitterButton.addWidget(removeButton)
        splitterButton.addWidget(saveButton)
        # add the draw part
        # self.PaintPanel = QPainter()
        # self.PaintPanel.end()
        self.DrawingFrame = QStackedWidget(self)
        # self.DrawingFrame.insertWidget(0, self.PaintPanel)


        # connection des events
        addButton.clicked.connect(self.addButtonFunc)

        self.hbox.addWidget(splitterButton)
        self.setGeometry(200, 200, 900, 900)
        self.setWindowTitle('QSplitter demo')
        self.show()

    def addButtonFunc(self):
        """action started after the press of add button"""
        self.rectAdd = rectangle_form.RectangleForm()
        self.DrawingFrame.addWidget(self.rectAdd)
        print ("inside of the addButton function")



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
