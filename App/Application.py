# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Application.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(920, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(920, 500))
        MainWindow.setMaximumSize(QtCore.QSize(920, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/Icon_PNG.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rit_logo = QtGui.QLabel(self.centralwidget)
        self.rit_logo.setGeometry(QtCore.QRect(-1, -20, 921, 111))
        self.rit_logo.setObjectName(_fromUtf8("rit_logo"))
        self.project_title = QtGui.QLabel(self.centralwidget)
        self.project_title.setGeometry(QtCore.QRect(2, 110, 921, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Manjari"))
        self.project_title.setFont(font)
        self.project_title.setObjectName(_fromUtf8("project_title"))
        self.dsp = QtGui.QCheckBox(self.centralwidget)
        self.dsp.setGeometry(QtCore.QRect(20, 270, 58, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Manjari"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dsp.setFont(font)
        self.dsp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dsp.setMouseTracking(False)
        self.dsp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dsp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dsp.setAcceptDrops(False)
        self.dsp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dsp.setIconSize(QtCore.QSize(0, 0))
        self.dsp.setCheckable(True)
        self.dsp.setChecked(True)
        self.dsp.setAutoExclusive(False)
        self.dsp.setTristate(False)
        self.dsp.setObjectName(_fromUtf8("dsp"))
        self.reset_button_2 = QtGui.QPushButton(self.centralwidget)
        self.reset_button_2.setEnabled(True)
        self.reset_button_2.setGeometry(QtCore.QRect(400, 370, 40, 40))
        self.reset_button_2.setWhatsThis(_fromUtf8(""))
        self.reset_button_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/clear_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button_2.setIcon(icon1)
        self.reset_button_2.setIconSize(QtCore.QSize(25, 25))
        self.reset_button_2.setDefault(False)
        self.reset_button_2.setFlat(False)
        self.reset_button_2.setObjectName(_fromUtf8("reset_button_2"))
        self.listView_2 = QtGui.QListView(self.centralwidget)
        self.listView_2.setEnabled(False)
        self.listView_2.setGeometry(QtCore.QRect(470, 160, 441, 280))
        palette = QtGui.QPalette()
        self.listView_2.setPalette(palette)
        font = QtGui.QFont()
        font.setKerning(True)
        self.listView_2.setFont(font)
        self.listView_2.setMouseTracking(False)
        self.listView_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listView_2.setAutoFillBackground(False)
        self.listView_2.setStyleSheet(_fromUtf8(""))
        self.listView_2.setFrameShape(QtGui.QFrame.Box)
        self.listView_2.setFrameShadow(QtGui.QFrame.Raised)
        self.listView_2.setLineWidth(1)
        self.listView_2.setMidLineWidth(0)
        self.listView_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.syn_button = QtGui.QPushButton(self.centralwidget)
        self.syn_button.setGeometry(QtCore.QRect(400, 190, 40, 40))
        self.syn_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.syn_button.setWhatsThis(_fromUtf8(""))
        self.syn_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/syn_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.syn_button.setIcon(icon2)
        self.syn_button.setIconSize(QtCore.QSize(30, 30))
        self.syn_button.setDefault(True)
        self.syn_button.setFlat(False)
        self.syn_button.setObjectName(_fromUtf8("syn_button"))
        self.kan_input = QtGui.QTextEdit(self.centralwidget)
        self.kan_input.setGeometry(QtCore.QRect(20, 190, 371, 80))
        self.kan_input.setLocale(QtCore.QLocale(QtCore.QLocale.Kannada, QtCore.QLocale.India))
        self.kan_input.setFrameShape(QtGui.QFrame.StyledPanel)
        self.kan_input.setFrameShadow(QtGui.QFrame.Raised)
        self.kan_input.setObjectName(_fromUtf8("kan_input"))
        self.columnView_2 = QtGui.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(10, 160, 441, 280))
        self.columnView_2.setFrameShape(QtGui.QFrame.Box)
        self.columnView_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.columnView_2.setObjectName(_fromUtf8("columnView_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 93, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 901, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(451, 160, 20, 291))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.en_input = QtGui.QTextEdit(self.centralwidget)
        self.en_input.setGeometry(QtCore.QRect(20, 330, 371, 80))
        self.en_input.setFrameShadow(QtGui.QFrame.Raised)
        self.en_input.setObjectName(_fromUtf8("en_input"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 93, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.translate_button = QtGui.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(400, 330, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.translate_button.setFont(font)
        self.translate_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/translate_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.translate_button.setIcon(icon3)
        self.translate_button.setIconSize(QtCore.QSize(25, 25))
        self.translate_button.setObjectName(_fromUtf8("translate_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 400, 107, 9))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.reset_button_1 = QtGui.QPushButton(self.centralwidget)
        self.reset_button_1.setEnabled(True)
        self.reset_button_1.setGeometry(QtCore.QRect(400, 230, 40, 40))
        self.reset_button_1.setWhatsThis(_fromUtf8(""))
        self.reset_button_1.setText(_fromUtf8(""))
        self.reset_button_1.setIcon(icon1)
        self.reset_button_1.setIconSize(QtCore.QSize(25, 25))
        self.reset_button_1.setDefault(False)
        self.reset_button_1.setFlat(False)
        self.reset_button_1.setObjectName(_fromUtf8("reset_button_1"))
        self.previous_button = QtGui.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(810, 390, 40, 40))
        self.previous_button.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon4)
        self.previous_button.setIconSize(QtCore.QSize(40, 40))
        self.previous_button.setFlat(True)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.next_button = QtGui.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(860, 390, 40, 40))
        self.next_button.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon5)
        self.next_button.setIconSize(QtCore.QSize(40, 40))
        self.next_button.setFlat(True)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.play_button = QtGui.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(480, 390, 40, 40))
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_button.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon6)
        self.play_button.setIconSize(QtCore.QSize(40, 40))
        self.play_button.setFlat(True)
        self.play_button.setObjectName(_fromUtf8("play_button"))
        self.stop_button = QtGui.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(530, 390, 40, 40))
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon7)
        self.stop_button.setIconSize(QtCore.QSize(52, 52))
        self.stop_button.setFlat(True)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.play_progress = QtGui.QSlider(self.centralwidget)
        self.play_progress.setEnabled(False)
        self.play_progress.setGeometry(QtCore.QRect(478, 360, 425, 29))
        self.play_progress.setMaximum(100)
        self.play_progress.setPageStep(10)
        self.play_progress.setTracking(True)
        self.play_progress.setOrientation(QtCore.Qt.Horizontal)
        self.play_progress.setTickPosition(QtGui.QSlider.NoTicks)
        self.play_progress.setTickInterval(10)
        self.play_progress.setObjectName(_fromUtf8("play_progress"))
        self.rating = QtGui.QSpinBox(self.centralwidget)
        self.rating.setGeometry(QtCore.QRect(820, 310, 80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.rating.setFont(font)
        self.rating.setAutoFillBackground(False)
        self.rating.setWrapping(False)
        self.rating.setFrame(True)
        self.rating.setAlignment(QtCore.Qt.AlignCenter)
        self.rating.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.rating.setAccelerated(True)
        self.rating.setPrefix(_fromUtf8(""))
        self.rating.setMaximum(10)
        self.rating.setProperty("value", 5)
        self.rating.setObjectName(_fromUtf8("rating"))
        self.waveform_button = QtGui.QPushButton(self.centralwidget)
        self.waveform_button.setGeometry(QtCore.QRect(480, 310, 40, 40))
        self.waveform_button.setAutoFillBackground(True)
        self.waveform_button.setStyleSheet(_fromUtf8(""))
        self.waveform_button.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/waveform.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waveform_button.setIcon(icon8)
        self.waveform_button.setIconSize(QtCore.QSize(35, 35))
        self.waveform_button.setAutoDefault(False)
        self.waveform_button.setDefault(False)
        self.waveform_button.setFlat(False)
        self.waveform_button.setObjectName(_fromUtf8("waveform_button"))
        self.pitch_button = QtGui.QPushButton(self.centralwidget)
        self.pitch_button.setGeometry(QtCore.QRect(580, 310, 40, 40))
        self.pitch_button.setAutoFillBackground(True)
        self.pitch_button.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/pitch_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pitch_button.setIcon(icon9)
        self.pitch_button.setIconSize(QtCore.QSize(30, 30))
        self.pitch_button.setAutoDefault(False)
        self.pitch_button.setDefault(False)
        self.pitch_button.setFlat(False)
        self.pitch_button.setObjectName(_fromUtf8("pitch_button"))
        self.reverse_button = QtGui.QPushButton(self.centralwidget)
        self.reverse_button.setEnabled(False)
        self.reverse_button.setGeometry(QtCore.QRect(530, 250, 40, 40))
        self.reverse_button.setWhatsThis(_fromUtf8(""))
        self.reverse_button.setAutoFillBackground(True)
        self.reverse_button.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/reverse_syn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reverse_button.setIcon(icon10)
        self.reverse_button.setIconSize(QtCore.QSize(30, 30))
        self.reverse_button.setAutoDefault(False)
        self.reverse_button.setDefault(False)
        self.reverse_button.setFlat(False)
        self.reverse_button.setObjectName(_fromUtf8("reverse_button"))
        self.spectrum_button = QtGui.QPushButton(self.centralwidget)
        self.spectrum_button.setGeometry(QtCore.QRect(530, 310, 40, 40))
        self.spectrum_button.setAutoFillBackground(True)
        self.spectrum_button.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/spectrum.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spectrum_button.setIcon(icon11)
        self.spectrum_button.setIconSize(QtCore.QSize(30, 30))
        self.spectrum_button.setAutoDefault(False)
        self.spectrum_button.setDefault(False)
        self.spectrum_button.setFlat(False)
        self.spectrum_button.setObjectName(_fromUtf8("spectrum_button"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(470, 350, 441, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(470, 290, 441, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.noise_red_button = QtGui.QPushButton(self.centralwidget)
        self.noise_red_button.setEnabled(False)
        self.noise_red_button.setGeometry(QtCore.QRect(480, 250, 40, 40))
        self.noise_red_button.setAutoFillBackground(True)
        self.noise_red_button.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/noise_reduction.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noise_red_button.setIcon(icon12)
        self.noise_red_button.setIconSize(QtCore.QSize(30, 30))
        self.noise_red_button.setAutoDefault(False)
        self.noise_red_button.setDefault(False)
        self.noise_red_button.setFlat(False)
        self.noise_red_button.setObjectName(_fromUtf8("noise_red_button"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(470, 230, 441, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 290, 441, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.text_view = QtGui.QTextEdit(self.centralwidget)
        self.text_view.setEnabled(True)
        self.text_view.setGeometry(QtCore.QRect(477, 170, 425, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.text_view.setFont(font)
        self.text_view.setFrameShape(QtGui.QFrame.WinPanel)
        self.text_view.setFrameShadow(QtGui.QFrame.Plain)
        self.text_view.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_view.setObjectName(_fromUtf8("text_view"))
        self.refresh_button = QtGui.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(760, 390, 40, 40))
        self.refresh_button.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_button.setIcon(icon13)
        self.refresh_button.setIconSize(QtCore.QSize(40, 40))
        self.refresh_button.setFlat(True)
        self.refresh_button.setObjectName(_fromUtf8("refresh_button"))
        self.columnView_2.raise_()
        self.listView_2.raise_()
        self.rit_logo.raise_()
        self.project_title.raise_()
        self.dsp.raise_()
        self.reset_button_2.raise_()
        self.syn_button.raise_()
        self.kan_input.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.en_input.raise_()
        self.label_8.raise_()
        self.translate_button.raise_()
        self.label.raise_()
        self.reset_button_1.raise_()
        self.previous_button.raise_()
        self.next_button.raise_()
        self.play_button.raise_()
        self.stop_button.raise_()
        self.play_progress.raise_()
        self.rating.raise_()
        self.waveform_button.raise_()
        self.pitch_button.raise_()
        self.reverse_button.raise_()
        self.spectrum_button.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.noise_red_button.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.text_view.raise_()
        self.refresh_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuView.setTearOffEnabled(False)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDevelopers = QtGui.QAction(MainWindow)
        self.actionDevelopers.setObjectName(_fromUtf8("actionDevelopers"))
        self.actionMentor = QtGui.QAction(MainWindow)
        self.actionMentor.setObjectName(_fromUtf8("actionMentor"))
        self.actionAbout_Project = QtGui.QAction(MainWindow)
        self.actionAbout_Project.setObjectName(_fromUtf8("actionAbout_Project"))
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.actionSynthesized_Text = QtGui.QAction(MainWindow)
        self.actionSynthesized_Text.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionSynthesized_Text.setObjectName(_fromUtf8("actionSynthesized_Text"))
        self.menuAbout.addAction(self.actionDevelopers)
        self.menuAbout.addAction(self.actionMentor)
        self.menuAbout.addAction(self.actionLicense)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuView.addAction(self.actionSynthesized_Text)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kannada Speech Synthesis", None))
        self.rit_logo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/img/img/rit_logo.png\" width=\"250\" height=\"125\"/></p></body></html>", None))
        self.project_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#333333;\">Kannada Speech Synthesis</span></p></body></html>", None))
        self.dsp.setToolTip(_translate("MainWindow", "Apply Signal Processing Operations", None))
        self.dsp.setText(_translate("MainWindow", "DSP", None))
        self.reset_button_2.setToolTip(_translate("MainWindow", "Clear", None))
        self.reset_button_2.setStatusTip(_translate("MainWindow", "Clear English Text", None))
        self.syn_button.setToolTip(_translate("MainWindow", "Synthesize", None))
        self.syn_button.setStatusTip(_translate("MainWindow", "Synthesize", None))
        self.label_7.setText(_translate("MainWindow", "Kannada Text", None))
        self.label_8.setText(_translate("MainWindow", "English Text", None))
        self.translate_button.setToolTip(_translate("MainWindow", "Translate (en-kn)", None))
        self.translate_button.setStatusTip(_translate("MainWindow", "Translate", None))
        self.label.setText(_translate("MainWindow", "Powered by Google Translate", None))
        self.reset_button_1.setToolTip(_translate("MainWindow", "Clear", None))
        self.reset_button_1.setStatusTip(_translate("MainWindow", "Clear Kannada Text", None))
        self.previous_button.setToolTip(_translate("MainWindow", "Previous", None))
        self.previous_button.setStatusTip(_translate("MainWindow", "Previous", None))
        self.next_button.setToolTip(_translate("MainWindow", "Next", None))
        self.next_button.setStatusTip(_translate("MainWindow", "Next", None))
        self.play_button.setToolTip(_translate("MainWindow", "Play", None))
        self.play_button.setStatusTip(_translate("MainWindow", "Play", None))
        self.stop_button.setToolTip(_translate("MainWindow", "Stop", None))
        self.stop_button.setStatusTip(_translate("MainWindow", "Stop", None))
        self.rating.setToolTip(_translate("MainWindow", "User Rating", None))
        self.rating.setSpecialValueText(_translate("MainWindow", "Really..!!", None))
        self.rating.setSuffix(_translate("MainWindow", " /10", None))
        self.waveform_button.setToolTip(_translate("MainWindow", "View Waveform", None))
        self.waveform_button.setStatusTip(_translate("MainWindow", "View Waveform", None))
        self.pitch_button.setToolTip(_translate("MainWindow", "View Pitch Contour", None))
        self.pitch_button.setStatusTip(_translate("MainWindow", "View Pitch Contour", None))
        self.reverse_button.setToolTip(_translate("MainWindow", "Synthesize Reverse Statement", None))
        self.reverse_button.setStatusTip(_translate("MainWindow", "Will be Released in Next Update", None))
        self.spectrum_button.setToolTip(_translate("MainWindow", "View Magnitude Spectrum", None))
        self.spectrum_button.setStatusTip(_translate("MainWindow", "View Magnitude Spectrum", None))
        self.noise_red_button.setToolTip(_translate("MainWindow", "Reduce Noise", None))
        self.noise_red_button.setStatusTip(_translate("MainWindow", "WIll be released in next update", None))
        self.refresh_button.setToolTip(_translate("MainWindow", "Refresh", None))
        self.refresh_button.setStatusTip(_translate("MainWindow", "Refresh", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuView.setTitle(_translate("MainWindow", "View all", None))
        self.actionDevelopers.setText(_translate("MainWindow", "Developers", None))
        self.actionMentor.setText(_translate("MainWindow", "Mentor", None))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project", None))
        self.actionLicense.setText(_translate("MainWindow", "License", None))
        self.actionSynthesized_Text.setText(_translate("MainWindow", "Synthesis", None))

import AppResources_rc