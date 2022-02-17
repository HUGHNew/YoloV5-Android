## export.py

```python
parser.add_argument('--data', type=str, default=ROOT / 'data/coco128.yaml')
    parser.add_argument('--weights', type=str, default=ROOT / 'yolov5s.pt')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640, 640])
    parser.add_argument('--batch-size', type=int, default=1)
    parser.add_argument('--device', default='cpu')
    parser.add_argument('--half', action='store_true')
    parser.add_argument('--inplace', action='store_true')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--optimize', action='store_true')
    parser.add_argument('--int8', action='store_true')
    parser.add_argument('--dynamic', action='store_true')
    parser.add_argument('--simplify', action='store_true')
    parser.add_argument('--opset', type=int, default=13)
    parser.add_argument('--topk-per-class', type=int, default=100)
    parser.add_argument('--topk-all', type=int, default=100)
    parser.add_argument('--iou-thres', type=float, default=0.45)
    parser.add_argument('--conf-thres', type=float, default=0.25)
    parser.add_argument('--include', nargs='+',
                        default=['torchscript', 'onnx'])
```

`python3 export.py --simplify --weights __pt `

## onnx2ncnn.py

usage:python3 onnx2ncnn.py [64|86] file

```python
python3 onnx2ncnn.py # use onnx2ncnn-64.exe to convert weights/last-sim.onnx by default
python3 onnx2ncnn.py file # specify the file to convert
python3 onnx2ncnn.py 86 file # specify the file and execute program to convert
```
results(.param .bin file) would be saved to runs/exp\* ~~\* means saved by sequence~~