import sys
import abc
from PyQt4 import QtGui, QtCore

class FormInterface(QtGui.QWidget):
    def __init__(self, color):
        """
        Initialize.
        """
        super(FormInterface, self).__init__()
        self._origin = None
        self._color = color
        self._predatashape = {}

    ##############
    # painter definition
    ##############
    def paintEvent(self, event):
        """function which will draw the form
        event dedicated to manage the draw
        """
        # definition of painter
        self.qp = QtGui.QPainter()
        self.qp.begin(self)
        self.addForm(self.qp)
        self.qp.end()

    @abc.abstractmethod
    def createForm(self, form):
        """add the form defined by the class by using the Qpainter"""
        # rajouter un raise not implemented si fonction non utilise dans la classe
        # if this function is called directly by the mother class, an error message will appear
        return

    ##############
    # definition of form origin
    ##############
    @property
    def origin(self):
        return self._origin

    @abc.abstractmethod
    def className(self):
        """will return the name of the clase"""
        return

    @abc.abstractmethod
    def predataShape(self):
        """goal: define the different parameter of the shape in one dictionnary"""
        return


    ################
    # move function
    ################
    @abc.abstractmethod
    def isOver(self, x, y):
        return

    @abc.abstractmethod
    def move(self, x, y):
        return

    @abc.abstractmethod
    def shift(self, dx, dy):
        return


class Selection(object):
    """
    Class that represents any selected shape(s)
    """

    def __init__(self, shape, position):
        self.__shape = shape
        self.__pos = position
        self._origin = self.__shape.origin

    def move(self, position):
        delta = position - self.__pos
        self.__shape.move(self._origin[0] + delta.x(), self._origin[1] + delta.y())


