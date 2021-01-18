import pytest
import Task
from PySide2.QtCore import *

@pytest.fixture
def app(qtbot):
    test_task = Task.Window()
    qtbot.addWidget(test_task)

    return test_task


def test_labelx(app):
    assert app.func_label.text()    == 'Enter the function of X :         '
    assert app.min_val_label.text() == 'Enter the minimum value of X : '
    assert app.max_val_label.text() == 'Enter the maximum value of X : '
    assert app.masseage.text()      == 'Please enter your function space separated.'

def test_textboxes(app):
    assert app.func_val # To ensure that the window has these labels
    assert app.min_val
    assert app.max_val

def test_button_click(app , qtbot):
    qtbot.mouseClick(app.button, Qt.LeftButton)
    assert app.canvas
