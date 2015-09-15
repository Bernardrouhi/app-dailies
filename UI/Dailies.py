"""
Created on September 7th, 2015
@author: Bernard Rouhi
"""
import os, sys, shutil, subprocess, inspect
from PyQt4 import QtGui, QtCore

os.chdir("..")
below_path =  os.getcwd()
if below_path not in sys.path:
	sys.path.append(below_path)

import Modules.Converter as convert
import Modules.PreConvert as preConvert
reload(convert)
reload(preConvert)

showDailiesWindow = None

class MainWindow(QtGui.QWidget):
	def __init__(self, parent=None):

		QtGui.QWidget.__init__(self,parent)

		#General Setup
		version = 0.1
		self.setWindowIcon(QtGui.QIcon('Icon/Bear_256x256.png'))
		self.setWindowTitle('Dailies Video v%s'%version)
		self.setGeometry(300, 300, 250, 150)
		self.setFixedHeight(500)
		self.setFixedWidth(400)
		# self.setStyleSheet("""
		# 	QComboBox {
		# 	color : rgb(80,80,80);
		# 	}
		# 	""")

		self.setLayout(QtGui.QVBoxLayout())
		self.layout().setContentsMargins(5,5,5,5)
		self.layout().setSpacing(5)

		#Validation
		val_txt = QtCore.QRegExp('[a-zA-Z_]+')
		val_mult = QtCore.QRegExp('[a-zA-Z_0-9\[\]]+')
		val_num = QtCore.QRegExp('[0-9]+')

		general_widget = QtGui.QVBoxLayout()
		general_widget.setContentsMargins(0,0,0,0)
		general_widget.setSpacing(2)
		general_widget.setAlignment(QtCore.Qt.AlignTop)

		self.layout().addLayout(general_widget)

		#>>>>>>>>GROUP>>>>>>>>>>
		movie_info_group = QtGui.QGroupBox('Video Information:')
		movie_info_GPLayout = QtGui.QVBoxLayout()
		movie_info_GPLayout.setContentsMargins(5,5,5,5)
		movie_info_GPLayout.setSpacing(3)
		movie_info_GPLayout.setAlignment(QtCore.Qt.AlignTop)
		#-----------------------

		movie_artist_widget = QtGui.QHBoxLayout()
		movie_artist_widget.setContentsMargins(1,1,1,1)
		movie_artist_widget.setSpacing(2)
		movie_artist_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_info_GPLayout.addLayout(movie_artist_widget)

		## Artist
		staticArtistName = QtGui.QLabel("Artist:")
		staticArtistName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticArtistName.setFixedWidth(74)
		self.getArtistName = QtGui.QLineEdit()
		self.getArtistName.setPlaceholderText("Artist Name...")

		movie_artist_widget.addWidget(staticArtistName)
		movie_artist_widget.addWidget(self.getArtistName)

		#-----------------------
		movie_info_group.setLayout(movie_info_GPLayout)
		general_widget.addWidget(movie_info_group)
		#-----------------------

		movie_sequence_widget = QtGui.QHBoxLayout()
		movie_sequence_widget.setContentsMargins(1,1,1,1)
		movie_sequence_widget.setSpacing(2)
		movie_sequence_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_info_GPLayout.addLayout(movie_sequence_widget)

		## Sequence
		staticSequenceName = QtGui.QLabel("Sequence:")
		staticSequenceName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticSequenceName.setFixedWidth(74)
		self.getSequenceName = QtGui.QLineEdit()
		self.getSequenceName.setPlaceholderText("Sequence Name...")

		movie_sequence_widget.addWidget(staticSequenceName)
		movie_sequence_widget.addWidget(self.getSequenceName)

		#-----------------------
		movie_info_group.setLayout(movie_info_GPLayout)
		general_widget.addWidget(movie_info_group)
		#-----------------------

		movie_shot_widget = QtGui.QHBoxLayout()
		movie_shot_widget.setContentsMargins(1,1,1,1)
		movie_shot_widget.setSpacing(2)
		movie_shot_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_info_GPLayout.addLayout(movie_shot_widget)

		## Shot
		staticShotName = QtGui.QLabel("Shot:")
		staticShotName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticShotName.setFixedWidth(74)
		self.getShotName = QtGui.QLineEdit()
		self.getShotName.setPlaceholderText("Shot Name...")

		movie_shot_widget.addWidget(staticShotName)
		movie_shot_widget.addWidget(self.getShotName)

		#-----------------------
		movie_info_group.setLayout(movie_info_GPLayout)
		general_widget.addWidget(movie_info_group)
		#-----------------------

		movie_task_widget = QtGui.QHBoxLayout()
		movie_task_widget.setContentsMargins(1,1,1,1)
		movie_task_widget.setSpacing(2)
		movie_task_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_info_GPLayout.addLayout(movie_task_widget)

		## Task
		staticTaskName = QtGui.QLabel("Task:")
		staticTaskName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticTaskName.setFixedWidth(74)
		self.getTaskName = QtGui.QLineEdit()
		self.getTaskName.setPlaceholderText("Task Name...")

		movie_task_widget.addWidget(staticTaskName)
		movie_task_widget.addWidget(self.getTaskName)

		#-----------------------
		movie_info_group.setLayout(movie_info_GPLayout)
		general_widget.addWidget(movie_info_group)
		#-----------------------

		movie_version_widget = QtGui.QHBoxLayout()
		movie_version_widget.setContentsMargins(1,1,1,1)
		movie_version_widget.setSpacing(2)
		movie_version_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_info_GPLayout.addLayout(movie_version_widget)

		## Version
		staticVersionName = QtGui.QLabel("Version:")
		staticVersionName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticVersionName.setFixedWidth(74)
		self.getVersionNum = QtGui.QLineEdit()
		self.getVersionNum.setPlaceholderText("Version Name...")

		movie_version_widget.addWidget(staticVersionName)
		movie_version_widget.addWidget(self.getVersionNum)

		#-----------------------
		movie_info_group.setLayout(movie_info_GPLayout)
		general_widget.addWidget(movie_info_group)
		#<<<<<<<<<<<<<<<<<<<<<<<

		#########################################################
		#########################################################

		#Tabs
		self.tab_widget = QtGui.QTabWidget()
		self.tab_widget.setTabPosition(QtGui.QTabWidget.East)
		self.tab_widget.setLayout(QtGui.QVBoxLayout())
		self.tab_widget.layout().setContentsMargins(5,5,5,5)
		self.tab_widget.layout().setSpacing(2)
		self.tab_widget.setSizePolicy(QtGui.QSizePolicy.Minimum,
										QtGui.QSizePolicy.Minimum)

		general_widget.addWidget(self.tab_widget)

		#########################################################
		#Movie Tab
		movie_widget = QtGui.QWidget()
		movie_main_layout = QtGui.QVBoxLayout()
		movie_widget.setLayout(movie_main_layout)
		movie_widget.layout().setContentsMargins(5,5,5,5)
		movie_widget.layout().setSpacing(2)
		movie_widget.layout().setAlignment(QtCore.Qt.AlignTop)
		movie_widget.setSizePolicy(QtGui.QSizePolicy.Minimum,
										QtGui.QSizePolicy.Minimum)

		#>>>>>>>>GROUP>>>>>>>>>>
		movie_read_group = QtGui.QGroupBox('Read Video:')
		movie_read_GPLayout = QtGui.QVBoxLayout()
		movie_read_GPLayout.setContentsMargins(5,5,5,5)
		movie_read_GPLayout.setSpacing(3)
		movie_read_GPLayout.setAlignment(QtCore.Qt.AlignTop)
		#-----------------------

		movie_videoRead_widget = QtGui.QHBoxLayout()
		movie_videoRead_widget.setContentsMargins(1,1,1,1)
		movie_videoRead_widget.setSpacing(2)
		movie_videoRead_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_read_GPLayout.addLayout(movie_videoRead_widget)

		## Video Read
		staticVideoReadName = QtGui.QLabel("Video Path:")
		staticVideoReadName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticVideoReadName.setFixedWidth(80)
		self.getVideoRead = QtGui.QLineEdit()
		self.getVideoRead.setPlaceholderText("Read File...")
		self.getVideoRead.setReadOnly(True)
		actionVideoRead = QtGui.QPushButton('Read File')
		actionVideoRead.released.connect(self.getFilePath)

		movie_videoRead_widget.addWidget(staticVideoReadName)
		movie_videoRead_widget.addWidget(self.getVideoRead)
		movie_videoRead_widget.addWidget(actionVideoRead)

		#-----------------------
		movie_read_group.setLayout(movie_read_GPLayout)
		movie_main_layout.addWidget(movie_read_group)
		#-----------------------

		movie_res_widget = QtGui.QHBoxLayout()
		movie_res_widget.setContentsMargins(1,1,1,1)
		movie_res_widget.setSpacing(2)
		movie_res_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_read_GPLayout.addLayout(movie_res_widget)

		## Video Resolution
		staticReadResName = QtGui.QLabel("Resolution:")
		staticReadResName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticReadResName.setFixedWidth(80)
		self.getReadResComb= QtGui.QComboBox()
		self.getReadResComb.addItem("128x96")
		self.getReadResComb.addItem("160x120")
		self.getReadResComb.addItem("320x200")
		self.getReadResComb.addItem("320x240")
		self.getReadResComb.addItem("352x288")
		self.getReadResComb.addItem("640x480")
		self.getReadResComb.addItem("704x576")
		self.getReadResComb.addItem("800x600")
		self.getReadResComb.addItem("852x480")
		self.getReadResComb.addItem("1024x768")
		self.getReadResComb.addItem("1280x720")
		self.getReadResComb.addItem("1280x1024")
		self.getReadResComb.addItem("1366x768")
		self.getReadResComb.addItem("1600x1024")
		self.getReadResComb.addItem("1600x1200")
		self.getReadResComb.addItem("1920x1200")
		self.getReadResComb.addItem("1920x1080")
		self.getReadResComb.addItem("2048x1536")
		self.getReadResComb.addItem("2560x1600")
		self.getReadResComb.addItem("2560x2048")
		self.getReadResComb.addItem("3200x2048")
		self.getReadResComb.addItem("3840x2400")
		self.getReadResComb.addItem("5120x4096")
		self.getReadResComb.addItem("6400x4096")
		self.getReadResComb.addItem("7680x4800")

		movie_res_widget.addWidget(staticReadResName)
		movie_res_widget.addWidget(self.getReadResComb)

		#-----------------------
		movie_read_group.setLayout(movie_read_GPLayout)
		movie_main_layout.addWidget(movie_read_group)
		#-----------------------

		movie_framerate_widget = QtGui.QHBoxLayout()
		movie_framerate_widget.setContentsMargins(1,1,1,1)
		movie_framerate_widget.setSpacing(2)
		movie_framerate_widget.setAlignment(QtCore.Qt.AlignTop)

		movie_read_GPLayout.addLayout(movie_framerate_widget)

		## Video Frame Rate
		staticFrameRateName = QtGui.QLabel("Frame Rate:")
		staticFrameRateName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticFrameRateName.setFixedWidth(80)
		self.getFrameRateComb= QtGui.QComboBox()
		self.getFrameRateComb.addItem("24")
		self.getFrameRateComb.addItem("25")
		self.getFrameRateComb.addItem("30")

		movie_framerate_widget.addWidget(staticFrameRateName)
		movie_framerate_widget.addWidget(self.getFrameRateComb)

		#-----------------------
		movie_read_group.setLayout(movie_read_GPLayout)
		movie_main_layout.addWidget(movie_read_group)
		#<<<<<<<<<<<<<<<<<<<<<<<

		self.tab_widget.layout().addWidget(movie_widget)
		self.tab_widget.addTab(movie_widget,"Video")
		#########################################################
		#########################################################
		#Image Tab
		image_widget = QtGui.QWidget()
		image_main_layout = QtGui.QVBoxLayout()
		image_widget.setLayout(image_main_layout)
		image_widget.layout().setContentsMargins(5,5,5,5)
		image_widget.layout().setSpacing(2)
		image_widget.layout().setAlignment(QtCore.Qt.AlignTop)
		image_widget.setSizePolicy(QtGui.QSizePolicy.Minimum,
										QtGui.QSizePolicy.Minimum)

		#>>>>>>>>GROUP>>>>>>>>>>
		image_read_group = QtGui.QGroupBox('Read Images:')
		image_read_GPLayout = QtGui.QVBoxLayout()
		image_read_GPLayout.setContentsMargins(5,5,5,5)
		image_read_GPLayout.setSpacing(3)
		image_read_GPLayout.setAlignment(QtCore.Qt.AlignTop)
		#-----------------------

		image_videoRead_widget = QtGui.QHBoxLayout()
		image_videoRead_widget.setContentsMargins(1,1,1,1)
		image_videoRead_widget.setSpacing(2)
		image_videoRead_widget.setAlignment(QtCore.Qt.AlignTop)

		image_read_GPLayout.addLayout(image_videoRead_widget)

		## Image Read
		staticImageReadName = QtGui.QLabel("Images Path:")
		staticImageReadName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticImageReadName.setFixedWidth(80)
		self.getImageRead = QtGui.QLineEdit()
		self.getImageRead.setPlaceholderText("Read From...")
		self.getImageRead.setReadOnly(True)
		actionImageRead = QtGui.QPushButton('Read Files')
		actionImageRead.released.connect(self.getImagePath)

		image_videoRead_widget.addWidget(staticImageReadName)
		image_videoRead_widget.addWidget(self.getImageRead)
		image_videoRead_widget.addWidget(actionImageRead)

		#-----------------------
		image_read_group.setLayout(image_read_GPLayout)
		image_main_layout.addWidget(image_read_group)
		#-----------------------

		image_type_widget = QtGui.QHBoxLayout()
		image_type_widget.setContentsMargins(1,1,1,1)
		image_type_widget.setSpacing(2)
		image_type_widget.setAlignment(QtCore.Qt.AlignTop)

		image_read_GPLayout.addLayout(image_type_widget)

		## Image Resolution
		staticImageTypeName = QtGui.QLabel("Image Type:")
		staticImageTypeName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticImageTypeName.setFixedWidth(80)
		self.getImageTypeComb= QtGui.QComboBox()
		self.getImageTypeComb.addItem("jpg")
		self.getImageTypeComb.addItem("png")
		self.getImageTypeComb.addItem("bmp")

		image_type_widget.addWidget(staticImageTypeName)
		image_type_widget.addWidget(self.getImageTypeComb)

		#-----------------------
		image_read_group.setLayout(image_read_GPLayout)
		image_main_layout.addWidget(image_read_group)
		#<<<<<<<<<<<<<<<<<<<<<<<

		self.tab_widget.layout().addWidget(image_widget)
		self.tab_widget.addTab(image_widget,"Images")
		#########################################################

		#-----------------------
		Write_widget = QtGui.QVBoxLayout()
		Write_widget.setContentsMargins(0,0,0,0)
		Write_widget.setSpacing(2)
		Write_widget.setAlignment(QtCore.Qt.AlignTop)

		self.layout().addLayout(Write_widget)

		#>>>>>>>>GROUP>>>>>>>>>>
		write_group = QtGui.QGroupBox('Write:')
		write_GPLayout = QtGui.QVBoxLayout()
		write_GPLayout.setContentsMargins(5,5,5,5)
		write_GPLayout.setSpacing(3)
		write_GPLayout.setAlignment(QtCore.Qt.AlignTop)
		#-----------------------

		write_path_widget = QtGui.QHBoxLayout()
		write_path_widget.setContentsMargins(1,1,1,1)
		write_path_widget.setSpacing(2)
		write_path_widget.setAlignment(QtCore.Qt.AlignTop)

		write_GPLayout.addLayout(write_path_widget)

		## Video write
		staticWriteName = QtGui.QLabel("Write Video:")
		staticWriteName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticWriteName.setFixedWidth(74)
		self.getWritePath = QtGui.QLineEdit()
		self.getWritePath.setPlaceholderText("Write to...")
		self.getWritePath.setReadOnly(True)
		actionWritePath = QtGui.QPushButton('Write to')
		actionWritePath.released.connect(self.setDestination)
		# actionVideowrite.released.connect(self.getImagePath)

		write_path_widget.addWidget(staticWriteName)
		write_path_widget.addWidget(self.getWritePath)
		write_path_widget.addWidget(actionWritePath)

		#-----------------------
		write_group.setLayout(write_GPLayout)
		Write_widget.addWidget(write_group)
		#-----------------------

		write_Res_widget = QtGui.QHBoxLayout()
		write_Res_widget.setContentsMargins(1,1,1,1)
		write_Res_widget.setSpacing(2)
		write_Res_widget.setAlignment(QtCore.Qt.AlignTop)

		write_GPLayout.addLayout(write_Res_widget)

		## Video Resolution
		staticImageWriteResName = QtGui.QLabel("Write Res:")
		staticImageWriteResName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticImageWriteResName.setFixedWidth(74)
		self.getImageWriteResComb= QtGui.QComboBox()
		self.getImageWriteResComb.addItem("4K Ultra HD [4096x2160]")
		self.getImageWriteResComb.addItem("1080p Full HD [1920x1080]")
		self.getImageWriteResComb.addItem("720p HD [1280x720]")

		write_Res_widget.addWidget(staticImageWriteResName)
		write_Res_widget.addWidget(self.getImageWriteResComb)

		#-----------------------
		write_group.setLayout(write_GPLayout)
		Write_widget.addWidget(write_group)
		#-----------------------

		write_framerate_widget = QtGui.QHBoxLayout()
		write_framerate_widget.setContentsMargins(1,1,1,1)
		write_framerate_widget.setSpacing(2)
		write_framerate_widget.setAlignment(QtCore.Qt.AlignTop)

		write_GPLayout.addLayout(write_framerate_widget)

		## Video Frame Rate
		staticWriteFrameRateName = QtGui.QLabel("Frame Rate:")
		staticWriteFrameRateName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticWriteFrameRateName.setFixedWidth(74)
		self.getWriteFrameRateComb= QtGui.QComboBox()
		self.getWriteFrameRateComb.addItem("24")
		self.getWriteFrameRateComb.addItem("25")
		self.getWriteFrameRateComb.addItem("30")

		write_framerate_widget.addWidget(staticWriteFrameRateName)
		write_framerate_widget.addWidget(self.getWriteFrameRateComb)

		#-----------------------
		write_group.setLayout(write_GPLayout)
		Write_widget.addWidget(write_group)
		#-----------------------

		write_startframe_widget = QtGui.QHBoxLayout()
		write_startframe_widget.setContentsMargins(1,1,1,1)
		write_startframe_widget.setSpacing(2)
		write_startframe_widget.setAlignment(QtCore.Qt.AlignTop)

		write_GPLayout.addLayout(write_startframe_widget)

		## Video Frame Rate
		staticWriteStartFrameName = QtGui.QLabel("Start Frame:")
		staticWriteStartFrameName.setAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignRight|QtCore.Qt.AlignCenter)
		staticWriteStartFrameName.setFixedWidth(74)
		self.getWriteStartFrame= QtGui.QLineEdit()
		self.getWriteStartFrame.setPlaceholderText("Start Frame From...")
		StartFrame_validator = QtGui.QRegExpValidator(val_num,self.getWriteStartFrame)
		self.getWriteStartFrame.setValidator(StartFrame_validator)

		write_startframe_widget.addWidget(staticWriteStartFrameName)
		write_startframe_widget.addWidget(self.getWriteStartFrame)

		#-----------------------
		write_group.setLayout(write_GPLayout)
		Write_widget.addWidget(write_group)
		#<<<<<<<<<<<<<<<<<<<<<<<

		write_action_widget = QtGui.QHBoxLayout()
		write_action_widget.setContentsMargins(0,0,0,0)
		write_action_widget.setSpacing(2)
		write_action_widget.setAlignment(QtCore.Qt.AlignTop)

		self.layout().addLayout(write_action_widget)

		## Write it
		actionWriteVideo = QtGui.QPushButton("Convert")
		actionWriteVideo.released.connect(self.convert)

		write_action_widget.addWidget(actionWriteVideo)
		#-----------------------

		self.getArtistName.setText("Bernard Rouhi")
	def getImagePath(self):
		MyPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
		self.getImageRead.setText(MyPath)

	def getFilePath(self):
		filters = "Select file"
		selected_filter = "Videos (*.mov *.mp4 *.mpg)"
		MyPath = str(QtGui.QFileDialog.getOpenFileName(self, "Select Directory",filters, selected_filter))
		self.getVideoRead.setText(MyPath)

	def getPaths(self):
		mainPaths = open("MainPaths.txt","r")
		lines = (mainPaths.read()).splitlines()
		paths = {}
		for eachline in lines:
			print eachline
			if "FFMPEG Path:" in eachline:
				paths["FFMPEG"] =  (eachline.replace("FFMPEG Path:","")).replace(" ", "")
		return paths

	def convert(self):
		artistName = (self.getArtistName.text()).replace(" ","-")
		if not artistName:
			artistName = "Unknown"
		sequenceName = self.getSequenceName.text()
		shotName = self.getShotName.text()
		taskName = self.getTaskName.text()
		if not taskName:
			taskName = "Unknown"
		versionNum = self.getVersionNum.text()
		if not versionNum:
			versionNum = "Unknown"
		if self.getWriteStartFrame.text():
			frameStrat = int(self.getWriteStartFrame.text())
		else:
			frameStrat = 0

		sequenceName = preConvert.combineName(sequence=sequenceName, shot=shotName, version=versionNum)
		frameRate = int(self.getWriteFrameRateComb.currentText())
		finalResolution = ((str(self.getImageWriteResComb.currentText())).split("[")[-1]).replace("]","")
		finalDestination = (str(self.getWritePath.text())).replace("\\","/")
		if finalDestination:
			if self.tab_widget.currentIndex() == 0:
				videoPath 		= self.getVideoRead.text()
				videoResolution = preConvert.resCode(Resolution = str(self.getReadResComb.currentText()))
				videoFrameRate  = int(self.getFrameRateComb.currentText())
				pathDic = convert.getPaths()
				prePath = preConvert.setPreDestination(tempPath="c:/temp/ImageToVideo/%s"%sequenceName)
				preVideoPath = preConvert.setPreDestination(tempPath="%s/Video"%prePath)
				if videoPath:
					ImageName = convert.video2images(
						ffmpegPath = pathDic["FFMPEG"] ,
						VideoSource = videoPath ,
						VideoName = sequenceName ,
						ImageDestination = preVideoPath ,
						Resolution = videoResolution,
						FrameRate = videoFrameRate ,
						Zeros = 5
						)
					ImageName = preConvert.renameAndMove(
						setImagesPath = preVideoPath ,
						fileType = "png" ,
						name = sequenceName ,
						zeros = 5 , 
						destination = prePath ,
						startNum = frameStrat
						)
					textBurn = convert.textDecoration(ArtistN=artistName, SequenceN=sequenceName, TaskN=taskName, FrameN=True, TimeCode=True)
					if frameStrat != 0:
						preConvert.FillTheGap(
							ImagesPath = prePath ,
							fileType = "png" ,
							name = sequenceName ,
							zeros = 5 ,
							FrameStart = frameStrat
							)
					offsetT = preConvert.frameTotime(TimeValue=frameStrat, FrameRate=frameRate)
					convert.images2video(
						ffmpegPath = pathDic["FFMPEG"],
						ImageSource = "%s/%s"%(prePath,ImageName) ,
						VideoDestination = "%s/%s.mov"%(finalDestination,sequenceName) ,
						TextBurn = textBurn , 
						Resolution = finalResolution ,
						FrameRate = frameRate ,
						OffsetTime = offsetT
						)
				preConvert.deletePath(SelectedPath=prePath)
			if self.tab_widget.currentIndex() == 1:
				imageSource = (str(self.getImageRead.text())).replace("\\","/")
				imageType = str(self.getImageTypeComb.currentText())
				pathDic = convert.getPaths()
				textBurn = convert.textDecoration(ArtistN=artistName, SequenceN=sequenceName, TaskN=taskName, FrameN=True, TimeCode=True)
				prePath = preConvert.setPreDestination(tempPath="c:/temp/ImageToVideo/%s"%sequenceName)
				if imageSource:
					ImageName = preConvert.renameAndMove(
						setImagesPath = imageSource ,
						fileType = imageType ,
						name = sequenceName ,
						zeros = 5 , 
						destination = prePath ,
						startNum = frameStrat
						)
					if frameStrat != 0:
						preConvert.FillTheGap(
							ImagesPath = prePath ,
							fileType = imageType ,
							name = sequenceName ,
							zeros = 5 ,
							FrameStart = frameStrat
							)
					offsetT = preConvert.frameTotime(TimeValue=frameStrat, FrameRate=frameRate)
					convert.images2video(
						ffmpegPath = pathDic["FFMPEG"],
						ImageSource = "%s/%s"%(prePath,ImageName) ,
						VideoDestination = "%s/%s.mov"%(finalDestination,sequenceName) ,
						TextBurn = textBurn , 
						Resolution = finalResolution ,
						FrameRate = frameRate ,
						OffsetTime = offsetT
						)
				preConvert.deletePath(SelectedPath=prePath)

	def setDestination(self):
		MyPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Save To"))
		self.getWritePath.setText(MyPath)

def create():
	global showDailiesWindow
	app = QtGui.QApplication(sys.argv)
	if showDailiesWindow is None:
		showDailiesWindow = MainWindow()
	showDailiesWindow.show()
	sys.exit(app.exec_())

def delete():
	global showDailiesWindow
	if showDailiesWindow is None:
		return
	showDailiesWindow.deleteLater()
	showDailiesWindow = None

if __name__ == '__main__':
	create()