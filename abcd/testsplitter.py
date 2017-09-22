# systeme class
import sys
import logging

# UI class
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
# switch to pyqt5
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets


# personnal class
import abcd.forms.rectangle_form
import abcd.RenderAreaWidget
import abcd.Reconciliation



class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.__bodySize = [10, 10, 70, 60]

    def initUI(self):
        self.hbox = QtWidgets.QHBoxLayout(self)

        # radio button definition
        self.radioBody = QtWidgets.QRadioButton("Body", self)
        self.radioTail = QtWidgets.QRadioButton("Tail", self)
        self.radioNose = QtWidgets.QRadioButton("Nose", self)
        splitterRadio = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitterRadio.addWidget(self.radioBody)
        splitterRadio.addWidget(self.radioTail)
        splitterRadio.addWidget(self.radioNose)
        self.sizeSlider = self.sliderCreation(min=0.5, max=3, value=1, interval=0.5)

        #self.halfSize = QRadioButton("Half", self)
        #self.normalSize = QRadioButton("Normal", self)/home/renault/.local/share/virtualenvs/abcd-oF17S63F/bin/activate
        #self.doubleSize = QRadioButton("Double", self)
        #splitterRadio2 = QSplitter(Qt.Horizontal)
        #splitterRadio2.addWidget(self.halfSize)
        #splitterRadio2.addWidget(self.normalSize)
        #splitterRadio2.addWidget(self.doubleSize)

        # button definition and associated splitter
        addButton = QtWidgets.QPushButton('Add', self)
        addButton.setToolTip('add a new slice')
        addButton.setFixedSize(110, 30)

        removeButton = QtWidgets.QPushButton('Remove', self)
        removeButton.setToolTip('remove a slice')
        removeButton.setFixedSize(110, 30)
        saveButton = QtWidgets.QPushButton('Save', self)
        saveButton.setToolTip('Save a slice')
        saveButton.setFixedSize(110, 30)
        loadButton = QtWidgets.QPushButton('Load', self)
        loadButton.setToolTip('Load a config file')
        loadButton.setFixedSize(110, 30)


        splitterButton = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitterButton.addWidget(splitterRadio)
        #splitterButton.addWidget(splitterRadio2)

        splitterButton2 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitterButton2.addWidget(addButton)
        splitterButton2.addWidget(removeButton)
        splitterButton2.addWidget(saveButton)
        splitterButton2.addWidget(loadButton)

        sliderArea = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        sliderArea.addWidget(self.sizeSlider)

        ###################### third try with QTextObjectInterface object
        # self.drawarea = QStackedWidget(self)
        self.renderArea = abcd.RenderAreaWidget.RenderArea()
        self.renderArea.setFixedSize(800, 700)

        # Splitter vertical
        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.textedit=QtWidgets.QTextEdit()
        self.textedit.setFixedSize(800, 200)
        splitter1.addWidget(splitterButton)
        splitter1.addWidget(splitterButton2)
        splitter1.addWidget(QtWidgets.QLabel('Size Coefficient: '))
        splitter1.addWidget(sliderArea)
        splitter1.addWidget(self.textedit)
        #splitter1.addWidget(self.drawarea)
        splitter1.addWidget(self.renderArea)

        self.hbox.addWidget(splitter1)
        #self.hbox.addWidget(self.drawarea)
        self.setLayout(self.hbox)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))

        # connection des events
        addButton.clicked.connect(self.addButtonFunc)
        saveButton.clicked.connect(self.saveButtonFunc)
        removeButton.clicked.connect(self.removeButtonFunc)
        loadButton.clicked.connect(self.loadButtonFunc)

        self.setGeometry(200, 200, 900, 900)
        self.setWindowTitle('QSplitter demo')
        self.show()

    def sliderCreation(self, min, max, value, interval):
        """define a slider with default values if parameter are not set"""
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setValue(value)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(interval)
        self.slider.valueChanged.connect(self.valueChange)
        return self.slider

    def valueChange(self):
        sliderCoef = self.slider.value()
        self.textedit.append("inside of slider: " + str(sliderCoef))
        return sliderCoef


    def finalSize(self, objectSize):
        """will define the new size of object in regard of """
        # list will be used to copy the list and not to refer at the same list
        modifiedSize = list(objectSize)

        try:
            vc = self.valueChange()
            modifiedSize = [o * vc for o in objectSize]
            return modifiedSize
        except:
            # configuration of the log file name
            #logFileName = 'Validation_%s.log' % time.strftime('%y%m%d', time.localtime(time.time()))

            logging.exception("function finalSize, parameter objectSize not a list")


    def addButtonFunc(self):
        """action started after the press of add button"""
        partShape = None
        if (self.radioBody.isChecked() == True):
            print('in radio body selection')
            appliedSize = self.finalSize(self.__bodySize)
            partShape = "Body"
            self.rectAdd = abcd.forms.rectangle_form.RectangleForm(appliedSize[0], appliedSize[1], appliedSize[2], appliedSize[3], partShape, QtGui.QColor(255, 0, 0))
        if (self.radioNose.isChecked() == True):
            partShape = "Nose"
            self.rectAdd = abcd.forms.rectangle_form.RectangleForm(10, 10, 40 , 60, partShape, QtGui.QColor(255, 255, 0))
        if (self.radioTail.isChecked() == True):
            partShape = "Tail"
            self.rectAdd = abcd.forms.rectangle_form.RectangleForm(10, 10, 50 , 50, partShape, QtGui.QColor(0, 0, 255))
        rectAddTex = "a new rectangle form: %s" % (partShape)
        self.renderArea.addShape(self.rectAdd)
        self.textedit.append(rectAddTex)
        print ("inside of the addButton function")



    def saveButtonFunc(self):
        """action started after the press of add button"""
        print ("inside of the saveButton function")
        self.renderArea.toJson()

    def removeButtonFunc(self):
        """action started after the press of add button"""
        print ("inside of the removeButton function")


    def loadButtonFunc(self):
        """action started after the press of add button"""
        print ("inside of the removeButton function")
        reconciclass = Reconciliation()
        print ("current value of listclass" + reconciclass.listClass())



    def mousePressEvent(self, event):
        """select the nearest current object"""
        if event.button() == Qt.LeftButton:
            self.textedit.append("left click")

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()