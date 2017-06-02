import sys
import rectangle_form

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout(self)

        # radio button definition
        radioBody = QRadioButton("Body", self)
        radioTail = QRadioButton("Tail", self)
        radioNose = QRadioButton("Nose", self)
        splitterRadio = QSplitter(Qt.Horizontal)
        splitterRadio.addWidget(radioBody)
        splitterRadio.addWidget(radioTail)
        splitterRadio.addWidget(radioNose)

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
        splitterButton.addWidget(splitterRadio)
        splitterButton.addWidget(addButton)
        splitterButton.addWidget(removeButton)
        splitterButton.addWidget(saveButton)

        # Splitter vertical
        splitter1 = QSplitter(Qt.Vertical)
        self.textedit=QTextEdit()
        splitter1.addWidget(splitterButton)
        splitter1.addWidget(self.textedit)
        #splitter1.setSizes([100,200])


        #### premier essai avec QFrame
        # self.bottom = QFrame()
        # self.bottom.setFrameShape(QFrame.StyledPanel)
        #######

        ##################### creation d'une sous fenetre qui ajoute du text   ref2
        #self.mdi = QMdiArea()
        #self.sub = QMdiSubWindow()
        #self.sub.setWidget(QTextEdit())
        #self.sub.setWindowTitle("subwindow test")
        #self.mdi.addSubWindow(self.sub)

        ###############################    first version with number of splitter equal to the number of rectangle added  ref1
        #self.splitter2 = QSplitter(Qt.Vertical)
        #self.splitter2.addWidget(splitter1)

        #  element for the sub part ref 2
        # self.splitter2.addWidget(self.sub)
        # self.splitter2.addWidget(self.bottom)

        # hbox.addWidget(self.splitter2)    ref1

        ###################### third try with QTextObjectInterface object
        self.drawarea = QStackedWidget(self)

        self.hbox.addWidget(splitter1)
        self.hbox.addWidget(self.drawarea)
        self.setLayout(self.hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        # connection des events
        addButton.clicked.connect(self.addButtonFunc)
        saveButton.clicked.connect(self.saveButtonFunc)
        removeButton.clicked.connect(self.removeButtonFunc)

        self.setGeometry(200, 200, 900, 900)
        self.setWindowTitle('QSplitter demo')
        self.show()

    def addButtonFunc(self):
        """action started after the press of add button"""
        self.rectAdd = rectangle_form.RectangleForm()
        rectAddTex = "a new rectangle form"
        #self.sub.addWidget(rectAdd)           ref2
        #self.splitter2.addWidget(rectAdd)     ref1
        # self.hbox.addWidget(rectAdd)                      basic behavior reference
        self.drawarea.addWidget(self.rectAdd)
        self.textedit.append(rectAddTex)
        print ("inside of the addButton function")

    def saveButtonFunc(self):
        """action started after the press of add button"""
        print ("inside of the saveButton function")

    def removeButtonFunc(self):
        """action started after the press of add button"""
        print ("inside of the removeButton function")

    def mousePressEvent(self, event):
        """select the nearest current object"""
        if event.button() == Qt.LeftButton:
            self.rectAdd.mouseDown(self)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()