# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyplane/gui/Ui_ZoomWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZoomWidget(object):
    def setupUi(self, ZoomWidget):
        ZoomWidget.setObjectName("ZoomWidget")
        ZoomWidget.resize(795, 587)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ZoomWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(ZoomWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.xminLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xminLineEdit.sizePolicy().hasHeightForWidth())
        self.xminLineEdit.setSizePolicy(sizePolicy)
        self.xminLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.verticalLayout.addWidget(self.xminLineEdit)
        self.label_2 = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.xmaxLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmaxLineEdit.sizePolicy().hasHeightForWidth())
        self.xmaxLineEdit.setSizePolicy(sizePolicy)
        self.xmaxLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.verticalLayout.addWidget(self.xmaxLineEdit)
        self.label_3 = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.yminLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yminLineEdit.sizePolicy().hasHeightForWidth())
        self.yminLineEdit.setSizePolicy(sizePolicy)
        self.yminLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.yminLineEdit.setObjectName("yminLineEdit")
        self.verticalLayout.addWidget(self.yminLineEdit)
        self.label_4 = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ymaxLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymaxLineEdit.sizePolicy().hasHeightForWidth())
        self.ymaxLineEdit.setSizePolicy(sizePolicy)
        self.ymaxLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.ymaxLineEdit.setObjectName("ymaxLineEdit")
        self.verticalLayout.addWidget(self.ymaxLineEdit)
        self.SetButton = QtWidgets.QPushButton(ZoomWidget)
        self.SetButton.setObjectName("SetButton")
        self.verticalLayout.addWidget(self.SetButton)
        self.ZoomButton = QtWidgets.QPushButton(ZoomWidget)
        self.ZoomButton.setObjectName("ZoomButton")
        self.verticalLayout.addWidget(self.ZoomButton)
        self.RefreshButton = QtWidgets.QPushButton(ZoomWidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.verticalLayout.addWidget(self.RefreshButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(ZoomWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.forwardCheckbox = QtWidgets.QCheckBox(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.forwardCheckbox.setFont(font)
        self.forwardCheckbox.setObjectName("forwardCheckbox")
        self.verticalLayout.addWidget(self.forwardCheckbox)
        self.backwardCheckbox = QtWidgets.QCheckBox(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.backwardCheckbox.setFont(font)
        self.backwardCheckbox.setObjectName("backwardCheckbox")
        self.verticalLayout.addWidget(self.backwardCheckbox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(ZoomWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.xinitLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xinitLineEdit.sizePolicy().hasHeightForWidth())
        self.xinitLineEdit.setSizePolicy(sizePolicy)
        self.xinitLineEdit.setObjectName("xinitLineEdit")
        self.verticalLayout.addWidget(self.xinitLineEdit)
        self.label_8 = QtWidgets.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.yinitLineEdit = QtWidgets.QLineEdit(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yinitLineEdit.sizePolicy().hasHeightForWidth())
        self.yinitLineEdit.setSizePolicy(sizePolicy)
        self.yinitLineEdit.setObjectName("yinitLineEdit")
        self.verticalLayout.addWidget(self.yinitLineEdit)
        self.CreateTrajectoryButton = QtWidgets.QPushButton(ZoomWidget)
        self.CreateTrajectoryButton.setObjectName("CreateTrajectoryButton")
        self.verticalLayout.addWidget(self.CreateTrajectoryButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.linLabel = QtWidgets.QLabel(ZoomWidget)
        self.linLabel.setObjectName("linLabel")
        self.verticalLayout.addWidget(self.linLabel)
        self.linBox = QtWidgets.QComboBox(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linBox.sizePolicy().hasHeightForWidth())
        self.linBox.setSizePolicy(sizePolicy)
        self.linBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.linBox.setObjectName("linBox")
        self.verticalLayout.addWidget(self.linBox)
        self.linButton = QtWidgets.QPushButton(ZoomWidget)
        self.linButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.linButton.setObjectName("linButton")
        self.verticalLayout.addWidget(self.linButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mpl_layout = QtWidgets.QVBoxLayout()
        self.mpl_layout.setObjectName("mpl_layout")
        self.frame = QtWidgets.QWidget(ZoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(444, 0))
        self.frame.setObjectName("frame")
        self.mpl_layout.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.mpl_layout)

        self.retranslateUi(ZoomWidget)
        QtCore.QMetaObject.connectSlotsByName(ZoomWidget)

    def retranslateUi(self, ZoomWidget):
        _translate = QtCore.QCoreApplication.translate
        ZoomWidget.setWindowTitle(_translate("ZoomWidget", "Form"))
        self.label_9.setText(_translate("ZoomWidget", "Window Range"))
        self.label.setText(_translate("ZoomWidget", "xmin"))
        self.label_2.setText(_translate("ZoomWidget", "xmax"))
        self.label_3.setText(_translate("ZoomWidget", "ymin"))
        self.label_4.setText(_translate("ZoomWidget", "ymax"))
        self.SetButton.setText(_translate("ZoomWidget", "Set"))
        self.ZoomButton.setText(_translate("ZoomWidget", "Zoom"))
        self.RefreshButton.setText(_translate("ZoomWidget", "Refresh"))
        self.label_5.setText(_translate("ZoomWidget", "Integration"))
        self.forwardCheckbox.setText(_translate("ZoomWidget", "Forward"))
        self.backwardCheckbox.setText(_translate("ZoomWidget", "Backward"))
        self.label_6.setText(_translate("ZoomWidget", "Initial Condition"))
        self.label_7.setText(_translate("ZoomWidget", "x-Coordinate"))
        self.label_8.setText(_translate("ZoomWidget", "y-Coordinate"))
        self.CreateTrajectoryButton.setText(_translate("ZoomWidget", "Create"))
        self.linLabel.setText(_translate("ZoomWidget", "Linearization"))
        self.linButton.setText(_translate("ZoomWidget", "Linearize"))
