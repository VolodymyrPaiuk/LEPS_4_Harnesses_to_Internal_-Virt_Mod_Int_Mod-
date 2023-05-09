# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEPS_4_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import module.Harness_to_Internal
import module.Choose_file
import module.read_record_csv

class Ui_LEPS_4_2(object):

    def __init__(self):
        #Ініціалізація всіх змінних
        self.Read_harnesses = []
        self.uniq_har = []
        self.Read_Int = []
        self.Readed_Int_and_number_of_virt = []
        self.Read_Virt = []
        self.Rezult = []

    def setupUi(self, LEPS_4_2):
        LEPS_4_2.setObjectName("LEPS_4_2")
        LEPS_4_2.setWindowModality(QtCore.Qt.ApplicationModal)
        LEPS_4_2.resize(817, 348)
        self.pushButton = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 201, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 271, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(LEPS_4_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 271, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(LEPS_4_2)
        self.label.setGeometry(QtCore.QRect(220, 10, 521, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LEPS_4_2)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 521, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LEPS_4_2)
        self.label_3.setGeometry(QtCore.QRect(220, 90, 521, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LEPS_4_2)
        self.label_4.setGeometry(QtCore.QRect(500, 130, 100, 21))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(LEPS_4_2)
        self.progressBar.setGeometry(QtCore.QRect(290, 130, 200, 31))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(LEPS_4_2)
        QtCore.QMetaObject.connectSlotsByName(LEPS_4_2)

    def retranslateUi(self, LEPS_4_2):
        _translate = QtCore.QCoreApplication.translate
        LEPS_4_2.setWindowTitle(_translate("LEPS_4_2", "LEPS_4_1"))
        self.pushButton.setText(_translate("LEPS_4_2", "Download harnesses"))
        self.pushButton.clicked.connect(self.clicer_pushButton)
        self.pushButton_2.setText(_translate("LEPS_4_2", "Download Virtual"))
        self.pushButton_2.clicked.connect(self.clicer_pushButton_2)
        self.pushButton_3.setText(_translate("LEPS_4_2", "Download Internal"))
        self.pushButton_3.clicked.connect(self.clicer_pushButton_3)
        self.pushButton_4.setText(_translate("LEPS_4_2", "Generate Internal for harnesses"))
        self.pushButton_4.clicked.connect(self.clicer_pushButton_4)
        self.pushButton_5.setText(_translate("LEPS_4_2", "SAVE Internal"))
        self.pushButton_5.clicked.connect(self.clicer_pushButton_5)
        self.label.setText(_translate("LEPS_4_2", "NOT"))
        self.label_2.setText(_translate("LEPS_4_2", "NOT"))
        self.label_3.setText(_translate("LEPS_4_2", "NOT"))
        self.label_4.setText(_translate("LEPS_4_2", "NOT"))

    def clicer_pushButton(self):
        Open_Read_harnesses = QFileDialog.getExistingDirectory()
        if Open_Read_harnesses:
            self.Read_harnesses = module.Choose_file.choose_harnesses_in_folder(Open_Read_harnesses)
            # визначення списку унікальних вязок
            for i in self.Read_harnesses:
                if i[0] not in self.uniq_har:
                    self.uniq_har.append(i[0])
            self.label.setText(Open_Read_harnesses)

    def clicer_pushButton_2(self):
        Open_Read_Virtual = QFileDialog.getOpenFileName()
        if Open_Read_Virtual:
            self.Read_Virt = module.Choose_file.choose_Virt(Open_Read_Virtual[0])
            name_open_file = Open_Read_Virtual[0].split("/")
            self.label_2.setText(name_open_file[len(name_open_file) - 1])


    def clicer_pushButton_3(self):
        Open_Read_Int = QFileDialog.getOpenFileName()
        if Open_Read_Int:
            self.Read_Int = module.read_record_csv.read(Open_Read_Int[0])
            # Роблю список інтернал і кількість віртуалів(умов) під інтернал, щоб в кінці відсіяти умови які виконались але це умови які не виконались під більші конфігурації
            internal_withaut_harn = []
            internal_withaut_harn_mas = []
            for i in self.Read_Int:
                if i[0] not in internal_withaut_harn:
                    internal_withaut_harn.append(i[0])
            for i in self.Read_Int:
                internal_withaut_harn_mas.append(i[0])
            for i in internal_withaut_harn:
                add_in_mass = []
                add_in_mass.append(i)
                add_in_mass.append(internal_withaut_harn_mas.count(i))
                self.Readed_Int_and_number_of_virt.append(add_in_mass)

            name_open_file = Open_Read_Int[0].split("/")
            self.label_3.setText(name_open_file[len(name_open_file) - 1])

    def clicer_pushButton_4(self):
        # self.Rezult = module.Harness_to_Internal.Harness_to_Internal(self.Read_harnesses, self.Read_Virt, self.Read_Int)
        for i in range(len(self.uniq_har)):
            # Проходжу циклом для відбору окремої вязки в масив
            one_separ_harn_prev = []
            for k in self.Read_harnesses:
                if self.uniq_har[i] == k[0]:
                    one_separ_harn_prev.append(k)
            # Видаляю дублікати щоб не було помилки при закиданні однакових вязок
            one_separ_harn = []
            for k in one_separ_harn_prev:
                if k not in one_separ_harn:
                    one_separ_harn.append(k)
            self.Rezult.extend(module.Harness_to_Internal.Harness_to_Internal(self.uniq_har[i], one_separ_harn, self.Read_Virt, self.Read_Int, self.Readed_Int_and_number_of_virt))

            self.progressBar.setProperty("value", i/len(self.uniq_har)*100)
        self.label_4.setText("GENERATED")


    def clicer_pushButton_5(self):
        save_Rezult = QFileDialog.getSaveFileName(filter='Data File (*.csv)')
        if save_Rezult:
            module.read_record_csv.record(self.Rezult, save_Rezult[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LEPS_4_2 = QtWidgets.QWidget()
    ui = Ui_LEPS_4_2()
    ui.setupUi(LEPS_4_2)
    LEPS_4_2.show()
    sys.exit(app.exec_())
