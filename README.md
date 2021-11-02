Notes for YoloV5 deployment to Android
> using [NCNN](https://github.com/Tencent/ncnn) framework

simple demo proj(ncnn) reference:<https://github.com/nihui/ncnn-android-yolov5/>

and PyTorch demo reference:<https://github.com/pytorch/android-demo-app/tree/master/ObjectDetection>

## Model Conversion

NCNN model files: .bin .param

caffe2ncnn
onnx2ncnn
keras2ncnn

PyTorch(.pt) -> onnx --onnx2ncnn-->ncnn
<https://github.com/Tencent/ncnn/wiki/use-ncnn-with-pytorch-or-onnx>
