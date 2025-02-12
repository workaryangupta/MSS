# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_mscolab_operation_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MscolabOperation(object):
    def setupUi(self, MscolabOperation):
        MscolabOperation.setObjectName("MscolabOperation")
        MscolabOperation.setWindowModality(QtCore.Qt.NonModal)
        MscolabOperation.setEnabled(True)
        MscolabOperation.resize(1066, 687)
        MscolabOperation.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MscolabOperation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.user_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_info.sizePolicy().hasHeightForWidth())
        self.user_info.setSizePolicy(sizePolicy)
        self.user_info.setObjectName("user_info")
        self.horizontalLayout_3.addWidget(self.user_info)
        self.proj_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proj_info.sizePolicy().hasHeightForWidth())
        self.proj_info.setSizePolicy(sizePolicy)
        self.proj_info.setObjectName("proj_info")
        self.horizontalLayout_3.addWidget(self.proj_info)
        spacerItem = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.changes_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changes_info.sizePolicy().hasHeightForWidth())
        self.changes_info.setSizePolicy(sizePolicy)
        self.changes_info.setMinimumSize(QtCore.QSize(266, 0))
        self.changes_info.setObjectName("changes_info")
        self.horizontalLayout_3.addWidget(self.changes_info)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.collaboratorsList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collaboratorsList.sizePolicy().hasHeightForWidth())
        self.collaboratorsList.setSizePolicy(sizePolicy)
        self.collaboratorsList.setMinimumSize(QtCore.QSize(200, 300))
        self.collaboratorsList.setObjectName("collaboratorsList")
        self.horizontalLayout_4.addWidget(self.collaboratorsList)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchMessageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchMessageLineEdit.setObjectName("searchMessageLineEdit")
        self.horizontalLayout_5.addWidget(self.searchMessageLineEdit)
        self.searchPrevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchPrevBtn.setObjectName("searchPrevBtn")
        self.horizontalLayout_5.addWidget(self.searchPrevBtn)
        self.searchNextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchNextBtn.setObjectName("searchNextBtn")
        self.horizontalLayout_5.addWidget(self.searchNextBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.messageList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageList.sizePolicy().hasHeightForWidth())
        self.messageList.setSizePolicy(sizePolicy)
        self.messageList.setMinimumSize(QtCore.QSize(539, 300))
        self.messageList.setObjectName("messageList")
        self.verticalLayout_3.addWidget(self.messageList)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewBtn = QtWidgets.QPushButton(self.centralwidget)
        self.previewBtn.setToolTip("")
        self.previewBtn.setAutoDefault(False)
        self.previewBtn.setDefault(False)
        self.previewBtn.setFlat(False)
        self.previewBtn.setObjectName("previewBtn")
        self.horizontalLayout_2.addWidget(self.previewBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageTextContainer = QtWidgets.QWidget(self.centralwidget)
        self.messageTextContainer.setObjectName("messageTextContainer")
        self.horizontalLayout.addWidget(self.messageTextContainer)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sendMessageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendMessageBtn.setDefault(True)
        self.sendMessageBtn.setObjectName("sendMessageBtn")
        self.verticalLayout.addWidget(self.sendMessageBtn)
        self.uploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayout.addWidget(self.uploadBtn)
        self.editMessageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editMessageBtn.setToolTip("")
        self.editMessageBtn.setObjectName("editMessageBtn")
        self.verticalLayout.addWidget(self.editMessageBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setEnabled(True)
        self.cancelBtn.setObjectName("cancelBtn")
        self.verticalLayout.addWidget(self.cancelBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.serviceMessageList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serviceMessageList.sizePolicy().hasHeightForWidth())
        self.serviceMessageList.setSizePolicy(sizePolicy)
        self.serviceMessageList.setMinimumSize(QtCore.QSize(275, 0))
        self.serviceMessageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.serviceMessageList.setObjectName("serviceMessageList")
        self.horizontalLayout_4.addWidget(self.serviceMessageList)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MscolabOperation.setCentralWidget(self.centralwidget)
        self.actionCloseWindow = QtWidgets.QAction(MscolabOperation)
        self.actionCloseWindow.setObjectName("actionCloseWindow")
        MscolabOperation.addAction(self.actionCloseWindow)

        self.retranslateUi(MscolabOperation)
        self.actionCloseWindow.triggered.connect(MscolabOperation.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MscolabOperation)

    def retranslateUi(self, MscolabOperation):
        _translate = QtCore.QCoreApplication.translate
        MscolabOperation.setWindowTitle(_translate("MscolabOperation", "Mscolab Operation Chat"))
        self.user_info.setText(_translate("MscolabOperation", "Logged In: "))
        self.proj_info.setText(_translate("MscolabOperation", "Operation:"))
        self.changes_info.setText(_translate("MscolabOperation", "Change Log:"))
        self.searchMessageLineEdit.setPlaceholderText(_translate("MscolabOperation", "Search Message"))
        self.searchPrevBtn.setText(_translate("MscolabOperation", "Previous"))
        self.searchNextBtn.setText(_translate("MscolabOperation", "Next"))
        self.previewBtn.setText(_translate("MscolabOperation", "Preview"))
        self.sendMessageBtn.setText(_translate("MscolabOperation", "send"))
        self.uploadBtn.setToolTip(_translate("MscolabOperation", "Upload image or file"))
        self.uploadBtn.setText(_translate("MscolabOperation", "Upload"))
        self.editMessageBtn.setText(_translate("MscolabOperation", "Update"))
        self.cancelBtn.setText(_translate("MscolabOperation", "Cancel"))
        self.actionCloseWindow.setText(_translate("MscolabOperation", "CloseWindow"))
        self.actionCloseWindow.setShortcut(_translate("MscolabOperation", "Ctrl+W"))
