# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyplane/gui/Ui_ZoomWidgetSimple.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZoomWidgetSimple(object):
    def setupUi(self, ZoomWidgetSimple):
        ZoomWidgetSimple.setObjectName("ZoomWidgetSimple")
        ZoomWidgetSimple.resize(662, 593)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ZoomWidgetSimple)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(ZoomWidgetSimple)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.tminLabel = QtWidgets.QLabel(ZoomWidgetSimple)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tminLabel.setFont(font)
        self.tminLabel.setObjectName("tminLabel")
        self.verticalLayout.addWidget(self.tminLabel)
        self.xminLineEdit = QtWidgets.QLineEdit(ZoomWidgetSimple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xminLineEdit.sizePolicy().hasHeightForWidth())
        self.xminLineEdit.setSizePolicy(sizePolicy)
        self.xminLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.verticalLayout.addWidget(self.xminLineEdit)
        self.tmaxLabel = QtWidgets.QLabel(ZoomWidgetSimple)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tmaxLabel.setFont(font)
        self.tmaxLabel.setObjectName("tmaxLabel")
        self.verticalLayout.addWidget(self.tmaxLabel)
        self.xmaxLineEdit = QtWidgets.QLineEdit(ZoomWidgetSimple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmaxLineEdit.sizePolicy().hasHeightForWidth())
        self.xmaxLineEdit.setSizePolicy(sizePolicy)
        self.xmaxLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.verticalLayout.addWidget(self.xmaxLineEdit)
        self.param_minLabel = QtWidgets.QLabel(ZoomWidgetSimple)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.param_minLabel.setFont(font)
        self.param_minLabel.setObjectName("param_minLabel")
        self.verticalLayout.addWidget(self.param_minLabel)
        self.yminLineEdit = QtWidgets.QLineEdit(ZoomWidgetSimple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yminLineEdit.sizePolicy().hasHeightForWidth())
        self.yminLineEdit.setSizePolicy(sizePolicy)
        self.yminLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.yminLineEdit.setObjectName("yminLineEdit")
        self.verticalLayout.addWidget(self.yminLineEdit)
        self.param_maxLabel = QtWidgets.QLabel(ZoomWidgetSimple)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.param_maxLabel.setFont(font)
        self.param_maxLabel.setObjectName("param_maxLabel")
        self.verticalLayout.addWidget(self.param_maxLabel)
        self.ymaxLineEdit = QtWidgets.QLineEdit(ZoomWidgetSimple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymaxLineEdit.sizePolicy().hasHeightForWidth())
        self.ymaxLineEdit.setSizePolicy(sizePolicy)
        self.ymaxLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.ymaxLineEdit.setObjectName("ymaxLineEdit")
        self.verticalLayout.addWidget(self.ymaxLineEdit)
        self.SetButton = QtWidgets.QPushButton(ZoomWidgetSimple)
        self.SetButton.setObjectName("SetButton")
        self.verticalLayout.addWidget(self.SetButton)
        self.ZoomButton = QtWidgets.QPushButton(ZoomWidgetSimple)
        self.ZoomButton.setObjectName("ZoomButton")
        self.verticalLayout.addWidget(self.ZoomButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mpl_layout = QtWidgets.QVBoxLayout()
        self.mpl_layout.setObjectName("mpl_layout")
        self.frame = QtWidgets.QWidget(ZoomWidgetSimple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(444, 0))
        self.frame.setObjectName("frame")
        self.mpl_layout.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.mpl_layout)

        self.retranslateUi(ZoomWidgetSimple)
        QtCore.QMetaObject.connectSlotsByName(ZoomWidgetSimple)

    def retranslateUi(self, ZoomWidgetSimple):
        _translate = QtCore.QCoreApplication.translate
        ZoomWidgetSimple.setWindowTitle(_translate("ZoomWidgetSimple", "Form"))
        self.label_9.setText(_translate("ZoomWidgetSimple", "Window Range"))
        self.tminLabel.setText(_translate("ZoomWidgetSimple", "tmin"))
        self.tmaxLabel.setText(_translate("ZoomWidgetSimple", "tmax"))
        self.param_minLabel.setText(_translate("ZoomWidgetSimple", "xmin"))
        self.param_maxLabel.setText(_translate("ZoomWidgetSimple", "xmax"))
        self.SetButton.setText(_translate("ZoomWidgetSimple", "Set"))
        self.ZoomButton.setText(_translate("ZoomWidgetSimple", "Zoom"))
