def textDecoration(ArtistN="", SequenceN="", TaskN="", FrameN=True, TimeCode=False, Resolution = 25):
	allData = []
	if ArtistN:
		allData.append("drawtext=fontfile='C\:/Windows/fonts/arial.ttf':fontsize=18:text=%s:r=%s:x=0:y=5:fontcolor=0xFFFFFF99:box=1:boxborderw=2:boxcolor=0x0F0F0F55"%(ArtistN,Resolution))
	if SequenceN:
		allData.append("drawtext=fontfile='C\:/Windows/fonts/arial.ttf':fontsize=18:text=%s:r=%s:x=0:y=h-(1.5*lh):fontcolor=0xFFFFFF99:box=1:boxborderw=2:boxcolor=0x0F0F0F55"%(SequenceN,Resolution))
	if TaskN:
		allData.append("drawtext=fontfile='C\:/Windows/fonts/arial.ttf':fontsize=18:text=%s:r=%s:x=(w-tw):y=5:fontcolor=0xFFFFFF99:box=1:boxborderw=2:boxcolor=0x0F0F0F55"%(TaskN,Resolution))
	if FrameN:
		Num = "%{n}"
		allData.append("drawtext=fontfile='C\:/Windows/fonts/arial.ttf':fontsize=18:text=%s:r=%s:x=(w-tw):y=h-(1.5*lh):fontcolor=0xFFFFFF99:box=1:boxborderw=2:boxcolor=0x0F0F0F55"%(Num,Resolution))
	if TimeCode:
		allData.append("drawtext=fontfile='C\:/Windows/fonts/arial.ttf':fontsize=22: timecode='00\:00\:00\:00': r=%s: x=(w-tw)/2: y=h-(1.5*lh): fontcolor=0xFFFFFF90: box=1: boxborderw=2: boxcolor=0x0F0F0F88"%Resolution)

	finalData = ""
	for data in allData:
		if finalData == "":
			finalData = "[in]%s"%data
		else:
			finalData = "%s , %s"%(finalData,data)
	finalData = finalData + "[out]"
	return finalData

def video2images(ffmpegPath, VideoSource, VideoName , ImageDestination, Resolution, FrameRate, Zeros):
	import os
	ffmpegSource = "%s\\bin\\ffmpeg.exe"%ffmpegPath
	ImageName = VideoName + ".%" + str(Zeros) + "d" + ".png"
	os.system('%s -i "%s" -r %s -s %s -f image2 "%s/%s"'%(ffmpegSource, VideoSource, FrameRate, Resolution,ImageDestination, ImageName))#+"& pause"
	return ImageName

def images2video(ffmpegPath, ImageSource, VideoDestination, TextBurn, Resolution, FrameRate, OffsetTime):
	import os
	ffmpegSource = "%s\\bin\\ffmpeg.exe"%ffmpegPath
	DecCodec = "-s %s -aspect 16:9 -vcodec libx264 -acodec aac -strict -2 -r %s -pix_fmt yuv420p"%(Resolution,FrameRate)
	os.system('%s -i "%s" -ss %s -vf "%s" %s -an -y "%s"'%(ffmpegSource, ImageSource, OffsetTime, TextBurn, DecCodec, VideoDestination))#+"& pause"

def getPaths():
	mainPaths = open("UI/MainPaths.txt","r")
	lines = (mainPaths.read()).splitlines()
	paths = {}
	for eachline in lines:
		if "FFMPEG Path:" in eachline:
			paths["FFMPEG"] =  (eachline.replace("FFMPEG Path:","")).replace(" ", "")
	return paths