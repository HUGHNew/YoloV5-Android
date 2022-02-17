import sys
import os
from functools import reduce

def SayUsage():
	print("usage:python3 onnx2ncnn.py [64|86] file")

def getRuns()->str:
	if os.path.exists("runs/exp0"):
		rel=reduce(lambda x,y:x if x>y else y,map(lambda x:int(x.split("xp")[1]),os.listdir("./runs")))+1
	else:
		if not os.path.exists("runs"):
			os.mkdir("runs")
		rel=0
	os.mkdir(f"runs/exp{rel}")
	return f"runs/exp{rel}"

def getModel(arg)->str:
	dot=arg.find('.')
	if dot==-1: # not .pt file
		SayUsage()
		print("failed! Not pytorch model")
	else:
		if not os.path.isfile(arg):
			print(f"file ${arg} not exists")
			return ""
		return arg[:dot].split('/')[-1]

class Run():
	@staticmethod
	def _run_(file,ver):
		fname=getModel(file)
		p=getRuns()
		fname="yolov5" if fname=="" else fname
		# print(f"onnx2ncnn-64.exe weights/{fname}.pt {p}/{fname}.param {p}/{fname}.bin")
		os.system(f"./onnx2ncnn-{ver}.exe weights/{fname}.onnx {p}/{fname}.param {p}/{fname}.bin")
	@staticmethod
	def Run64(file):
		Run._run_(file,64)
	@staticmethod
	def Run86(file):
		Run._run_(file,86)


if __name__=="__main__":
	file=sys.argv[1] if len(sys.argv)==3 else "weights/last-sim.onnx"
	if len(sys.argv)==1:
		Run.Run64(file)
	elif len(sys.argv)==2:
		if sys.argv[1]=="64":
			Run.Run64(file)
		elif sys.argv[1]=="86":
			Run.Run86(file)
		else:
			Run.Run64(sys.argv[1])
	elif len(sys.argv)==3:
		if sys.argv[1]=="64":
			Run.Run64(sys.argv[2])
		elif sys.argv[1]=="86":
			Run.Run86(sys.argv[2])
		else:
			SayUsage()
	else:
		SayUsage()