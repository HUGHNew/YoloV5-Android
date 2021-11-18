import sys
import os
from functools import reduce
def getRuns()->str:
	rel=reduce(lambda x,y:x if x>y else y,map(lambda x:int(x.split("xp")[1]),os.listdir("./runs")))+1
	os.mkdir(f"runs/exp{rel}")
	return f"runs/exp{rel}"

def getModel(arg)->str:
	dot=arg.find('.')
	if dot==-1: # not .pt file
		print("usage:python ./onnx2ncnn.py __.pt")
	else:
		if not os.path.isfile(arg):
			print("file not exists")
			return ""
		return arg[:dot].split('/')[-1]

class Run():
	@staticmethod
	def _run_(file,ver):
		fname=getModel(file)
		p=getRuns()
		fname="yolov5" if fname=="" else fname
		# print(f"onnx2ncnn-64.exe weights/{fname}.pt {p}/{fname}.param {p}/{fname}.bin")
		os.system(f"onnx2ncnn-{ver}.exe weights/{fname}.onnx {p}/{fname}.param {p}/{fname}.bin")
	@staticmethod
	def Run64(file):
		Run._run_(file,64)
	@staticmethod
	def Run86(file):
		Run._run_(file,86)

if __name__=="__main__":
	file="weights/last-sim.onnx"
	if len(sys.arg)==0:
		print("usage:python3 onnx2ncnn.py [64|86] file")
	elif len(sys.arg)==1:
		Run.Run64(file)
	else:
		if sys.argv[1]=="64":
			Run.Run64(file)
		elif sys.argv[1]=="86":
			Run.Run86(file)
		else:
			Run.Run64(sys.argv[1])