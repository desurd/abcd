# systeme class
import sys

# UI class
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# personnal class
import rectangle_form
import RenderAreaWidget


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.__bodySize = [10, 10, 70, 60]

    def initUI(self):
        self.hbox = QHBoxLayout(self)

        # radio button definition
        self.radioBody = QRadioButton("Body", self)
        self.radioTail = QRadioButton("Tail", self)
        self.radioNose = QRadioButton("Nose", self)
        splitterRadio = QSplitter(Qt.Horizontal)
        splitterRadio.addWidget(self.radioBody)
        splitterRadio.addWidget(self.radioTail)
        splitterRadio.addWidget(self.radioNose)
        self.sizeSlider = self.sliderCreation(min=0.5, max=3, value=1, interval=0.5)

        self.halfSize = QRadioButton("Half", self)
        self.normalSize = QRadioButton("Normal", self)
        self.doubleSize = QRadioButton("Double", self)
        splitterRadio2 = QSplitter(Qt.Horizontal)
        splitterRadio2.addWidget(self.halfSize)
        splitterRadio2.addWidget(self.normalSize)
        splitterRadio2.addWidget(self.doubleSize)

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
        splitterButton.addWidget(splitterRadio2)

        splitterButton2 = QSplitter(Qt.Horizontal)
        splitterButton2.addWidget(addButton)
        splitterButton2.addWidget(removeButton)
        splitterButton2.addWidget(saveButton)

        sliderArea = QSplitter(Qt.Horizontal)
        sliderArea.addWidget(self.sizeSlider)

        ###################### third try with QTextObjectInterface object
        # self.drawarea = QStackedWidget(self)
        self.renderArea = RenderAreaWidget.RenderArea()
        self.renderArea.setFixedSize(800, 700)

        # Splitter vertical
        splitter1 = QSplitter(Qt.Vertical)
        self.textedit=QTextEdit()
        self.textedit.setFixedSize(800, 200)
        splitter1.addWidget(splitterButton)
        splitter1.addWidget(splitterButton2)
        splitter1.addWidget(QLabel('Size Coefficient: '))
        splitter1.addWidget(sliderArea)
        splitter1.addWidget(self.textedit)
        #splitter1.addWidget(self.drawarea)
        splitter1.addWidget(self.renderArea)

        self.hbox.addWidget(splitter1)
        #self.hbox.addWidget(self.drawarea)
        self.setLayout(self.hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        # connection des events
        addButton.clicked.connect(self.addButtonFunc)
        saveButton.clicked.connect(self.saveButtonFunc)
        removeButton.clicked.connect(self.removeButtonFunc)

        self.setGeometry(200, 200, 900, 900)
        self.setWindowTitle('QSplitter demo')
        self.show()

    def sliderCreation(self, min, max, value, interval):
        """define a slider with default values if parameter are not set"""
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setValue(value)
        self.slider.setTickPosition(QSlider.TicksBelow)
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

        #self.textedit.append("value of slider bar in final size" + str(userCoef))
        self.textedit.append("value of slider bar in final size" + str(self.valueChange()))
        # temporary removed
        #if self.halfSize.isChecked() == True:
        #    coef = 0.5
        #if self.normalSize.isChecked() == True:
        #    coef = 1
        #if self.doubleSize.isChecked() == True:
        #    coef = 2
        try:
            for i in xrange(len(objectSize)):
                modifiedSize[i]= modifiedSize[i] * (self.valueChange())
            return modifiedSize
        except:
            print ('function finalSize, parameter objectSize not a list')


    def addButtonFunc(self):
        """action started after the press of add button"""
        partShape = None
        if (self.radioBody.isChecked() == True):
            print 'in radio body selection'
            appliedSize = self.finalSize(self.__bodySize)
            self.rectAdd = rectangle_form.RectangleForm(appliedSize[0], appliedSize[1], appliedSize[2], appliedSize[3], QColor(255, 0, 0))
            partShape = "Body"
        if (self.radioNose.isChecked() == True):
            self.rectAdd = rectangle_form.RectangleForm(10, 10, 40 , 60, QColor(255, 255, 0))
            partShape = "Nose"
        if (self.radioTail.isChecked() == True):
            self.rectAdd = rectangle_form.RectangleForm(10, 10, 50 , 50, QColor(0, 0, 255))
            partShape = "Tail"
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

    def mousePressEvent(self, event):
        """select the nearest current object"""
        if event.button() == Qt.LeftButton:
            self.textedit.append("left click")

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()