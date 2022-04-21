import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget 
from PyQt6.QtWidgets import QLineEdit 
from PyQt6.QtWidgets import QPushButton 
from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import QIcon 



class Dicom(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prueba")
        #self.setGeometry(500, 300, 400, 300)
        self.resize(500, 300) #width, height
        #self.setStyleSheet('background-color:white')

        layout = QVBoxLayout()
        self.setLayout(layout)

        #Widgets
        self.inputField = QLineEdit()
        button = QPushButton('Say Hello', clicked=self.sayHello)
        #button.clciced.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)


    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))
        




#app = QApplication([])
app = QApplication(sys.argv)

window = Dicom()
window.show()

sys.exit(app.exec())


