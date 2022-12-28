import jetson_inference
import jetson_utils
import argparse
import json

parser = argparse.ArgumentParser(description="Distinguish between Gold and Iron Pyrite (Fool's Gold).", formatter_class = argparse.RawTextHelpFormatter, epilog="")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
parser.add_argument("filename", type=str, help="The file being used for the machine learning.")
args = parser.parse_known_args()[0]
image_net = jetson_inference.imageNet(args.network,['--log-level=error'])
with open("labels.json", "r") as f:
    goldAndPyrite = json.load(f)
    mineralsNotRocks = goldAndPyrite.values()

img = jetson_utils.loadImage(args.filename)
class_idx,confidence = image_net.Classify(img)

class_desc = image_net.GetClassDesc(class_idx)
print("\033[92mimage is recognized as '{:s}' (class #{:d}) with {:f}% confidence\033[0m".format(class_desc, class_idx, confidence * 100))