# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyplane/gui/Ui_SystemTabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SystemTabWidget(object):
    def setupUi(self, SystemTabWidget):
        SystemTabWidget.setObjectName("SystemTabWidget")
        SystemTabWidget.resize(639, 541)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SystemTabWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(SystemTabWidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.ppTab = QtWidgets.QWidget()
        self.ppTab.setObjectName("ppTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ppTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ppLayout = QtWidgets.QVBoxLayout()
        self.ppLayout.setObjectName("ppLayout")
        self.ppPlaceholder = QtWidgets.QWidget(self.ppTab)
        self.ppPlaceholder.setObjectName("ppPlaceholder")
        self.ppLayout.addWidget(self.ppPlaceholder)
        self.verticalLayout.addLayout(self.ppLayout)
        self.tabWidget.addTab(self.ppTab, "")
        self.xTab = QtWidgets.QWidget()
        self.xTab.setObjectName("xTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.xTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.xLayout = QtWidgets.QVBoxLayout()
        self.xLayout.setObjectName("xLayout")
        self.xPlaceholder = QtWidgets.QWidget(self.xTab)
        self.xPlaceholder.setObjectName("xPlaceholder")
        self.xLayout.addWidget(self.xPlaceholder)
        self.verticalLayout_2.addLayout(self.xLayout)
        self.tabWidget.addTab(self.xTab, "")
        self.yTab = QtWidgets.QWidget()
        self.yTab.setObjectName("yTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.yTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.yLayout = QtWidgets.QVBoxLayout()
        self.yLayout.setObjectName("yLayout")
        self.yPlaceholder = QtWidgets.QWidget(self.yTab)
        self.yPlaceholder.setObjectName("yPlaceholder")
        self.yLayout.addWidget(self.yPlaceholder)
        self.verticalLayout_3.addLayout(self.yLayout)
        self.tabWidget.addTab(self.yTab, "")
        self.tTab = QtWidgets.QWidget()
        self.tTab.setObjectName("tTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tLayout = QtWidgets.QVBoxLayout()
        self.tLayout.setObjectName("tLayout")
        self.tPlaceholder = QtWidgets.QWidget(self.tTab)
        self.tPlaceholder.setObjectName("tPlaceholder")
        self.tLayout.addWidget(self.tPlaceholder)
        self.verticalLayout_5.addLayout(self.tLayout)
        self.tabWidget.addTab(self.tTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(SystemTabWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SystemTabWidget)

    def retranslateUi(self, SystemTabWidget):
        _translate = QtCore.QCoreApplication.translate
        SystemTabWidget.setWindowTitle(_translate("SystemTabWidget", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ppTab), _translate("SystemTabWidget", "Phase Plane"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xTab), _translate("SystemTabWidget", "x(t)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yTab), _translate("SystemTabWidget", "y(t)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tTab), _translate("SystemTabWidget", "t(x,y)"))
