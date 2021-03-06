
from PySide6.QtCore import QRect, QMetaObject, QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QLabel, QRadioButton, QLineEdit, QPushButton
from PIL import Image
import numpy as np
import png 
import os, pydicom
import cv2 as cv
import glob
import sys

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName(u"Form")
        Form.resize(664, 460)
        Form.setToolTipDuration(-2)
        Form.setStyleSheet("background-color: rgb(153, 204, 255);")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(280, 20, 101, 41))
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(QFont.Normal)
        self.label.setFont(font)
        self.label.setObjectName(u"label")

        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(20, 80, 151, 16))
        self.label_2.setObjectName(u"label_2")

        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(20, 290, 151, 16))
        self.label_3.setObjectName(u"label_3")

        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QRect(60, 130, 141, 16))
        self.label_4.setObjectName(u"label_4")

        self.radioButton = QRadioButton(Form)
        self.radioButton.setGeometry(QRect(150, 200, 99, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(u"radioButton")

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setGeometry(QRect(280, 200, 99, 20))
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.label_5 = QLabel(Form)
        self.label_5.setGeometry(QRect(60, 160, 141, 16))
        self.label_5.setObjectName(u"label_5")

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QRect(202, 130, 251, 21))
        self.lineEdit.setStyleSheet("background: white")
        self.lineEdit.setObjectName(u"lineEdit")

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setGeometry(QRect(200, 160, 251, 21))
        self.lineEdit_2.setStyleSheet("background: white")
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(480, 190, 113, 32))
        self.pushButton.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.cambiarFormato)

        self.label_6 = QLabel(Form)
        self.label_6.setGeometry(QRect(60, 200, 61, 16))
        self.label_6.setObjectName(u"label_6")

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setGeometry(QRect(200, 320, 251, 21))
        self.lineEdit_3.setStyleSheet("background: white")

        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.label_7 = QLabel(Form)
        self.label_7.setGeometry(QRect(58, 320, 141, 16))
        self.label_7.setObjectName(u"label_7")

        self.label_8 = QLabel(Form)
        self.label_8.setGeometry(QRect(60, 350, 61, 16))
        self.label_8.setObjectName(u"label_8")

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setGeometry(QRect(200, 350, 111, 21))
        self.lineEdit_4.setStyleSheet("background: white")
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.pushButton2 = QPushButton(Form)
        self.pushButton2.setGeometry(QRect(480, 350, 113, 32))
        self.pushButton2.setStyleSheet("background-color: rgb(224, 224, 224);")        
        self.pushButton2.setObjectName(u"pushButton")
        self.pushButton2.clicked.connect(self.crearVideo)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setGeometry(QRect(470, 130, 31, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.selectorArchivos('boton 1'))

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setGeometry(QRect(470, 160, 31, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.selectorArchivos('boton 2'))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setGeometry(QRect(470, 320, 31, 21))
        self.pushButton_5.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.selectorArchivos('boton 3'))

        #self.pushButton4 =QPushButton(Form)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def selectorArchivos(self, name):
        if name == 'boton 3':
            ruta = QFileDialog.getExistingDirectory(self, "Open Directory", r'.')
            self.lineEdit_3.setText(ruta)
        else:
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            dialog.setDirectory(r'./')
            if dialog.exec():
                ruta = dialog.selectedFiles()[0]
                if name == 'boton 1':
                    self.lineEdit.setText(ruta)
                else:
                    self.lineEdit_2.setText(ruta)


    def cambiarFormato(self):
        rutaEntrada = self.lineEdit.text()
        rutaSalida = self.lineEdit_2.text()

        list_of_files = []
        if os.path.isfile(rutaEntrada):
            archivo=os.path.basename(open(rutaEntrada).name)
            list_of_files = [archivo]
        else:
            list_of_files = os.listdir(rutaEntrada)
        
        for file in list_of_files:
            try:
                ds = pydicom.dcmread(os.path.join(rutaEntrada,file)) #al nombre de la carpeta le une el nombre de archivo
                shape = ds.pixel_array.shape #devulve[alto, ancho]

                # Convert to float to avoid overflow or underflow losses.
                image_2d = ds.pixel_array.astype(float)

                # Rescaling grey scale between 0-255
                image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

                # Convert to uint
                image_2d_scaled = np.uint8(image_2d_scaled)

                # Write the PNG file
                file= file.split(".dcm")[0] #quitar el texto que no se quiere
                if self.radioButton_2.isChecked():
                    with open(os.path.join(rutaSalida, file) +'.png' , 'wb') as png_file: #wb :w de escritura y b de que es archibo binario
                        w = png.Writer(shape[1], shape[0], greyscale=True) #ancho y alto
                        w.write(png_file, image_2d_scaled)
                else:
                    # Write the JPG file
                    im = Image.fromarray(image_2d_scaled)
                    im.save(os.path.join(rutaSalida, file) +'.jpg')
                
            except:
                print('Could not convert: ', file)

    def crearVideo(self):
        ruta = self.lineEdit_3.text() + '/*'
        frame = self.lineEdit_4.text()
        size = (0, 0)
        img_array = []
        for filename in sorted(glob.glob(ruta)): #recorre todos los archivos .png de la carpeta /*png
            img = cv.imread(filename) #lee la imagen
            height, width, _ = img.shape #obtiene el tama??o de la imagen (ancho, alto y numero de colores)
            size = (width,height) #alamacenamos en una variable el tama??o del video
            img_array.append(img) #mete la imagen en la lista de imagenes
        #crea el video 
        #fourcc = especificas el formato 
        #15 = numero de imagenes por segundo (frames)
        out = cv.VideoWriter('./project.avi',cv.VideoWriter_fourcc(*'DIVX'), int(frame), size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()



    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", u"Dicom GUI"))
        self.label.setText(_translate("Form", u"DICOM"))
        self.label_2.setText(_translate("Form", u"Conversi??n de im??genes"))
        self.label_3.setText(_translate("Form", u"Video con im??genes"))
        self.label_4.setText(_translate("Form", u"Ruta entrada dataset:"))
        self.radioButton.setText(_translate("Form", u".JPG"))
        self.radioButton_2.setText(_translate("Form", u".PNG"))
        self.label_5.setText(_translate("Form", u"Ruta salida dataset:"))
        self.pushButton.setText(_translate("Form", u"Convertir"))
        self.label_6.setText(_translate("Form", u"Formato:"))
        self.label_7.setText(_translate("Form", u"Ruta  im??genes:"))
        self.label_8.setText(_translate("Form", u"Frames/s:"))
        self.pushButton2.setText(_translate("Form", u"Crear"))
    
        self.pushButton_3.setText(_translate("Form", u"..."))
        self.pushButton_4.setText(_translate("Form", u"..."))
        self.pushButton_5.setText(_translate("Form", u"..."))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
