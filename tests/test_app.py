"""Test case for PySide bug #982
If you hover the mouse over the window, it will be fine,
but the first time the topLevelAt is called with the cursor
outside the window, it will segfault.
"""

# stdlib imports
import sys

# Import Qt:
from PySide import QtGui, QtCore
# from PyQt4 import QtGui, QtCore

def print_topLevelAt():
    """callback to print current cursor position and return of topLevelAt"""
    cpos = QtGui.QCursor.pos()
    print cpos
    # when nothing is there, PyQt returns None
    # whereas PySide segfaults in this call:
    print QtGui.qApp.topLevelAt(cpos)

if __name__ == '__main__':
    # create empty window, with a timer that calls topLevelAt with
    # the current cursor position every 1s
    app = QtGui.QApplication([])
    window = QtGui.QMainWindow()
    window.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(print_topLevelAt)
    timer.start(1000)
    
    app.exec_()
