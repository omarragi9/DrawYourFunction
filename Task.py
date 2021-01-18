from PySide2.QtWidgets import *
from PySide2.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw Your Function')
        self.resize(500 , 400)
        
        func_label    = QLabel(self)
        min_val_label = QLabel(self)
        max_val_label = QLabel(self)
        masseage      = QLabel(self)
        masseage.setFixedSize(300, 20)
        setattr(Window, 'func_label', func_label)
        setattr(Window, 'min_val_label', min_val_label)
        setattr(Window, 'max_val_label', max_val_label)
        setattr(Window, 'masseage', masseage)
        
        func_label.setText('Enter the function of X :         ')
        func_label.setAlignment(Qt.AlignCenter)
        min_val_label.setText('Enter the minimum value of X : ')
        min_val_label.setAlignment(Qt.AlignCenter)
        max_val_label.setText('Enter the maximum value of X : ')
        max_val_label.setAlignment(Qt.AlignCenter)
        masseage.setText('Please enter your function space separated.')

        func_val = QLineEdit()
        min_val  = QLineEdit()
        max_val  = QLineEdit()
        setattr(Window, 'func_val', func_val)
        setattr(Window, 'min_val', min_val)
        setattr(Window, 'max_val', max_val)
            
            
        def Draw_Function():
             try:
                 x        = range(int(min_val.text()) , int(max_val.text()) + 1) # The range from minimum value of x to the maximum value of x
                 func     = func_val.text() # The body of the function
                 result   = [[] for i in range(len(x))] # The result of the function for each input of x
                 counter  = 0
                 for j in x:
                     for i in func.split():
                         if isinstance(i , str) and (i in ['+' , '-' , '/' , '*' , '^' , '**']):
                             pass
                         elif isinstance(i , str) and (i.isdigit()):
                             pass
                         else:
                             i = j
                         result[counter].append(i)
                     counter += 1


                 counter = 0
                 for string in result:
                     if string: # Just to avoid error if any item of the result list is empty list
                         result[counter] = string
                         result[counter] = eval(''.join([str(elem) for elem in result[counter]]))
                         counter += 1
                         
                 print(result)
                 setattr(Window, 'result', result)
                 canvas = FigureCanvas(Figure(figsize = (5 , 3)))
                 setattr(Window, 'canvas', canvas)
                 layout.addWidget(canvas)
                 static_ax = canvas.figure.subplots()
                 static_ax.plot(x , result)
             except ArithmeticError as e:
                 error_label = QLabel(self)
                 error_label.setText('Invalid Function')
                 layout.addWidget(error_label, 4, 2)
             except:
                 error_label = QLabel(self)
                 error_label.setText('Please Enter Your Inputs')
                 layout.addWidget(error_label, 4, 1)
             
        button = QPushButton("Submit")
        setattr(Window, 'button', button)
        button.clicked.connect(Draw_Function)
        button.setFixedSize(100, 20)

        layout = QGridLayout(self)
        layout.addWidget(func_label, 1, 0)
        layout.addWidget(func_val, 1, 1)
        layout.addWidget(min_val_label, 2, 0)
        layout.addWidget(min_val, 2, 1)
        layout.addWidget(max_val_label, 3, 0)
        layout.addWidget(max_val, 3, 1)
        layout.addWidget(button, 4, 0)
        layout.addWidget(masseage, 0, 1)

        
myApp  = QCoreApplication.instance()
if myApp is None:
    myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
#sys.exit(0)
