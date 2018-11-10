# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog,QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from ui_imagedialog import Ui_ImageDialog
import heatmap,heatmap_groups,lineplot, violin_group,violin_topic,scatter_group,scatter_topic, main_graph, shell


class Main(QMainWindow):

    def terminate(self):
        sys.exit(app.exec_())
    def showDialog(self):
        index = self.ui.taskbox.currentIndex()
         #
        if index>=1 and  index<=8:
            fname, _ = QFileDialog.getOpenFileName(filter='*.csv')
        else:
            fname, _ = QFileDialog.getOpenFileName(filter='*.json')
        self.filename = fname
        self.ui.plotnow.setStyleSheet('QPushButton {background-color: green; color: white;}')
        app.processEvents()
        self.ui.plotnow.setEnabled(True)

    def processtasks(self):

        index = self.ui.taskbox.currentIndex()

        if index>=1 and  index<=8:
            self.ui.selectfile.setEnabled(True)
            self.ui.selectfile.setStyleSheet('QPushButton {background-color: lightblue; color: black;}')
            self.ui.selectfile.setText('Select CSV File')
        else:
            self.ui.selectfile.setEnabled(True)
            self.ui.selectfile.setStyleSheet('QPushButton {background-color: lightblue; color: black;}')
            self.ui.selectfile.setText('Select JSON File')





    def plot(self):
        self.ui.selectfile.setEnabled(False)
        self.ui.selectfile.setStyleSheet('QPushButton {background-color: gray; color: black;}')
        index = self.ui.taskbox.currentIndex()
        if index == 1:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = heatmap.make_heatmap(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            heatmap.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index== 2:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = heatmap_groups.make_heatmap(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            heatmap_groups.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index==3:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = lineplot.read_data(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            lineplot.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()

        elif index == 4:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = violin_group.read_data(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            violin_group.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index == 5:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = violin_topic.read_data(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            violin_topic.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index == 6:
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            scatter_group.plot(self.filename)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index == 7:
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            scatter_topic.plot(self.filename)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index == 8:
            self.ui.msgbox.setText('Parsing data...')
            app.processEvents()
            self.data = main_graph.read_data(self.filename)
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            main_graph.plot(self.data)
            self.ui.msgbox.setText(' ')
            app.processEvents()
        elif index ==9:
            self.ui.msgbox.setText('Visualizing...')
            app.processEvents()
            shell.plot(self.filename)
            self.ui.msgbox.setText(' ')
            app.processEvents()

    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
        self.ui.plotnow.setStyleSheet('QPushButton {background-color: gray; color: white;}')
        self.ui.quitbutton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')
        # connect signals
        self.ui.selectfile.clicked.connect(self.showDialog)
        self.ui.taskbox.activated.connect(self.processtasks)
        self.ui.quitbutton.clicked.connect(self.terminate)
        self.ui.plotnow.clicked.connect(self.plot)



        #self.ui.comboBox.



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



#
# app = QApplication(sys.argv)
# window = QDialog()
# ui = Ui_ImageDialog()
# ui.setupUi(window)
# window.show()
# sys.exit(app.exec_())