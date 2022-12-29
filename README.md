# What is this project?

This project is an image classification model that classifies whether an image contains *Gold* or *Pyrite*. Gold is a noble metal that is very rare and is often used to make jewellery and certain pieces inside computer components. Iron Pyrite is a compound that looks similar to Gold to an untrained viewer, earning it the name of *Fool's Gold*. This model differentiates whether the image it receives is of gold or fool's gold.

# How does this project work?

This project functions by retraining the ResNet-18 model, which contains robust general parameters for image classification, to serve our purpose of differentiating between gold and pyrite. This is known as transfer learning. You can learn more about transfer learning on ResNet 18 [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-cat-dog.md).

# How to run the project:

Step 1: Have the Jetson Inference library installed on your device using [this link](https://github.com/dusty-nv/jetson-inference)

Step 2: Move the model inside the directory: jetson-inference/python/training/classification/models

Step 3: Move the image to be classified inside the directory: jetson-inference/python/training/classification/data

Step 4: Move the label file inside the directory: jetson-inference/python/training/classification/data

Step 5: Run the following commands:

```
cd jetson-inference/python/training/classification

NET=models/[Path to directory in which model is housed, if applicable. Leave blank if the model is inside this folder and not a sub-folder.]

DATASET=data/[Path to directory in which the image to be classified is housed, if applicable. Leave blank if the image is inside this folder and not a sub-folder.]

imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/[Image to be classified].[File extension] [Name to save the classified image as].[File extension]
```

Step 6: An image with the name that you chose should be generated inside the 'classification' directory, containing some text that classifies it based on the model.
