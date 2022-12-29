Step 1: Have the Jetson Inference library installed on your device.
Step 2: Move the model inside the directory: jetson-inference/python/training/classification/models
Step 3: Move the image to be classified inside the directory: jetson-inference/python/training/classification/data
Step 4: Move the label file inside the directory: jetson-inference/python/training/classification/data
Step 4: Run the following commands:

```
cd jetson-inference/python/training/classification

NET=models/[Path to directory in which model is housed, if applicable. Leave blank if the model is inside this folder and not a sub-folder.]

DATASET=data/[Path to directory in which the image to be classified is housed, if applicable. Leave blank if the image is inside this folder and not a sub-folder.]

imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/[Image to be classified].[File extension] [Name to save the classified image as].[File extension]
```

Step 5: An image with the name that you chose should be generated inside the 'classification' directory, containing some text that classifies it based on the model.