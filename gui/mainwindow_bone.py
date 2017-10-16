# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_bone.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Arbitrade(object):
    def setupUi(self, Arbitrade):
        Arbitrade.setObjectName("Arbitrade")
        Arbitrade.resize(1328, 969)
        self.centralwidget = QtWidgets.QWidget(Arbitrade)
        self.centralwidget.setObjectName("centralwidget")
        self.DateTimeView = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.DateTimeView.setGeometry(QtCore.QRect(1083, 0, 241, 34))
        self.DateTimeView.setObjectName("DateTimeView")
        self.PortfolioTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.PortfolioTableWidget.setGeometry(QtCore.QRect(10, 60, 511, 841))
        self.PortfolioTableWidget.setObjectName("PortfolioTableWidget")
        self.PortfolioTableWidget.setColumnCount(0)
        self.PortfolioTableWidget.setRowCount(0)
        self.PortfolioTableViewLabel = QtWidgets.QLabel(self.centralwidget)
        self.PortfolioTableViewLabel.setGeometry(QtCore.QRect(120, 10, 261, 51))
        self.PortfolioTableViewLabel.setObjectName("PortfolioTableViewLabel")
        self.PortfolioGraphViewLabel = QtWidgets.QLabel(self.centralwidget)
        self.PortfolioGraphViewLabel.setGeometry(QtCore.QRect(800, 10, 261, 51))
        self.PortfolioGraphViewLabel.setObjectName("PortfolioGraphViewLabel")
        self.PortfolioGraphWidget = QtWidgets.QGraphicsView(self.centralwidget)
        self.PortfolioGraphWidget.setGeometry(QtCore.QRect(540, 60, 771, 731))
        self.PortfolioGraphWidget.setMouseTracking(True)
        self.PortfolioGraphWidget.setObjectName("PortfolioGraphWidget")
        self.TransactionPushButtom = QtWidgets.QPushButton(self.centralwidget)
        self.TransactionPushButtom.setGeometry(QtCore.QRect(620, 820, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TransactionPushButtom.setFont(font)
        self.TransactionPushButtom.setObjectName("TransactionPushButtom")
        self.HistoryPushButtom = QtWidgets.QPushButton(self.centralwidget)
        self.HistoryPushButtom.setGeometry(QtCore.QRect(1010, 820, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.HistoryPushButtom.setFont(font)
        self.HistoryPushButtom.setObjectName("HistoryPushButtom")
        Arbitrade.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Arbitrade)
        self.statusbar.setObjectName("statusbar")
        Arbitrade.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Arbitrade)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 32))
        self.menubar.setObjectName("menubar")
        self.FileMenu = QtWidgets.QMenu(self.menubar)
        self.FileMenu.setObjectName("FileMenu")
        self.ToolsMenu = QtWidgets.QMenu(self.menubar)
        self.ToolsMenu.setObjectName("ToolsMenu")
        self.AboutMenu = QtWidgets.QMenu(self.menubar)
        self.AboutMenu.setObjectName("AboutMenu")
        Arbitrade.setMenuBar(self.menubar)
        self.LoadAction = QtWidgets.QAction(Arbitrade)
        self.LoadAction.setObjectName("LoadAction")
        self.SaveAction = QtWidgets.QAction(Arbitrade)
        self.SaveAction.setObjectName("SaveAction")
        self.ExitAction = QtWidgets.QAction(Arbitrade)
        self.ExitAction.setObjectName("ExitAction")
        self.StocksAction = QtWidgets.QAction(Arbitrade)
        self.StocksAction.setObjectName("StocksAction")
        self.AlgorithmAction = QtWidgets.QAction(Arbitrade)
        self.AlgorithmAction.setObjectName("AlgorithmAction")
        self.FileMenu.addAction(self.LoadAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.SaveAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.ExitAction)
        self.ToolsMenu.addAction(self.StocksAction)
        self.ToolsMenu.addSeparator()
        self.ToolsMenu.addAction(self.AlgorithmAction)
        self.ToolsMenu.addSeparator()
        self.menubar.addAction(self.FileMenu.menuAction())
        self.menubar.addAction(self.ToolsMenu.menuAction())
        self.menubar.addAction(self.AboutMenu.menuAction())

        self.retranslateUi(Arbitrade)
        QtCore.QMetaObject.connectSlotsByName(Arbitrade)

    def retranslateUi(self, Arbitrade):
        _translate = QtCore.QCoreApplication.translate
        Arbitrade.setWindowTitle(_translate("Arbitrade", "MainWindow"))
        self.DateTimeView.setDisplayFormat(_translate("Arbitrade", "M/d/yy h:mm:ss AP"))
        self.PortfolioTableViewLabel.setText(_translate("Arbitrade", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Portfolio Table View</span></p></body></html>"))
        self.PortfolioGraphViewLabel.setText(_translate("Arbitrade", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Portfolio Graph View</span></p></body></html>"))
        self.TransactionPushButtom.setToolTip(_translate("Arbitrade", "<html><head/><body><p>Buy or sell stocks</p></body></html>"))
        self.TransactionPushButtom.setText(_translate("Arbitrade", "Buy/Sell"))
        self.HistoryPushButtom.setToolTip(_translate("Arbitrade", "<html><head/><body><p>Buy or sell stocks</p></body></html>"))
        self.HistoryPushButtom.setText(_translate("Arbitrade", "View History"))
        self.FileMenu.setTitle(_translate("Arbitrade", "File"))
        self.ToolsMenu.setTitle(_translate("Arbitrade", "Tools"))
        self.AboutMenu.setTitle(_translate("Arbitrade", "About"))
        self.LoadAction.setText(_translate("Arbitrade", "Load"))
        self.SaveAction.setText(_translate("Arbitrade", "Save"))
        self.ExitAction.setText(_translate("Arbitrade", "Exit"))
        self.StocksAction.setText(_translate("Arbitrade", "Stocks"))
        self.AlgorithmAction.setText(_translate("Arbitrade", "Algorithm"))

