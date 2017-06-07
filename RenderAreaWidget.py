# create a widget which will accept other widget inside

import sys
import json
from PyQt4 import QtCore, QtGui, Qt

import abcdforminterface
import rectangle_form
import circleform



class RenderArea(QtGui.QWidget):

    def __init__(self, parent= None):
        '''init part for the RenderArea'''
        QtGui.QWidget.__init__(self, parent)
        # liste of shapes element
        self.setAutoFillBackground(True)
        self.__palette= self.palette()
        self.__palette.setColor(self.backgroundRole(), QtGui.QColor('white'))
        self.__painter = None
        self.__shapes = []
        self.__selected = None
        self.createUI()

    def addShape(self, shape):
        self.__shapes.append(shape)

    def paintEvent(self, event):
        if self.__shapes:
            if self.__painter is None:
                self.__painter = QtGui.QPainter(self)

            self.__painter.begin(self)
            for shape in self.__shapes:
                shape.createForm(self.__painter)
            self.__painter.end()


    def createUI(self):
        '''creation of the render area with the different geometry element'''
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Canvas')
        self.show()


    def mousePressEvent(self, event):
        self.__selected = None
        pos = event.pos()
        for shape in self.__shapes:
            if shape.isOver(pos.x(), pos.y()):
                self.__selected = abcdforminterface.Selection(shape, pos)
                break

    def mouseMoveEvent(self, event):
        if self.__selected is None:
            return

        self.__selected.move(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        self.__selected = None


    #def filePresent(self, fileName):
    #    try:
    #        if os.path.exist(fileName):
    #            print ("print file present - can be used")
    #            return True
    #    except:
    #        print ("json file does not exist, creation to do")
    #        return False

    def toJson(self):
        """will save the different elements present in __shape to a json files"""
        fileName= "first_save.json"
        with open(fileName, 'w') as f:
            for shape in self.__shapes:
                currentShape = {}
                if shape._name == "rectangle":
                    currentShape['name'] = shape._name
                    currentShape['origin'] = shape._origin
                    currentShape['width'] = shape._width
                    currentShape['height'] = shape._height
                    json.dump(currentShape, f, indent = 4)
                if shape._name == "circle":
                    print("circle save to do")
        fileName.close()

def main():
    app = QtGui.QApplication(sys.argv)
    canvas = RenderArea()
    #canvas.addShape(Rectangle(10, 10, 40 , 60, QtGui.QColor(255, 0, 0)))
    rectangle = rectangle_form.RectangleForm(10, 10, 40 , 60, QtGui.QColor(255, 0, 0))
    #circle = circleform.CircleForm(100, 30, 60, 60, QtGui.QColor(0, 0, 255))
    canvas.addShape(rectangle)
    #canvas.addShape(circle)
    canvas.toJson()
    #canvas.addShape(Ellipse(100, 30, 40, 10, QtGui.QColor(0, 255, 0)))
    #canvas.addShape(Circle(200, 30, 40, QtGui.QColor(0, 0, 255)))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
