# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Methodron.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import *


class Ui_Methodron(object):
    def setupUi(self, Methodron):
        Methodron.setObjectName("Methodron")
        Methodron.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(Methodron.sizePolicy().hasHeightForWidth())
        Methodron.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        Methodron.setFont(font)
        #Methodron.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(Methodron)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.ComputersList = TreeWidget(self.splitter)
        self.ComputersList.setObjectName("ComputersList")
        item_0 = QtWidgets.QTreeWidgetItem(self.ComputersList)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.ComputersList)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.MainWidget = QtWidgets.QWidget(self.splitter)
        self.MainWidget.setObjectName("MainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ComputerInformation = QtWidgets.QFrame(self.MainWidget)
        self.ComputerInformation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ComputerInformation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ComputerInformation.setObjectName("ComputerInformation")
        self.verticalLayout.addWidget(self.ComputerInformation)
        self.Status = QtWidgets.QFrame(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status.sizePolicy().hasHeightForWidth())
        self.Status.setSizePolicy(sizePolicy)
        self.Status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status.setObjectName("Status")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Status)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Status_FileTransfer = QtWidgets.QPushButton(self.Status)
        self.Status_FileTransfer.setCheckable(True)
        self.Status_FileTransfer.setChecked(False)
        self.Status_FileTransfer.setDefault(False)
        self.Status_FileTransfer.setFlat(True)
        self.Status_FileTransfer.setObjectName("Status_FileTransfer")
        self.horizontalLayout.addWidget(self.Status_FileTransfer)
        self.Status_DesktopSharing = QtWidgets.QPushButton(self.Status)
        self.Status_DesktopSharing.setCheckable(True)
        self.Status_DesktopSharing.setChecked(True)
        self.Status_DesktopSharing.setDefault(False)
        self.Status_DesktopSharing.setFlat(True)
        self.Status_DesktopSharing.setObjectName("Status_DesktopSharing")
        self.horizontalLayout.addWidget(self.Status_DesktopSharing)
        self.Status_Connecting = QtWidgets.QPushButton(self.Status)
        self.Status_Connecting.setCheckable(True)
        self.Status_Connecting.setChecked(True)
        self.Status_Connecting.setDefault(False)
        self.Status_Connecting.setFlat(True)
        self.Status_Connecting.setObjectName("Status_Connecting")
        self.horizontalLayout.addWidget(self.Status_Connecting)
        self.verticalLayout.addWidget(self.Status)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        Methodron.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Methodron)
        self.statusbar.setObjectName("statusbar")
        Methodron.setStatusBar(self.statusbar)
        self.MainMenu = QtWidgets.QToolBar(Methodron)
        self.MainMenu.setObjectName("MainMenu")
        Methodron.addToolBar(QtCore.Qt.TopToolBarArea, self.MainMenu)
        self.ActionsMenu = QtWidgets.QToolBar(Methodron)
        self.ActionsMenu.setObjectName("ActionsMenu")
        Methodron.addToolBar(QtCore.Qt.TopToolBarArea, self.ActionsMenu)
        self.RunningModeMenu = QtWidgets.QToolBar(Methodron)
        self.RunningModeMenu.setObjectName("RunningModeMenu")
        Methodron.addToolBar(QtCore.Qt.TopToolBarArea, self.RunningModeMenu)
        self.PermissionsMenu = QtWidgets.QToolBar(Methodron)
        self.PermissionsMenu.setObjectName("PermissionsMenu")
        Methodron.addToolBar(QtCore.Qt.TopToolBarArea, self.PermissionsMenu)
        Methodron.insertToolBarBreak(self.PermissionsMenu)
        self.ico = QtWidgets.QAction(Methodron)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ico.setIcon(icon)
        self.ico.setObjectName("ico")
        self.actionAbout = QtWidgets.QAction(Methodron)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(Methodron)
        self.actionSettings.setObjectName("actionSettings")
        self.actionServerMode = QtWidgets.QAction(Methodron)
        self.actionServerMode.setCheckable(True)
        self.actionServerMode.setObjectName("actionServerMode")
        self.actionCompatibilityMode = QtWidgets.QAction(Methodron)
        self.actionCompatibilityMode.setCheckable(True)
        self.actionCompatibilityMode.setObjectName("actionCompatibilityMode")
        self.actionAdd_Client = QtWidgets.QAction(Methodron)
        self.actionAdd_Client.setObjectName("actionAdd_Client")
        self.actionConnect_To = QtWidgets.QAction(Methodron)
        self.actionConnect_To.setObjectName("actionConnect_To")
        self.actionCombinationMode = QtWidgets.QAction(Methodron)
        self.actionCombinationMode.setCheckable(True)
        self.actionCombinationMode.setObjectName("actionCombinationMode")
        self.actionDisconnect = QtWidgets.QAction(Methodron)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionPermissionManager = QtWidgets.QAction(Methodron)
        self.actionPermissionManager.setObjectName("actionPermissionManager")
        self.actionFileTransfer = QtWidgets.QAction(Methodron)
        self.actionFileTransfer.setCheckable(True)
        self.actionFileTransfer.setObjectName("actionFileTransfer")
        self.actionDesktopSharing = QtWidgets.QAction(Methodron)
        self.actionDesktopSharing.setCheckable(True)
        self.actionDesktopSharing.setObjectName("actionDesktopSharing")
        self.MainMenu.addAction(self.ico)
        self.MainMenu.addSeparator()
        self.MainMenu.addAction(self.actionSettings)
        self.MainMenu.addAction(self.actionAbout)
        self.ActionsMenu.addAction(self.actionCombinationMode)
        self.ActionsMenu.addAction(self.actionServerMode)
        self.ActionsMenu.addAction(self.actionCompatibilityMode)
        self.RunningModeMenu.addAction(self.actionConnect_To)
        self.RunningModeMenu.addAction(self.actionDisconnect)
        self.RunningModeMenu.addAction(self.actionAdd_Client)
        self.PermissionsMenu.addAction(self.actionPermissionManager)
        self.PermissionsMenu.addSeparator()
        self.PermissionsMenu.addAction(self.actionFileTransfer)
        self.PermissionsMenu.addAction(self.actionDesktopSharing)

        self.retranslateUi(Methodron)
        QtCore.QMetaObject.connectSlotsByName(Methodron)

    def retranslateUi(self, Methodron):
        _translate = QtCore.QCoreApplication.translate
        Methodron.setWindowTitle(_translate("Methodron", "Methodron"))
        self.ComputersList.headerItem().setText(0, _translate("Methodron", "Computers"))
        __sortingEnabled = self.ComputersList.isSortingEnabled()
        self.ComputersList.setSortingEnabled(False)
        self.ComputersList.topLevelItem(0).setText(0, _translate("Methodron", "My Company"))
        self.ComputersList.topLevelItem(0).child(0).setText(0, _translate("Methodron", "Another Computer"))
        self.ComputersList.topLevelItem(0).child(1).setText(0, _translate("Methodron", "Print Room"))
        self.ComputersList.topLevelItem(1).setText(0, _translate("Methodron", "Family"))
        self.ComputersList.topLevelItem(1).child(0).setText(0, _translate("Methodron", "My PC"))
        self.ComputersList.topLevelItem(1).child(1).setText(0, _translate("Methodron", "Jezzita\'s PC"))
        self.ComputersList.setSortingEnabled(__sortingEnabled)
        self.Status_FileTransfer.setText(_translate("Methodron", "File Transfer"))
        self.Status_DesktopSharing.setText(_translate("Methodron", "Desktop Sharing"))
        self.Status_Connecting.setText(_translate("Methodron", "Connecting"))
        self.MainMenu.setWindowTitle(_translate("Methodron", "toolBar"))
        self.ActionsMenu.setWindowTitle(_translate("Methodron", "toolBar_2"))
        self.RunningModeMenu.setWindowTitle(_translate("Methodron", "toolBar_3"))
        self.PermissionsMenu.setWindowTitle(_translate("Methodron", "toolBar_4"))
        self.ico.setText(_translate("Methodron", "ico"))
        self.ico.setToolTip(_translate("Methodron", "<html><head/><body><p>Methodron</p></body></html>"))
        self.actionAbout.setText(_translate("Methodron", "About"))
        self.actionSettings.setText(_translate("Methodron", "Settings"))
        self.actionServerMode.setText(_translate("Methodron", "Server Mode"))
        self.actionServerMode.setToolTip(_translate("Methodron", "Allow multiple clients to connect to this computer"))
        self.actionCompatibilityMode.setText(_translate("Methodron", "Compatibility Mode"))
        self.actionCompatibilityMode.setToolTip(_translate("Methodron", "Connect to remote computer using Pure-RCT API"))
        self.actionAdd_Client.setText(_translate("Methodron", "Add Client"))
        self.actionAdd_Client.setToolTip(_translate("Methodron", "Add a client into list"))
        self.actionConnect_To.setText(_translate("Methodron", "Connect"))
        self.actionCombinationMode.setText(_translate("Methodron", "Combination Mode"))
        self.actionCombinationMode.setToolTip(_translate("Methodron", "Establish a connection with the connected computer as if it were working on the same computer"))
        self.actionDisconnect.setText(_translate("Methodron", "Disconnect"))
        self.actionPermissionManager.setText(_translate("Methodron", "Permission Manager"))
        self.actionPermissionManager.setToolTip(_translate("Methodron", "Permission Manager"))
        self.actionFileTransfer.setText(_translate("Methodron", "File Transfer"))
        self.actionFileTransfer.setToolTip(_translate("Methodron", "Apply for file transfer permission"))
        self.actionDesktopSharing.setText(_translate("Methodron", "Desktop Sharing"))
        self.actionDesktopSharing.setToolTip(_translate("Methodron", "Apply for desktop sharing permission"))


import rc_methodron
