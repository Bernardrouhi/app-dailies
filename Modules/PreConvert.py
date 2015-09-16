def renameAndMove(setImagesPath="",fileType="",name="",zeros=4, destination="",startNum=0):
	import shutil, os
	if zeros > 0:
		files=[]
		for each in os.listdir(setImagesPath):
			if ".%s"%fileType in each:
				files.append(each)
		files.sort()

		num = startNum
		for eachFile in files:
			numS = str(num)
			while len(numS) < zeros:
				numS = "0%s"%numS
			newformat = "%s.%s.%s"%(name,numS,fileType)
			print eachFile, " ", newformat
			num = num + 1
			shutil.copy("%s/%s"%(setImagesPath,eachFile),"%s/%s"%(destination ,newformat))
	return name + ".%" + str(zeros) + "d." + fileType

def resCode(Resolution):
	if "128x96" in Resolution:
		return "sqcif"
	elif "160x120"in Resolution:
		return "qqvga"
	elif "320x200"in Resolution:
		return "cga"
	elif "320x240"in Resolution:
		return "qvga"
	elif "352x288"in Resolution:
		return "cif"
	elif "640x480"in Resolution:
		return "vga"
	elif "704x576"in Resolution:
		return "4cif"
	elif "800x600"in Resolution:
		return "svga"
	elif "852x480"in Resolution:
		return "hd480"
	elif "1024x768"in Resolution:
		return "xga"
	elif "1280x720"in Resolution:
		return "hd720"
	elif "1280x1024"in Resolution:
		return "sxga"
	elif "1366x768"in Resolution:
		return "wxga"
	elif "1600x1024"in Resolution:
		return "wsxga"
	elif "1600x1200"in Resolution:
		return "uxga"
	elif "1920x1200"in Resolution:
		return "wuxga"
	elif "1920x1080"in Resolution:
		return "hd1080"
	elif "2048x1536"in Resolution:
		return "qxga"
	elif "2560x1600"in Resolution:
		return "woxga"
	elif "2560x2048"in Resolution:
		return "qsxga"
	elif "3200x2048"in Resolution:
		return "wqsxga"
	elif "3840x2400"in Resolution:
		return "wquxga"
	elif "5120x4096"in Resolution:
		return "hsxga"
	elif "6400x4096"in Resolution:
		return "whsxga"
	elif "7680x4800"in Resolution:
		return "whuxga"

def FillTheGap(ImagesPath="", fileType="", name="", zeros=4, FrameStart=0):
	import shutil, os
	files = []
	for each in os.listdir(ImagesPath):
			if ".%s"%fileType in each:
				files.append(each)
	files.sort()
	num = 0
	if num < FrameStart:
		while num < FrameStart :
			numS = str(num)
			while len(numS) < zeros:
				numS = "0%s"%numS
			newformat = "%s.%s.%s"%(name,numS,fileType)
			print newformat
			num = num + 1
			shutil.copy("%s/%s"%(ImagesPath,files[0]),"%s/%s"%(ImagesPath,newformat))

def setPreDestination(tempPath="c:/temp/ImageToVideo"):
	import shutil, os
	if os.path.exists(tempPath):
		shutil.rmtree(tempPath, ignore_errors=True)
		os.makedirs(tempPath)
	else:
		os.makedirs(tempPath)
	return tempPath 

def deletePath(SelectedPath):
	'''
	Delete the unnecessary files
	'''
	import shutil
	shutil.rmtree(SelectedPath, ignore_errors=True)

def combineName(sequence, shot, version):
	nameList = [sequence, shot, version]
	finalName = ""
	for each in nameList:
		if finalName:
			if each:
				finalName = "%s-%s"%(finalName,each)
			else:
				finalName = "%s-%s"%(finalName,"Unknown")
		else:
			if each:
				finalName = each
			else:
				finalName = "Unknown"
	return finalName

def frameTotime(TimeValue, FrameRate):
	TimeValue = float("%s.0"%TimeValue)
	FrameRate = float("%s.0"%FrameRate)
	hours = 00
	minutes = 00
	seconds = TimeValue/FrameRate
	if seconds >= 60:
		minutes = int(seconds / 60) 
		seconds = seconds - (minutes * 60)
		if minutes >= 60:
			hours = int(minutes / 60)
			minutes = minutes - (hours * 60)

	return "%s:%s:%s"%(hours,minutes,seconds)